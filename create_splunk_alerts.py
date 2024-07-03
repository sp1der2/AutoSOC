import requests, urllib3, json, os, getpass
import xml.etree.ElementTree as ET

# Credentials & server informations 
username = input("Enter your Splunk username : ")
splunk_password = getpass.getpass("Enter your Splunk password : ")
splunk_base_url=input("Enter your Splunk URL : ")

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Authentication to Splunk API
auth_url = f"{splunk_base_url}/services/auth/login"
auth_data = {
    
    'username': username,
    'password': password
}

response = requests.post(auth_url, data=auth_data, verify=False)

#Parsing HTTP response in order to find the session key
root = ET.fromstring(response.text)
session_key = root.find('sessionKey').text

#Define HTTP headers
headers = {
    'Authorization': f'Splunk {session_key}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
#Function to create alerts and send them to Splunk
def create_alert():
    for fichier in os.listdir('./alerts'): # Browsing each file in the alerts folder
        with open('./alerts/' + fichier, 'r') as f: #Open each alert on RO 
            alert_actions = json.load(f) # Load the alert in JSON format
            response = requests.post(f'{splunk_base_url}/services/saved/searches', headers=headers, data=alert_actions, verify=False) #Send POST request to save alert in Splunk
            if response.status_code == 201: #Check if alert has been successfully created
                print('[SUCCESS] Alert has been successfully created !')
                f.close()
            else:
                print('[FAIL] Alert cannot be created...')
                f.close()

create_alert()

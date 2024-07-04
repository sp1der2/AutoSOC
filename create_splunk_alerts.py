#!/usr/bin/env python3

import requests, urllib3, json, os
import xml.etree.ElementTree as ET

#green and red colors for output
class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

# Credentials & server informations 

splunk_base_url = 'https://192.168.56.100:8089'
username = 'admin'
password = 'P@ssw0rd!'

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Authentication to Splunk API
auth_url = f"{splunk_base_url}/services/auth/login"
auth_data = {
    
    'username': username,
    'password': password
}

#Authentication request
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
    for fichier in os.listdir('/Splunk/alerts/'): # Browsing each file in the alerts folder
        alt_name = fichier.split('.')[0] # Extract the alert name from the file name
        with open('/Splunk/alerts/' + fichier, 'r') as f: #Open each alert file in read mode
            alert_actions = json.load(f) # Load the alert in JSON format
            response = requests.post(f'{splunk_base_url}/services/saved/searches', headers=headers, data=alert_actions, verify=False) #Send POST request to save alert in Splunk
            if response.status_code == 201: #Check if alert has been successfully created
                print(color.GREEN + '[SUCCESS] Alert : ', alt_name, 'has been successfully created !')
                f.close()
            else:
                print(color.RED + '[FAIL] Alert : ', alt_name, 'cannot be created...')
                f.close()

create_alert()

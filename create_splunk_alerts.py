import requests, urllib3
import xml.etree.ElementTree as ET

# Informations d'authentification
username = input("Entrez votre nom d'utilisateur Splunk : ")
password = input("Entrez votre mot de passe Splunk : ")

splunk_base_url = "https://localhost:8089"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Authentification et récupération du jeton de session
auth_url = f"{splunk_base_url}/services/auth/login"
auth_data = {
    'username': username,
    'password': password
}

response = requests.post(auth_url, data=auth_data, verify=False)

#Parsing de la réponse HTTP (XML) pour trouver la session_key
root = ET.fromstring(response.text)
session_key = root.find('sessionKey').text
# print(session_key)

headers = {
    'Authorization': f'Splunk {session_key}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

alert_name=input("Entrez le nom de l'alerte : ")
alert_search=input("Entrez votre requête Splunk : ")

alert_name_user = alert_name
alert_search_user = alert_search 
alert_actions = {
    'name': alert_name_user,
    'search': alert_search_user,
    'alert_type': 'number of events',
    'alert_comparator': 'greater than',
    'alert_threshold': '0',
    'alert.digest_mode': '0',
    'alert.severity': '3',
    'alert.suppress': '0',
    'alert.expires': '24h',
    'alert.track': '1',
    'is_scheduled': '1',
    'cron_schedule': '*/1 * * * *', 
}

response = requests.post(f'{splunk_base_url}/services/saved/searches', headers=headers, data=alert_actions, verify=False)

if response.status_code == 201:
    print('L\'alerte a été créée avec succès')
else:
    print('Failed to create alert')
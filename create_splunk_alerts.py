import requests, urllib3, json, os
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

headers = {
    'Authorization': f'Splunk {session_key}',
    'Content-Type': 'application/x-www-form-urlencoded'
}


def create_alert():
    for fichier in os.listdir('./alerts'):
        with open('./alerts/' + fichier, 'r') as f:
            alert_actions = json.load(f)
            response = requests.post(f'{splunk_base_url}/services/saved/searches', headers=headers, data=alert_actions, verify=False)
            if response.status_code == 201:
                print('[SUCCESS] L\'alerte a été créée avec succès !')
                f.close()
            else:
                print('[FAIL] L\'alerte n\'a pas pu être créée...')
                f.close()

create_alert()
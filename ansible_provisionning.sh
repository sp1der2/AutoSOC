#!/bin/bash

echo "192.168.56.100 splunk" >> /etc/hosts
echo "Adding Splunk Machine to /etc/hosts done"
echo "192.168.56.50 client" >> /etc/hosts
echo "Adding client Machine to /etc/hosts done"
apt-get update && apt-get install unzip pipx ansible-core -y
unzip alerts.zip
ansible-playbook -i inventory.ini -l splunk splunk.yml
ansible-playbook -i inventory.ini -l client logs_forwarder.yaml

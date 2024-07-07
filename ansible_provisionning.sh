#!/bin/bash

sudo echo "192.168.56.100 splunk" >> /etc/hosts
sudo echo "192.168.56.50 client" >> /etc/hosts
sudo apt-get update && sudo apt-get install unzip pipx -y
unzip alerts.zip 
sudo -u vagrant pipx install ansible-core
export PATH=$PATH:/home/vagrant/.local/bin
source .bashrc
ansible-playbook -i inventory.ini -l splunk splunk.yml
ansible-playbook -i inventory.ini -l client logs_forwarder.yaml
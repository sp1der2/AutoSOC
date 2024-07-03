#!/bin/bash

#Couleurs
Green='\033[1;32m'
Red='\033[1;31m'
NOCOLOR='\033[0m'
Violet='\033[1;35m'
Cyan='\033[1;36m'
Blue='\033[1;34m'

#Definition des taches
tasks=(
    
    check_prerequis
    start_vagrant
    check_splunk_active
)

#Detecter Hyperviseur 
    #Code à ajouter..


#Check si Vagrant et Ansible sont installés sur la machine hote
function check_prerequis {
    if [ -z "$(which vagrant)" ]; then
        echo -e "${Red}Vagrant n'est pas installé !${NOCOLOR}"
        exit 1
    #Code à ajouter..
    fi
    if [ -z "$(which ansible)" ]; then
        echo -e "${Red}Ansible n'est pas installé ! ${NOCOLOR}"
        exit 1
    fi
    echo -e "${Blue}Pre-requis satisfaits, poursuite du script...${NOCOLOR}"
}

#Lancement de Vagrant
function start_vagrant {
    echo -en '\n'"${Violet}*** Demarrage de Vagrant... ***"'\n\n'
    sleep 1
    vagrant up
}


#Check si Splunk est bien actif et joignable
function check_splunk_active {
    content_length=$(curl -sI http://localhost:7999 | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
    if [ -n "$content_length" ] && [ "$content_length" -eq 331 ]; then
        echo -en "${Green}[✓] Si l'installation s'est bien déroulée, vous pouvez accéder à Splunk via http://localhost:8000\n\n${NOCOLOR}${Green}[✓] Accédez à Splunk avec le compte admin:P@ssw0rd!\n\n${NOCOLOR}Pour arrêter le lab, faites 'vagrant halt' ou 'vagrant destroy -f' pour le supprimer\n"
    else
        echo "${Red}[✗] Splunk n'est pas actif !"
    fi
}

#Exécution du programme
for task in "${tasks[@]}"
do
    $task
done

#TEST GIT
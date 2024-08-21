#!/bin/bash

# Colors : 
Green='\033[1;32m'
Red='\033[1;31m'
NOCOLOR='\033[0m'

# Tasks to do : 
tasks=(
    check
)

#Checking if VirtualBox and Vagrant are installed on host
function check {
    if [ -z "$(which virtualbox)" ]; then
        echo -e "${Red}VirtualBox isn't installed or cannot be found in \$PATH. Exiting.. ${NOCOLOR}"
        exit 1
    fi
    if [ -z "$(which vagrant)" ]; then
        echo -e "${Red}Vagrant isn't installed or cannot be found in \$PATH. Exiting.. ${NOCOLOR}"
        exit 1
    fi
    echo -e "${Green}Requirements satisfied ! AutoSOC is now starting...${NOCOLOR}"
    sleep 1
    vagrant up
}

# Processing tasks
for task in "${tasks[@]}"
do
    $task
done

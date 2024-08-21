# AutoSOC

AutoSOC est un projet visant à fournir un environnement de laboratoire pour les équipes de sécurité (Blue Team) afin de s'entraîner à détecter des menaces en utilisant un SIEM (Splunk) et un serveur web vulnérable. Ce laboratoire est conçu pour être déployé rapidement à l'aide de Vagrant, et permet aux utilisateurs de simuler des attaques, puis de surveiller et d'analyser les événements à l'aide de Splunk.

## Architecture du laboratoire

Le laboratoire AutoSOC se compose de trois machines virtuelles (VM) gérées par Vagrant :

1. **VM Splunk** : Cette machine virtuelle héberge une instance de Splunk qui collecte et analyse les données de journalisation.
2. **VM Serveur Web Vulnérable** : Ce serveur web délibérément vulnérable est conçu pour simuler des failles de sécurité courantes, permettant aux équipes de tester leurs compétences en détection et réponse aux incidents.
3. **VM Serveur Ansible** : Cette machine virtuelle agit comme un serveur Ansible, utilisé pour orchestrer les déploiements et configurations des autres VMs.

## Installation

Pour installer et configurer l'environnement AutoSOC, suivez les étapes ci-dessous :

### Prérequis

Assurez-vous d'avoir les logiciels suivants installés sur votre machine :

- [Vagrant](https://www.vagrantup.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (ou tout autre fournisseur de VM compatible avec Vagrant)

### Étapes d'installation

1. Clonez le dépôt AutoSOC depuis GitHub :

    ```bash
    git clone https://github.com/votreutilisateur/AutoSOC.git
    cd AutoSOC
    ```

2. Exécutez le script d'installation :

    ```bash
    ./setup.sh
    ```

    Ce script va configurer Vagrant et lancer les trois machines virtuelles.

3. Patientez pendant la création et la configuration des machines virtuelles. Une fois le processus terminé, vous aurez accès à l'interface web de Splunk pour commencer à travailler.

## Utilisation

- Accédez à l'interface Splunk à l'adresse : `http://localhost:8000`
- Utilisez les journaux collectés pour détecter et analyser les activités suspectes provenant du serveur web vulnérable.

## Contribution

Les contributions sont les bienvenues ! Pour proposer des améliorations, des correctifs, ou de nouvelles fonctionnalités, veuillez soumettre une pull request ou ouvrir une issue sur GitHub.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

**Note** : Ce projet est destiné uniquement à des fins éducatives et de formation. N'utilisez pas ce laboratoire sur des systèmes en production.

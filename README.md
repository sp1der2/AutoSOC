![autosoc logo](https://github.com/user-attachments/assets/0a8e34a0-bb29-479c-ac7a-1bb0067745ef)

        
Made with ❤️ by AI


# AutoSOC

AutoSOC is a project aimed at providing a lab environment for security teams (Blue Team) to practice threat detection using a SIEM (Splunk) and a vulnerable web server. This lab is designed to be quickly deployed using Vagrant, allowing users to simulate attacks and then monitor and analyze events using Splunk.

# Architecture

1. **Splunk VM**: This virtual machine hosts a Splunk instance that collects and analyzes log data.
2. **Vulnerable Web Server VM**: This intentionally vulnerable web server is designed to simulate common security flaws, allowing teams to test their detection and incident response skills.
3. **Ansible Server VM**: This virtual machine acts as an Ansible server, used to orchestrate the deployment and configuration of the other VMs.

### Prerequisites
Hardware :
~ 6 vCPUs / 5 Go RAM

Software : 
- [Vagrant](https://www.vagrantup.com/downloads)
- [VirtualBox 7.0 (as 7.1 isn't supported yet by Vagrant)](https://www.virtualbox.org/wiki/Downloads)


### Installation Steps

1. Clone the AutoSOC repository from GitHub:

    ```bash
    git clone https://github.com/sp1der2/AutoSOC.git
    cd AutoSOC
    ```

2. Run the setup script:

    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```

## Usage

- After deployment, access the Splunk interface at: `https://localhost:8000`
- Use credentials admin / P@ssw0rd! to log into Splunk

## SSH to VMs
Go to AutoSOC directory and type in a terminal `vagrant ssh splunk` or `vagrant ssh client`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Note**: This project is intended for educational and training purposes only. Do not use this lab on production systems.

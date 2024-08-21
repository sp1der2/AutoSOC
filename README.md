# AutoSOC

AutoSOC is a project aimed at providing a lab environment for security teams (Blue Team) to practice threat detection using a SIEM (Splunk) and a vulnerable web server. This lab is designed to be quickly deployed using Vagrant, allowing users to simulate attacks and then monitor and analyze events using Splunk.

## Lab Architecture

The AutoSOC lab consists of three virtual machines (VMs) managed by Vagrant:

1. **Splunk VM**: This virtual machine hosts a Splunk instance that collects and analyzes log data.
2. **Vulnerable Web Server VM**: This intentionally vulnerable web server is designed to simulate common security flaws, allowing teams to test their detection and incident response skills.
3. **Ansible Server VM**: This virtual machine acts as an Ansible server, used to orchestrate the deployment and configuration of the other VMs.

## Installation

To install and configure the AutoSOC environment, follow the steps below:

### Prerequisites

Ensure you have the following software installed on your machine:

- [Vagrant](https://www.vagrantup.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

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

    This script will configure Vagrant and launch the three virtual machines.

## Usage

- Access the Splunk interface at: `http://localhost:8000`
- Check the end of setup.sh in order to see credentials to log in

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Note**: This project is intended for educational and training purposes only. Do not use this lab on production systems.

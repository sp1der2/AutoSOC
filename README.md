![autosoc logo](https://github.com/user-attachments/assets/0a8e34a0-bb29-479c-ac7a-1bb0067745ef)

        
  
Logo made with ❤️ by AI


# AutoSOC

AutoSOC is a project aimed at providing a lab environment for security teams (Blue Team) to practice threat detection using a SIEM (Splunk) and a vulnerable web server. This lab is designed to be quickly deployed using Docker, allowing users to simulate attacks and then monitor and analyze events using Splunk.

# Architecture

1. **Splunk Container**: Collect and analyze log data.
2. **DVWA**: Vulnerable Web App.

### Installation Steps

1. Just launch the compose file in your terminal :

    ```bash
    cd AutoSOC && sudo docker compose up -d
    ```

## Usage

- After deployment, access the Splunk interface at: `https://localhost:8888`
- Credentials are available in the docker compose file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Note**: This project is intended for educational and training purposes only. Do not use this lab on production systems.

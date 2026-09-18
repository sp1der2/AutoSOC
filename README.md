![autosoc logo](https://github.com/user-attachments/assets/0a8e34a0-bb29-479c-ac7a-1bb0067745ef)

        

# AutoSOC

AutoSOC provides a lab environment for Blue Teams to practice threat detection using a SIEM (Splunk) and a vulnerable web server. Quick deployment via Docker, attack simulation, and event monitoring/analysis with Splunk.

# Architecture

1. **Splunk Container**: Collect and analyze log data.
2. **DVWA**: Vulnerable Web App.

## Requirements
- Docker + Docker Compose

### Installation

(Optional) if Docker not installed, install it quickly:

```bash
curl -fsSL "https://get.docker.com/" | sh
```

1. Clone the repo and launch the compose file:

```bash
    git clone https://github.com/sp1der2/AutoSOC && cd AutoSOC && sudo docker compose up -d
```

## Usage

- Splunk interface: `https://localhost:8888`
- Credentials in the docker compose file.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

**Note**: Educational/training use only. Do not use on production systems.

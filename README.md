# Automated-Recon1
### This tool is intended only for authorised security testing and educational use. Users must obtain explicit permission before scanning any systems

The scope of the automated recon includes:
  - Subdomain enumeration (API-based)
  - DNS resolution
  - HTTP status check
  - Port scan (basic)

I may expand this scope in a later version.

### Prerequisites
python3 -m venv venv
source venv/bin/activate
pip install requests dnspython python-nmap rich typer

### Project Structure
auto-recon/
│
├── core/
│   ├── subdomain.py
│   ├── dns.py
│   ├── ports.py
│   ├── http_probe.py
│
├── utils/
│   ├── logger.py
│   ├── config.py
│
├── output/
│   ├── reporter.py
│
├── main.py
├── requirements.txt
├── README.md

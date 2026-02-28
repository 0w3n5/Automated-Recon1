# Automated-Recon1
Automated reconnaissance for pen testing. Only for use on targets you have authority to test.

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

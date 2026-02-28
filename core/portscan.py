import nmap

def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1000')

    open_ports = []

    for proto in nm[target].all_protocols():
        ports = nm[target][proto].keys()
        for port in ports:
            open_ports.append(port)

    return open_ports

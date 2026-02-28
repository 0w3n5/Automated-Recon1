import typer
from core.subdomain import get_subdomains
from core.dns import resolve_domain
from core.ports import scan_ports
from core.http_probe import check_http

app = typer.Typer()

@app.command()
def recon(domain: str):
    typer.echo(f"Starting recon on {domain}")

    subs = get_subdomains(domain)

    for sub in subs:
        typer.echo(f"\n[+] {sub}")

        ips = resolve_domain(sub)
        typer.echo(f"  IPs: {ips}")

        if ips:
            ports = scan_ports(ips[0])
            typer.echo(f"  Open Ports: {ports}")

        http = check_http(sub)
        typer.echo(f"  HTTP: {http}")

if __name__ == "__main__":
    app()

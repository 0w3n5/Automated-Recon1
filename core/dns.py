import dns.resolver

def resolve_domain(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [rdata.to_text() for rdata in answers]
    except:
        return []

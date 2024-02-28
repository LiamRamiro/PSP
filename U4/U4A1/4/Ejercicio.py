# - Enter an IP or host address and have it look it up through whois and
# return the results to you.  

import whois

def whois_lookup(domain):
    try:
        data = whois.whois(domain)
        return data.text
    except Exception as e:
        return str(e)

# Example usage
print(whois_lookup("google.com"))
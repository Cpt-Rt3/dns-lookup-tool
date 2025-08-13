#!/usr/bin/env python3
import socket
import argparse
import dns.resolver
import dns.exception

def main():
    parser = argparse.ArgumentParser(
        description="DNS Lookup Tool (IP, NS, MX)"
    )
    parser.add_argument(
        "domain",
        nargs="?",
        help="Domain to query (e.g., example.com)"
    )
    args = parser.parse_args()

    domain = args.domain.strip() if args.domain else input("Enter domain: ").strip()

    # IP lookup
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")
    except Exception as e:
        print(f"IP lookup failed: {e}")

    # NS / MX lookups
    for rtype in ("NS", "MX"):
        try:
            answers = dns.resolver.resolve(domain, rtype, lifetime=3.0)
            for r in answers:
                print(f"{rtype} Record: {r}")
        except dns.resolver.NXDOMAIN:
            print(f"{rtype} lookup: domain does not exist")
        except dns.resolver.NoAnswer:
            print(f"{rtype} lookup: no answer")
        except dns.exception.Timeout:
            print(f"{rtype} lookup: timed out")
        except Exception as e:
            print(f"{rtype} lookup error: {e}")

if __name__ == "__main__":
    main()

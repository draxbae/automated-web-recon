#!/usr/bin/env python3

import subprocess
import os
import sys


def run_subfinder(domain):
    print("\n[+] Starting subdomain enumeration...")

    result = subprocess.run(
        ["subfinder", "-d", domain, "-silent"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[-] Subfinder failed.")
        return []

    subdomains = result.stdout.strip().splitlines()

    if not subdomains:
        print("[-] No subdomains found.")
        return []

    subdomains = subdomains[:50]

    with open("results/subdomains.txt", "w") as file:
        for subdomain in subdomains:
            file.write(subdomain + "\n")

    print(f"[+] Using {len(subdomains)} subdomains.")
    print("[+] Saved to results/subdomains.txt")

    return subdomains


def run_httpx(targets):
    print("\n[+] Starting HTTP information gathering...")

    input_data = "\n".join(targets)

    result = subprocess.run(
        [
            "httpx",
            "-silent",
            "-status-code",
            "-title",
            "-web-server",
            "-tech-detect",
            "-threads", "10",
            "-timeout", "5"
        ],
        input=input_data,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[-] HTTPX failed.")
        return []

    http_info = result.stdout.strip().splitlines()

    if not http_info:
        print("[-] No HTTP information found.")
        return []

    with open("results/live_hosts.txt", "w") as file:
        for host in http_info:
            file.write(host + "\n")

    print(f"[+] Found {len(http_info)} HTTP responses.")
    print("[+] Saved to results/live_hosts.txt")

    return http_info


def run_naabu(targets):
    print("\n[+] Starting port discovery...")

    input_data = "\n".join(targets)

    result = subprocess.run(
        [
            "naabu",
            "-silent",
            "-top-ports", "100"
        ],
        input=input_data,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[-] Naabu failed.")
        return []

    ports = result.stdout.strip().splitlines()

    if not ports:
        print("[-] No open ports found.")
        return []

    with open("results/ports.txt", "w") as file:
        for port in ports:
            file.write(port + "\n")

    print(f"[+] Found {len(ports)} open ports.")
    print("[+] Saved to results/ports.txt")

    return ports


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 recon.py <domain>")
        print("Example: python3 recon.py example.com")
        print("Local test: python3 recon.py --local")
        return

    target = sys.argv[1].strip()

    os.makedirs("results", exist_ok=True)

    if target == "--local":
        print("[+] Local test mode")
        print("[+] Target: http://127.0.0.1:8000")

        targets = ["127.0.0.1"]

        with open("results/subdomains.txt", "w") as file:
            file.write("127.0.0.1:8000\n")

        print("[+] Saved to results/subdomains.txt")

        http_results = run_httpx(["http://127.0.0.1:8000"])

        if http_results:
            run_naabu(targets)

        return

    print(f"[+] Target: {target}")

    subdomains = run_subfinder(target)

    if subdomains:
        http_results = run_httpx(subdomains)

        if http_results:
            run_naabu(subdomains)
    else:
        print("[-] No subdomains available.")


if __name__ == "__main__":
    main()

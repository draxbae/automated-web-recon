# Automated Web Reconnaissance Tool

A lightweight Python-based tool that automates basic web reconnaissance tasks for authorized security assessments.

**Focus:** Web Reconnaissance • Python Automation • Penetration Testing

---

## Project Overview

Reconnaissance is an important first step in a web security assessment. It helps identify available subdomains, web services, and exposed network services before further security testing.

I built this project to automate several repetitive reconnaissance tasks and combine commonly used security tools into a simple Python workflow.

The tool currently integrates:

- **Subfinder** — passive subdomain enumeration
- **HTTPX** — HTTP probing and basic web information gathering
- **Naabu** — basic port discovery
- **Python** — workflow automation and tool integration

The project is intentionally lightweight and focuses on understanding the reconnaissance process and automating its basic workflow.

---

## How It Works

```text
Target Domain
      │
      ▼
   Subfinder
      │
      ▼
 Subdomain List
      │
      ▼
     HTTPX
      │
      ▼
 Live HTTP Hosts
      │
      ▼
    Naabu
      │
      ▼
 Basic Port Discovery
      │
      ▼
    Results

The Python script coordinates the tools and stores the resulting information locally.

Features
Passive subdomain enumeration
HTTP service discovery
HTTP status and title detection
Web server information gathering
Basic technology detection
Basic port discovery
Automated result organization
Local testing mode
Limits processing to the first 50 discovered subdomains
Tools & Technologies
Tool / Technology	Purpose
Python 3	Automation and workflow orchestration
Subfinder	Passive subdomain enumeration
HTTPX	HTTP probing and web information gathering
Naabu	Basic port discovery
Kali Linux	Security testing environment
Requirements
Python 3
Kali Linux or another Linux environment
Subfinder
HTTPX
Naabu

The required tools should be installed and available in the system PATH.

Usage

Run the tool with:

python3 recon.py <domain>

Example:

python3 recon.py example.com

For local testing:

python3 recon.py --local

The local testing mode is provided to demonstrate the workflow without requiring an external target.

Output

Reconnaissance results are stored in the results/ directory:

results/
├── subdomains.txt
├── live_hosts.txt
└── ports.txt

The results/ directory is excluded from Git through .gitignore so that local reconnaissance data is not uploaded to the repository.

Skills Demonstrated

This project demonstrates practical experience with:

Web reconnaissance
Subdomain enumeration
HTTP service discovery
Basic network reconnaissance
Python scripting
Security tool integration
Command-line workflows
Kali Linux
Learning Outcomes

Through this project, I practiced how to:

Understand the basic workflow of web reconnaissance
Automate command-line security tools using Python
Process and organize tool output
Combine multiple security utilities into a single workflow
Build a simple security automation tool
Work with Linux-based security testing environments
Ethical Use

This project is intended for authorized security assessments, security laboratories, CTF environments, and systems owned or explicitly permitted for testing.

Do not use this tool against systems or domains without authorization.

Project Status

Status: Completed — Initial Version

Future improvements may include:

Improved result parsing
Configurable scan options
Additional reconnaissance modules
Better error handling
Structured reporting

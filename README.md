# Recon Toolkit

**Defensive Cybersecurity Reconnaissance Toolkit**

A modular, educational command-line toolkit for defensive cybersecurity reconnaissance and network analysis. Built for learning networking concepts and defensive security practices.

---

## ⚠️ Ethical Use Notice

This tool is intended **only** for:

- **Educational purposes** – Learning about networking, DNS, HTTP, and security headers
- **Authorized defensive research** – On systems you own or have explicit permission to test
- **Authorized penetration testing** – Where scope and permission are documented

**Do not** use this software against systems or networks without explicit permission from the owner. Unauthorized scanning may be illegal in your jurisdiction.

The creator of this tool is not responsible for any misuse, illegal activity, or damages caused by users of this software. **You are responsible for your actions.**

---

## Features

| Module | Description |
|--------|-------------|
| **Port Scanner** | Scans common ports on a target host using TCP sockets. Shows open ports and services. |
| **DNS Analysis** | Resolves domain names to IP addresses. Supports reverse DNS lookup (IP → hostname). |
| **Directory Scanner** | Checks for common web directories (/admin, /login, /api, etc.) and reports HTTP status codes. |
| **HTTP Header Analyzer** | Fetches HTTP headers and highlights missing security headers (CSP, HSTS, X-Frame-Options, etc.). |

---

## Installation

### Prerequisites

- **Python 3.8+**

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/DevMaine12/recon_toolkit.git
   cd recon_toolkit
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

Start the toolkit from the project root:

```bash
python main.py
```

You will see the main dashboard. Navigate with numbered options:

```
====================================
RECON TOOLKIT DASHBOARD
====================================

1) Port Scanner
2) DNS Analysis
3) Directory Scanner
4) HTTP Header Analyzer
5) Legal Notice / About
6) Exit
```

Each module has its own sub-menu where you can:

- Run scans
- View last results
- Export results to TXT

**Type `esc`** at any input prompt to return to the main dashboard.

---

## Project Structure

```
recon_toolkit/
│
├── main.py                 # Entry point
├── dashboard/
│   └── dashboard.py        # Main dashboard and navigation
│
├── modules/
│   ├── port_scanner/       # TCP port scanning
│   ├── dns_lookup/         # DNS resolution and reverse lookup
│   ├── directory_scanner/  # Web directory discovery
│   ├── header_analyzer/    # HTTP security header analysis
│   └── legal_notice/       # Ethical use notice
│
├── ui/
│   ├── banner.py           # CLI banners
│   ├── cli_layout.py       # Tables and layout
│   └── menu_utils.py       # Menu input handling
│
├── utils/
│   ├── logger.py           # Timestamped logging
│   ├── validator.py        # Domain/IP validation
│   └── export.py           # TXT report export
│
├── results/                # Exported scan reports (auto-created)
├── requirements.txt
└── README.md
```

---

## Module Details

### Port Scanner
- Uses Python sockets for TCP connection attempts
- Scans common ports (22, 80, 443, 3306, etc.)
- Timeout protection to avoid hanging
- Results displayed in a table; exportable to TXT

### DNS Lookup
- Forward lookup: domain → IP address(es)
- Reverse lookup: IP → hostname (PTR records)
- Clean display of resolution results

### Directory Scanner
- Checks common paths: /admin, /login, /dashboard, /api, etc.
- Reports HTTP status codes (200, 301, 403, 404)
- Handles timeouts and connection errors

### HTTP Header Analyzer
- Fetches HTTP headers from a URL
- Highlights presence/absence of security headers:
  - Content-Security-Policy
  - Strict-Transport-Security (HSTS)
  - X-Frame-Options
  - X-Content-Type-Options
  - Referrer-Policy, Permissions-Policy, etc.

---

## Exporting Results

After running a scan, you can export results to a TXT file. Reports are saved in the `results/` directory with filenames like:

- `port_scanner_example_com_2026-03-23.txt`
- `dns_analysis_example_com_2026-03-23.txt`
- `directory_scanner_https___example_com_2026-03-23.txt`
- `http_header_analyzer_https___example_com_2026-03-23.txt`

Each report includes:
- Timestamp
- Module name
- Target
- Scan results
- Creator credit

---

## Design Principles

- **Modular** – Easy to add new modules
- **Beginner-readable** – Comments explain networking concepts
- **Robust** – Error handling; program continues if a module fails
- **Minimal dependencies** – Uses `colorama` for colored output; standard library for core logic
- **Defensive only** – No exploitation or attack features

---

## License

This project is for educational use. Use responsibly and legally.

---

## Creator

**DevMaine12** 🇨🇺 🇵🇷

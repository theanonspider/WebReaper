#!/usr/bin/env python3
"""
🕷️ WebReaper — Advanced Phishing Simulation Framework
Usage: python webreaper.py --help
"""

import click
import json
import os
import sys
from datetime import datetime

try:
    from rich.console import Console
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

VERSION = "1.0.0"
CONFIG_FILE = "config.json"
TOKEN_FILE = "webreaper.token"
BANNER = """
╔══════════════════════════════════════════════╗
║                                              ║
║   🕷️  WEBREAPER — Phishing Framework     ║
║                                              ║
║        Simulation Tool v1.0                 ║
║                                              ║
╚══════════════════════════════════════════════╝
"""

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"[!] Config file {CONFIG_FILE} not found.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def check_token():
    config = load_config()
    if not config.get("token_required", True):
        return True
    if not os.path.exists(TOKEN_FILE):
        print(f"[!] Authorization token required. Create {TOKEN_FILE}")
        return False
    with open(TOKEN_FILE, "r") as f:
        token = f.read().strip()
    if token != "WEBREAPER_AUTHORIZED":
        print("[!] Invalid token.")
        return False
    return True

@click.group()
@click.version_option(version=VERSION, prog_name="WebReaper")
def main():
    """🕷️ WebReaper — Advanced Phishing Simulation Framework"""
    pass

@main.command()
def server():
    """Start the phishing server"""
    if not check_token():
        sys.exit(1)
    config = load_config()
    print(BANNER)
    print(f"[*] Starting WebReaper server...")
    print(f"[*] Host: {config['server']['host']}")
    print(f"[*] Port: {config['server']['port']}")
    print(f"[*] Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print("[i] Server module coming soon...")

@main.command()
@click.option("--url", "-u", required=True, help="Target URL to clone")
@click.option("--output", "-o", default="./output", help="Output directory")
def clone(url, output):
    """Clone a target webpage"""
    if not check_token():
        sys.exit(1)
    print(f"[*] Cloning {url}...")
    print(f"[*] Output: {output}")
    print("[i] Clone module coming soon...")

@main.command()
def stats():
    """Show campaign statistics"""
    if not check_token():
        sys.exit(1)
    print("[i] No campaigns yet.")

if __name__ == "__main__":
    main()

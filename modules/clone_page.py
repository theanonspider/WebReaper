"""
WebReaper Module : Page Cloner
Clone target web pages for phishing simulation.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
from datetime import datetime

class ClonePageModule:
    def __init__(self, url, output_dir):
        self.url = url
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.results = {
            "module": "clone_page",
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "data": {"cloned_files": [], "forms_found": 0}
        }

    def run(self):
        print(f"\n[+] Cloning {self.url}...")
        try:
            response = self.session.get(self.url, timeout=10)
            if response.status_code != 200:
                print(f"    [!] HTTP {response.status_code}")
                return self.results

            soup = BeautifulSoup(response.text, "html.parser")
            domain = urlparse(self.url).netloc
            page_dir = os.path.join(self.output_dir, domain)
            os.makedirs(page_dir, exist_ok=True)

            # Sauvegarder le HTML
            html_path = os.path.join(page_dir, "index.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            self.results["data"]["cloned_files"].append(html_path)

            # Détecter les formulaires
            forms = soup.find_all("form")
            self.results["data"]["forms_found"] = len(forms)
            for i, form in enumerate(forms):
                action = form.get("action", "")
                method = form.get("method", "POST")
                inputs = form.find_all("input")
                print(f"    Form {i+1}: {method} {action} ({len(inputs)} fields)")

            # Télécharger les ressources (CSS, JS, images)
            for tag in soup.find_all(["link", "script", "img"]):
                attr = "href" if tag.name == "link" else "src" if tag.name in ["script", "img"] else None
                if not attr:
                    continue
                resource_url = tag.get(attr)
                if not resource_url:
                    continue
                full_url = urljoin(self.url, resource_url)
                try:
                    res = self.session.get(full_url, timeout=5)
                    if res.status_code == 200:
                        filename = os.path.basename(urlparse(full_url).path) or "resource"
                        filepath = os.path.join(page_dir, filename)
                        with open(filepath, "wb") as f:
                            f.write(res.content)
                        self.results["data"]["cloned_files"].append(filepath)
                except:
                    pass

            print(f"    Cloned {len(self.results['data']['cloned_files'])} files")
            print(f"    Forms found: {len(forms)}")
        except Exception as e:
            print(f"    [!] Clone failed: {e}")
        return self.results

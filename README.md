# 🕷️ WebReaper

> **Advanced phishing simulation framework for authorized security testing.**
> For Red Team operations and security awareness training.

---

## 📖 Description

WebReaper is a modular phishing simulation framework designed for security professionals. It allows operators to clone websites, capture credentials, manage campaigns, and generate reports for authorized security engagements.

---

## ⚠️ Warning

**This tool is for authorized use only.** Always obtain written permission before deployment.

---

## ⚙️ Installation

```bash
git clone https://github.com/theanonspider/WebReaper.git
cd WebReaper
pip install -r requirements.txt
🚀 Usage

bash
# Create authorization token (required)
echo "WEBREAPER_AUTHORIZED" > webreaper.token

# Start the server
python webreaper.py
Access the dashboard at http://localhost:8080
Login: admin / WebReaper2024!

🧩 Modules

Module	Description
clone_page	Clone target web pages (HTML, CSS, JS, images)
credential_capture	Capture submitted credentials from phishing pages
campaign_manager	Create and manage phishing campaigns
report_generator	Generate HTML and JSON reports
🎨 Interface

Web dashboard with:

Campaign management
Credential viewer
Statistics overview

👤 Author

@theanonspider

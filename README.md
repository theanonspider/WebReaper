⚙️ Installation
bash

git clone https://github.com/theanonspider/WebReaper.git
cd WebReaper
pip install -r requirements.txt
echo "WEBREAPER_AUTHORIZED" > webreaper.token

🚀 Exemples d’utilisation
bash

# 1. Cloner une page
python webreaper.py clone-page --url https://example.com

# 2. Lancer un serveur de capture
python webreaper.py credential-capture --port 8080

# 3. Créer une campagne
python webreaper.py campaign-manager --action create --name "Campagne1"

📄 Sortie

Rapports dans reports/ : HTML.
⚖️ Licence

Usage éducatif et défensif uniquement.
👤 Auteur

@theanonspider — Cybersécurité éthique. 🐺

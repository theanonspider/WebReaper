
---

## 5️⃣ WEBREAPER V1 (5 modules)

```markdown
# 🕷️ WebReaper — Phishing Tool

> ⚠️ **AVERTISSEMENT** — Usage exclusivement éducatif et défensif.  
> Toute utilisation non autorisée est **ILLÉGALE** et engage votre responsabilité.

---

## 📖 Pourquoi WebReaper ?

**WebReaper** est un outil de phishing modulaire pour les tests autorisés.  
Il permet de cloner des pages, capturer des identifiants et gérer des campagnes.

---

## 🧩 Modules (5)

| Module | Fonction |
|--------|----------|
| `clone_page` | Clonage de pages web (HTML/CSS/JS) |
| `credential_capture` | Capture d’identifiants (POST) |
| `campaign_manager` | Gestion de campagnes |
| `report_generator` | Rapports HTML/JSON |

---

## 🔐 Sécurité

```bash
echo "WEBREAPER_AUTHORIZED" > webreaper.token

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

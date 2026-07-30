
3. **Commit** : `Update README complete`

---

## PDF : `WebReaper_V1.md`

1. **Add file** → **Create new file**
2. Nom : `WebReaper_V1.md`
3. Colle :

```markdown
# 🕷️ WEBREAPER V1 — DOCUMENTATION OFFICIELLE

> **Framework de simulation de phishing pour tests de sécurité autorisés.**
> Version publique — Open Source — Usage éducatif

---

## 📊 FICHE TECHNIQUE

| Élément | Détail |
|---------|--------|
| **Nom** | WebReaper |
| **Version** | 1.0 (Publique) |
| **Type** | Framework de simulation de phishing |
| **Licence** | MIT (usage éducatif uniquement) |
| **Langage** | Python 3 |
| **Plateforme** | Multi-plateforme |
| **Interface** | Web Dashboard (Flask) |
| **Modules** | 5 |
| **Dépôt** | github.com/theanonspider/WebReaper |

---

## 🧩 MODULES

### 📄 Clone Page
- Téléchargement du HTML, CSS, JS, images
- Détection des formulaires
- Sauvegarde structurée

### 🔑 Credential Capture
- Capture des identifiants soumis
- Enregistrement IP, User-Agent
- Export JSON

### 📋 Campaign Manager
- Création de campagnes
- Suivi des clics et captures
- Statistiques

### 📊 Report Generator
- Rapport HTML stylé
- Rapport JSON complet

### 🖥️ Server
- Flask web dashboard
- API REST
- Authentification admin

---

## 🔐 SÉCURITÉ

| Mécanisme | Description |
|-----------|-------------|
| **Token** | Fichier `webreaper.token` obligatoire |
| **Authentification** | Login/password dashboard |

---

## ⚙️ INSTALLATION

```bash
git clone https://github.com/theanonspider/WebReaper.git
cd WebReaper
pip install -r requirements.txt

🚀 UTILISATION

bash
echo "WEBREAPER_AUTHORIZED" > webreaper.token
python webreaper.py
Dashboard : http://localhost:8080
Login : admin / WebReaper2024!

⚠️ AVERTISSEMENT

Cet outil est fourni à des fins exclusivement éducatives et défensives.
Toute utilisation sans autorisation écrite est ILLÉGALE.

👤 AUTEUR

@theanonspider — Cybersécurité éthique

Document généré le 31 juillet 2026

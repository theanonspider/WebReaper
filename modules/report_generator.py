"""
WebReaper Module : Report Generator
Generate phishing campaign reports.
"""

import json
import os
from datetime import datetime

class ReportGeneratorModule:
    def __init__(self, output_dir, campaign_data, credentials_data):
        self.output_dir = output_dir
        self.campaign_data = campaign_data
        self.credentials_data = credentials_data

    def generate_html(self):
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WebReaper Report</title>
    <style>
        body {{ background:#0a0a0f; color:#ccc; font-family:monospace; max-width:800px; margin:40px auto; padding:20px; }}
        h1 {{ color:#ff1a1a; }} h2 {{ color:#cc0000; border-bottom:1px solid #330000; padding-bottom:5px; }}
        pre {{ background:#0f000f; padding:15px; border-left:3px solid #990000; overflow-x:auto; }}
        .footer {{ margin-top:40px; color:#444; text-align:center; font-size:0.8em; }}
    </style>
</head>
<body>
    <h1>🕷️ WebReaper Report</h1>
    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <h2>Campaign Summary</h2>
    <pre>{json.dumps(self.campaign_data, indent=2)}</pre>
    <h2>Captured Credentials</h2>
    <pre>{json.dumps(self.credentials_data, indent=2)}</pre>
    <div class="footer">WebReaper | Educational Use Only</div>
</body>
</html>"""
        filepath = os.path.join(self.output_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        with open(filepath, "w") as f:
            f.write(html)
        return filepath

    def generate_json(self):
        report = {
            "timestamp": datetime.now().isoformat(),
            "campaigns": self.campaign_data,
            "credentials": self.credentials_data
        }
        filepath = os.path.join(self.output_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(filepath, "w") as f:
            json.dump(report, f, indent=2)
        return filepath

"""
WebReaper Module : Campaign Manager
Manage phishing campaigns.
"""

import json
import os
import uuid
from datetime import datetime

class CampaignManagerModule:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.campaigns = {}
        self._load()

    def create(self, name, target_url, template=""):
        campaign_id = str(uuid.uuid4())[:8]
        self.campaigns[campaign_id] = {
            "id": campaign_id,
            "name": name,
            "target_url": target_url,
            "template": template,
            "created": datetime.now().isoformat(),
            "status": "active",
            "clicks": 0,
            "captures": 0
        }
        self._save()
        return campaign_id

    def list(self):
        return list(self.campaigns.values())

    def get(self, campaign_id):
        return self.campaigns.get(campaign_id)

    def add_click(self, campaign_id):
        if campaign_id in self.campaigns:
            self.campaigns[campaign_id]["clicks"] += 1
            self._save()

    def add_capture(self, campaign_id):
        if campaign_id in self.campaigns:
            self.campaigns[campaign_id]["captures"] += 1
            self._save()

    def _save(self):
        os.makedirs(self.output_dir, exist_ok=True)
        filepath = os.path.join(self.output_dir, "campaigns.json")
        with open(filepath, "w") as f:
            json.dump(self.campaigns, f, indent=2)

    def _load(self):
        filepath = os.path.join(self.output_dir, "campaigns.json")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                self.campaigns = json.load(f)

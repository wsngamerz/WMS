from flask import Blueprint, render_template, request, session, redirect

from wms.security import pageData

class dashboardBlueprint:
    def __init__(self, config, db, security):
        self.dashboard = Blueprint("dashboard", __name__, url_prefix='/dashboard')
        self.main(self.dashboard, config, db, security)

    def main(self, dashboard, config, db, security):
        self.configData = config.configData

        @dashboard.route("/")
        def dashboardPage():
            pageConfig = pageData(self.configData)
            return render_template("dashboard/dashboard.html", pageName="Dashboard", config=pageConfig)

        @dashboard.route("/settings/")
        def settingsHomePage():
            pageConfig = pageData(self.configData)
            return render_template("dashboard/settings.html", pageName="Settings", config=pageConfig)

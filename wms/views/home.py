from flask import Blueprint, render_template, request, session, redirect

from wms.security import pageData

class homeBlueprint:
    def __init__(self, config, db, security):
        self.home = Blueprint("home", __name__)
        config = config
        db = db
        security = security
        self.main(self.home, config, db, security)

    def main(self, home, config, db, security):
        self.configData = config.configData

        @home.route("/")
        def homePage():
            pageConfig = pageData(self.configData)
            return render_template("home/home.html", config=pageConfig)

        @home.route("/login/", methods=["GET"])
        def loginPage():
            pageConfig = pageData(self.configData)
            return render_template("home/login.html", config=pageConfig)

        @home.route("/login/", methods=["POST"])
        def loginAction():
            pageConfig = pageData(self.configData)
            username = str(request.form["username"])
            password = str(request.form["password"])
            session["loggedIn"] = True
            return redirect(str(pageConfig["request"]["rootURL"]), code=302)

        @home.route("/register/")
        def registerPage():
            pageConfig = pageData(self.configData)
            return render_template("home/register.html", config=pageConfig)

        @home.route("/logout/", methods=['GET'])
        def logoutPage():
            pageConfig = pageData(self.configData)
            return render_template("home/logout.html", config=pageConfig)

        @home.route("/logout/", methods=['POST'])
        def logoutAction():
            pageConfig = pageData(self.configData)
            session["loggedIn"] = False
            return redirect(str(pageConfig["request"]["rootURL"]), code=302)

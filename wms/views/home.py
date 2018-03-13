from flask import Blueprint, render_template, request, session, redirect

from wms.security import pageData

class homeBlueprint:
    def __init__(self, config, database, security):
        self.home = Blueprint("home", __name__)
        self.main(self.home, config, database, security)

    def main(self, home, config, database, security):
        self.configData = config.configData

        @home.route("/")
        def homePage():
            pageConfig = pageData(self.configData)
            return render_template("home/home.html", pageName="Home", config=pageConfig)

        @home.route("/login/", methods=["GET"])
        def loginPage():
            pageConfig = pageData(self.configData)
            return render_template("home/login.html", pageName="Login", config=pageConfig)

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
            return render_template("home/register.html", pageName="Register", config=pageConfig)

        @home.route("/register/", methods=["POST"])
        def registerAction():
            pageConfig = pageData(self.configData)
            fname = str(request.form["firstName"])
            lname = str(request.form["lastName"])
            username = str(request.form["username"])
            password = str(request.form["password"])
            passwordConfirm = str(request.form["passwordConfirm"])
            email = str(request.form["email"])
            validation = security.accountValidator(username, password, passwordConfirm, email)
            if validation == []:
                user = database.User(username=username, password=password, firstName=fname, lastName=lname, email=email)
                database.db.session.add(user)
                database.db.session.commit()
                session["loggedIn"] = True
                return redirect(str(pageConfig["request"]["rootURL"]), code=302)
            else:
                session["loggedIn"] = False
                return render_template("home/regError.html", pageName="Registration Error", config=pageConfig, errors=validation)

        @home.route("/logout/", methods=['GET'])
        def logoutPage():
            pageConfig = pageData(self.configData)
            return render_template("home/logout.html", pageName="Logout", config=pageConfig)

        @home.route("/logout/", methods=['POST'])
        def logoutAction():
            pageConfig = pageData(self.configData)
            session["loggedIn"] = False
            return redirect(str(pageConfig["request"]["rootURL"]), code=302)

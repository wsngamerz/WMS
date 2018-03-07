from flask import render_template, session, request, redirect

class Routes:
    def __init__(self, app, configData):
        self.configData = configData
        self.routes(app)

    def routes(self, app):

        @app.route("/")
        def indexPage():
            pageData = self.setConfig()
            return render_template('index.html', pageName="Home", config=pageData)

        @app.route("/settings/")
        def settingsPage():
            pageData = self.setConfig()
            return render_template("settings.html", pageName="Settings", config=pageData)

        # User Account Section
        @app.route("/login/", methods=['POST'])
        def loginAction():
            pageData = self.setConfig()
            username = str(request.form["username"])
            password = str(request.form["password"])
            session["loggedIn"] = True
            return redirect(str(pageData["request"]["rootURL"]), code=302)

        @app.route("/login/", methods=['GET'])
        def loginPage():
            pageData = self.setConfig()
            return render_template('login.html', pageName="Login", config=pageData)

        @app.route("/register/", methods=['POST'])
        def registerAction():
            pageData = self.setConfig()
            fname = str(request.form["firstName"])
            lname = str(request.form["lastName"])
            username = str(request.form["username"])
            password = str(request.form["password"])
            passwordConfirm = str(request.form["passwordConfirm"])
            email = str(request.form["email"])
            session["loggedIn"] = True
            return redirect(str(pageData["request"]["rootURL"]), code=302)

        @app.route("/register/", methods=['GET'])
        def registerPage():
            pageData = self.setConfig()
            return render_template('register.html', pageName="Register", config=pageData)

        @app.route("/logout/", methods=['POST'])
        def logoutAction():
            pageData = self.setConfig()
            session["loggedIn"] = False
            return redirect(str(pageData["request"]["rootURL"]), code=302)

        @app.route("/logout/", methods=['GET'])
        def logoutPage():
            pageData = self.setConfig()
            return render_template('logout.html', pageName="Logout", config=pageData)

        # Library Sections
        @app.route("/music/")
        def musicPage():
            pageData = self.setConfig()
            return render_template('music.html', pageName="Music", config=pageData)

        @app.route("/films/")
        def filmsPage():
            pageData = self.setConfig()
            return render_template('films.html', pageName="Films", config=pageData)

        @app.route("/tv/")
        def tvPage():
            pageData = self.setConfig()
            return render_template('tv.html', pageName="TV Shows", config=pageData)

    def setConfig(self):
        pageData = self.configData
        pageData["user"] = {}
        if not session.get("loggedIn"):
            pageData["user"]["loggedIn"] = False
        else:
            # pageData["user"]["data"] = db.Get.user(session["loggedIn"], pageData)
            # TODO: DB Get class
            pageData["user"]["loggedIn"] = True
        pageData["request"] = {}
        pageData["request"]["rootURL"] = str(request.url_root)
        return pageData

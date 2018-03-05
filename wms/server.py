from flask import Flask, render_template, session, request, redirect
import logging, random
from wms import config, db

app = Flask(__name__)

class Server:
    def __init__(self, config):
        logging.info("Initialising Server")
        self.configData = config.configData
        self.serverRoutes()
        self.runServer()

    def serverRoutes(self):
        logging.info("Setting Routes")

        @app.route("/")
        def indexPage():
            pageData = self.authentication()
            return render_template('index.html', pageName="Home", config=pageData)

        @app.route("/login/", methods=['POST'])
        def loginAction():
            pageData = self.authentication()
            username = str(request.form["username"])
            password = str(request.form["password"])
            session["loggedIn"] = True
            return redirect(str(pageData["request"]["rootURL"]), code=302)

        @app.route("/login/", methods=['GET'])
        def loginPage():
            pageData = self.authentication()
            return render_template('login.html', pageName="Login", config=pageData)

        @app.route("/register/", methods=['POST'])
        def registerAction():
            pageData = self.authentication()
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
            pageData = self.authentication()
            return render_template('register.html', pageName="Register", config=pageData)

        @app.route("/logout/", methods=['POST'])
        def logoutAction():
            pageData = self.authentication()
            session["loggedIn"] = False
            return redirect(str(pageData["request"]["rootURL"]), code=302)

        @app.route("/logout/", methods=['GET'])
        def logoutPage():
            pageData = self.authentication()
            return render_template('logout.html', pageName="Logout", config=pageData)

        @app.route("/music/")
        def musicPage():
            pageData = self.authentication()
            return render_template('music.html', pageName="Music", config=pageData)

        @app.route("/films/")
        def filmsPage():
            pageData = self.authentication()
            return render_template('films.html', pageName="Films", config=pageData)

        @app.route("/tv/")
        def tvPage():
            pageData = self.authentication()
            return render_template('tv.html', pageName="TV Shows", config=pageData)

    def randomBool(self):
        return bool(random.getrandbits(1))

    def authentication(self):
        pageData = self.configData
        pageData["user"] = {}
        if not session.get("loggedIn"):
            pageData["user"]["loggedIn"] = False
        else:
            # pageData["user"]["data"] = db.Get.user(session["loggedIn"], pageData)
            # TODO: DB Get class
            pageData["user"]["loggedIn"] = True
        pageData = self.addRequestInfo(pageData)
        return pageData

    def addRequestInfo(self, pageData):
        pageData["request"] = {}
        pageData["request"]["rootURL"] = str(request.url_root)
        return pageData

    def runServer(self):
        app.secret_key = self.configData["Security"]["salt"]
        app.run(self.configData["Server"]["hostname"], int(self.configData["Server"]["port"]))

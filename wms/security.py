from flask import session, request
import logging, re

class Security:
    def __init__(self, config):
        logging.info("Initialising Security")

    def accountValidator(self, username, password, passwordConfirm, email):
        error = []
        if len(username) < 5:
            error.append("Username is too short!")
        if len(username) > 250:
            error.append("Username is too long!")
        if len(password) < 8:
            error.append("Password is too short!")
        if len(password) > 60:
            error.append("Password is too long!")
        if password != passwordConfirm:
            error.append("Passwords Don't Match!")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error.append("Email is not valid")

        return error

def pageData(pageData):
    pageData["user"] = {}
    if not session.get("loggedIn"):
        pageData["user"]["loggedIn"] = False
    else:
        # pageData["user"]["data"] = db.Get.user(session["loggedIn"], pageData)
        # TODO: DB Get class
        # DEV: Using Temporary Hard-Coded Data to fill Templates
        pageData["user"]["loggedIn"] = True
        pageData["user"]["data"] = {}
        pageData["user"]["data"]["firstName"] = "TestFirstName"
        pageData["user"]["data"]["lastName"] = "TestLastName"
        pageData["user"]["data"]["username"] = "TestUsername"
    pageData["request"] = {}
    pageData["request"]["rootURL"] = str(request.url_root)
    return pageData

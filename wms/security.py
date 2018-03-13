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

def pageData(pageData, database):
    pageData["User"] = {}
    if session.get("loggedIn") == False:
        pageData["User"]["loggedIn"] = False
    else:
        if session.get("userID") != None:
            userData = database.User.query.get(session.get("userID"))
            pageData["User"]["loggedIn"] = True
            pageData["User"]["firstName"] = userData.firstName
            pageData["User"]["lastName"] = userData.lastName
            pageData["User"]["fullName"] = userData.fullName
            pageData["User"]["username"] = userData.username
            pageData["User"]["email"] = userData.email
    pageData["Request"] = {}
    pageData["Request"]["rootURL"] = str(request.url_root)
    return pageData

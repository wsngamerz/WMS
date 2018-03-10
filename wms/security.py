from flask import session, request
import logging

class Security:
    def __init__(self, config):
        logging.info("Initialising Security")

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

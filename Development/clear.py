import os

filesToDelete = ["../database/main.db",
                 "../database/users.db",
                 "../database/libraries/music.db",
                 "../database/libraries/films.db",
                 "../database/libraries/tv.db",
                 "../logs/main.log",
                 "../config.ini"]

for f in filesToDelete:
    if os.path.isfile(f):
        os.remove(f)
        print("Deleted File: " + str(f))

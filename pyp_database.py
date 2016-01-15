import os
import shutil
import table
import database
from datetime import date

def create_database(path):
    if os.path.exists(path):
        raise OSError("Can only create database from a path that does not exist")
    else:
        try:
            os.makedirs(path)
            cwd = os.getcwd()
            os.chdir(path)
            dbname = os.path.split(path)[-1]
            open(dbname + ".db", 'a').close()
            os.chdir(cwd)
        except:
            pass

def delete_database(path, confirmation=True):
    if not os.path.exists(path):
        raise OSError("Path does not exist, can not be a database")
    dbname = os.path.split(path)[-1]
    dbfilepath = os.path.join(path, dbname + ".db")
    if not os.path.isfile(dbfilepath):
        raise OSError("Path exists but the directory is not a database")

    if confirmation:
        print "This operation will delete the following files. do you with to proceed? y / N"
        for path, dirs, files in os.walk(path):
          print path,
          for f in files:
            print f,
        print ""
        decision = raw_input("> ")
        if decision == "y":
            shutil.rmtree(path)
    else:
        shutil.rmtree(path)


def use(path):
    return database.Database(path)


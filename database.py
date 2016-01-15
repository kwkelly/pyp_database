import table
import csv
import os

class Database(object):
    def __init__(self, path):
        if not os.path.exists(path):
            raise OSError("Path does not exist, can not be a database")
        dbname = os.path.split(path)[-1]
        dbfilepath = os.path.join(path, dbname + ".db")
        if not os.path.isfile(dbfilepath):
            raise OSError("Path exists but the directory is not a database")
        self.path = path
        
        # attach the table attributes
	for fn in os.listdir(path):
            filename, file_extension = os.path.splitext(fn)
            if os.path.isfile(fn) and file_extension == ".table":
                setattr(self, filename, table.Table(fn))
        
    def create_table(self, name, columns=None):
        table_path = os.path.join(self.path, name + ".table")
        if os.path.exists(table_path):
            raise OSError("Table exists")
        with open(table_path, 'a') as t:
            wr = csv.writer(t)
            wr.writerow(columns)
        setattr(self, name, table.Table(table_path))

        






import csv

class Table(object):
    def __init__(self, path):
        self.path = path

    def insert(self, *args, **kwargs):
        with open(self.path, 'rb') as table_file:
            table_reader = csv.reader(table_file)
            columns = next(table_reader)
            num_cols = len(columns)
        if len(args) != num_cols:
            raise ValueError("Can not insert different number of columns")
        else:
            with open(self.path, 'ab') as table_file:
                w = csv.writer(table_file)
                w.writerow(args)

    def query(self, **kwargs):
        if len(kwargs) != 1:
            raise ValueError("Only one kwarg allowed")
        key = dict.keys()[0]
        with open(self.path, 'rb') as table_file:
            table_reader = csv.reader(table_file)
            columns = next(table_reader)
        if key not in columns:
            raise ValueError("Key not in table")
        # get the column for the key



            
            

   
    def show(self):
        with open(self.path, 'rb') as table_file:
            table_reader = csv.reader(table_file)
            for row in table_reader:
                print ', '.join(row)

 

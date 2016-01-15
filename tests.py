import unittest
import pyp_database
import os
from datetime import date

class TestCase(unittest.TestCase):

    def test_create_database(self):
        pyp_database.create_database("imdb")
        self.assertTrue(os.path.exists("imdb"))
        pyp_database.delete_database("imdb", confirmation=False)

    def test_use_create(self):
        pyp_database.create_database("imdb")
        db = pyp_database.use("imdb")
        db.create_table('actors', columns=['id', 'name', 'date_of_birth'])
        self.assertTrue(os.path.exists("imdb/actors.table"))
        pyp_database.delete_database("imdb", confirmation=False)

    def test_use_insert(self):
        pyp_database.create_database("imdb")
        db = pyp_database.use("imdb")
        db.create_table('actors', columns=['id', 'name', 'date_of_birth'])
        self.assertTrue(hasattr(db, "actors"))
        db.create_table('other_actors', columns=['id', 'name', 'date_of_birth'])
        self.assertTrue(hasattr(db, "other_actors"))
        db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8))
        db.actors.show()
        db.other_actors.show()
        pyp_database.delete_database("imdb", confirmation=False)

    """
    def test_query(self):
        create_database("imdb")
        db = use("imdb")
        db.create_table('actors', columns=['id', 'name', 'date_of_birth'])
        self.assertTrue(hasattr(db, "actors"))
        db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8))
        db.actors.show()
        delete_database("imdb", confirmation=False)
    """


if __name__ == "__main__":
    unittest.main()

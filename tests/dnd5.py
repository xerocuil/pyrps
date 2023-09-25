import os
import sqlite3
import unittest


# Globals

APPDIR = os.path.dirname(os.path.realpath(__file__))
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()


# Testing
class TestUtils(unittest.TestCase):

  ## Init
  def setUp(self):
    self.db_path = os.path.join(APPDIR, 'db.sqlite3')

  ## Functions
  
  ''' Check table for data '''
  def check_table(self, table):
    query = 'SELECT count(*) FROM ' + table
    query_r = cursor.execute(query)
    for r in query_r:
      return r[0]

  ## Database Testing
  def test_dbConnection(self):

    ''' Check if db exists '''
    self.assertTrue(os.path.exists(self.db_path), 'database not found.')

    ''' Check if tables have data '''
    self.assertNotEqual(self.check_table('dnd5_armor'), 0, 'No data in dnd5_armor')
    self.assertNotEqual(self.check_table('dnd5_cclass'), 0, 'No data in dnd5_cclass')
    # self.assertNotEqual(self.check_table('dnd5_monster'), 0, 'No data in dnd5_monster')
    self.assertNotEqual(self.check_table('dnd5_race'), 0, 'No data in dnd5_race')
    self.assertNotEqual(self.check_table('dnd5_shield'), 0, 'No data in dnd5_shield')
    # self.assertNotEqual(self.check_table('dnd5_spell'), 0, 'No data in dnd5_spell')
    self.assertNotEqual(self.check_table('dnd5_weapon'), 0, 'No data in dnd5_weapon')


if __name__ == "__main__":
  unittest.main()
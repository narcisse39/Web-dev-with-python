__author__ = 'Narcisse'
from pymongo import MongoClient

class Database(object):
    URI ='mongodb://localhost:27017'
    DATABASE = None

    @staticmethod
    def initialize():
        client = MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find_one(collection,query):
       return  Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find(collection,query):
        return Database.DATABASE[collection].find(query)

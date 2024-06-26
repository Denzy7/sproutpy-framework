import mysql.connector as mysqlConnector
import psycopg2
import pymongo
import sqlite3

class DatabaseManager:
    def __init__(self, database_config = {}):
        self.config = database_config
        self.connection = None

    def connect(self):
        if self.config['default'] == 'mysql':
            try:
                self.config = self.config['mysql_database'] 
                self.connection = mysqlConnector.connect(
                    host=self.config['host'],
                    user=self.config['user'],
                    password=self.config['password'],
                    database=self.config['database']
                )
                print("Connected to the MySQL database!")
            except mysqlConnector.Error as err:
                print("MySQL Error: ", err)
        elif self.config['default'] == 'sqlite':
            try:
                self.config = self.config['sqlite_database']
                self.connection = sqlite3.connect(self.config['database'])
                print("Connected to the SQLite database!")
            except sqlite3.Error as err:
                print("SQLite Error: ", err)
        elif self.config['default'] == 'mongodb':
            try:
                self.config = self.config['mongodb_database']
                client = pymongo.MongoClient(self.config['host'])
                db_name = self.config['database']
                self.connection = client[db_name]
                print("Connected to the MongoDB!")
            except pymongo.errors.ConnectionError as err:
                print("MongoDB Error: ", err)
        elif self.config['default'] == 'postgresql':
            try:
                self.config = self.config['postgresql_database']
                self.connection = psycopg2.connect(
                    host=self.config['host'],
                    user=self.config['user'],
                    password=self.config['password'],
                    database=self.config['database']
                )
                print("Connected to the PostgreSQL database!")
            except psycopg2.Error as err:
                print("PostgreSQL Error: ", err)
        else:
            print("Unsupported database connection type!")

        return self.connection
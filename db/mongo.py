from configparser import RawConfigParser
from pymongo import MongoClient


class Mongo:
    __DB_CLIENT: MongoClient = None

    __CONFIG_SECTION_NAME = "Mongo"
    config: RawConfigParser = None

    def __init__(self, config: RawConfigParser):
        self.config = config

    def __exit__(self):
        self.close_db()

    def __is_connected(self):
        return self.__DB_CLIENT is not None

    def __get_config_value(self, key: str):
        return self.config.get(self.__CONFIG_SECTION_NAME, key)

    def get_db(self):
        database = self.config.get(self.__CONFIG_SECTION_NAME, "database")

        if self.__is_connected():
            print("- Mongo.get_db: Already connected to DB!")
            return self.__DB_CLIENT.get_database(database)
        else:
            protocol = self.__get_config_value("protocol")
            username = self.__get_config_value("username")
            password = self.__get_config_value("password")
            domain = self.__get_config_value("domain")

            uri = f"{protocol}://{username}:{password}@{domain}/?retryWrites=true&w=majority"

            self.__DB_CLIENT = MongoClient(uri)
            db = self.__DB_CLIENT.get_database(database)
            print("- Mongo.get_db: Connected to DB")
            return db

    def close_db(self):
        if self.__is_connected():
            self.__DB_CLIENT.close()
            self.__DB_CLIENT = None
            print("- Mongo.close_db: DB connection has been closed!")
            return True
        else:
            print("- Mongo.close_db: DB connection was already closed!")
            return False

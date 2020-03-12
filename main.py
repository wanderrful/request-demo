import requests
import json
import configparser

from db import Mongo


def print_reqres():
    r = requests.get("https://reqres.in/api/users?page=1")
    print(r.status_code)
    for data in r.json()["data"]:
        print(json.dumps(data, indent=4))


def get_content(connection):
    """
    This assumed "test" collection could promoted to a Config variable as well, but I had to draw a line _somewhere_ for demonstration purposes
    """
    content = connection.get_db().get_collection("test").find_one({})
    print(content)


def get_collections(connection):
    collections = connection.get_db().list_collection_names()
    print(f"Collections in this database: {collections}")


if __name__ == "__main__":
    config = configparser.RawConfigParser()
    config.read("config.cfg")

    mongo = Mongo(config)

    try:
        while True:
            cmd = input("blah: ").lower()
            if cmd == "exit":
                break
            elif cmd == "help":
                print("Available commands: exit, help, close, collections, reqres, (any)")
            elif cmd == "close":
                mongo.close_db()
            elif cmd == "collections":
                get_collections(mongo)
            elif cmd == "reqres":
                print_reqres()
            else:
                get_content(mongo)
    except (KeyboardInterrupt, SystemExit):
        mongo.close_db()
        print("> program interrupted!")
    finally:
        mongo.close_db()
        print("> program completed!")

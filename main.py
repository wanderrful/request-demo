import requests
import json
from db import Database
import configparser


def print_reqres():
    r = requests.get("https://reqres.in/api/users?page=1")
    print(r.status_code)
    for data in r.json()["data"]:
        print(json.dumps(data, indent=4))


def get_word(english):
    this_word = db.get_db().get_collection("test").find({})

    print(this_word)


if __name__ == "__main__":
    config = configparser.RawConfigParser()
    config.read("config.cfg")

    db = Database(config)

    while True:
        try:
            cmd = input("blah: ").lower()
            if cmd == "exit":
                break
            elif cmd == "close":
                db.close_db()
            else:
                get_word("making it good")
        except (KeyboardInterrupt, SystemExit):
            db.close_db()
            print("> program interrupted!")

    db.close_db()
    print("> program completed!")
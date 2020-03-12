# Python Request Demo!

This is a demonstration Python repository that shows how to interact with a Mongo database through a single, persistent connection!

The main things on display here are:
- That we can perform Mongo DB queries and operations with a single connection, without having to create a new one each time we want to ask Mongo for information.
- That we can manage closing and re-opening connections so that we only ever need to have one alive at a time.
- That we can use the built-in Python ConfigParser to manage our connection information
- That we can also hit APIs as needed to gather information

# Setup

## Requirements:

- Python 3.6 or higher
- PIP
- Connection information for a live Mongo server (or some other Mongo Cloud server)

## Installation:

- `cd` into the same folder as this README file
- `pip install -r requirements.txt`
- Rename the `config.example.cfg` file to just `config.cfg`
- Replace the placeholder information in that `config.cfg` file with your own Mongo server's relevant information!
- Run the `main.py` Python file however you normally do it

# Usage Notes:

- For the sake of demonstration, we're assuming that the Mongo database, described in your Config file, has a collection called "test" and that it does not contain a ridiculously large number of documents.
- To use, simply hit Enter to query your Mongo database's "test" collection. The first time, you will see a "connecting" message, but every time after that you will see that you will instead use the already-existing connection (rather than making a new one each time!)
- When a connection is live, type "collections" and hit Enter to see the list of all collections in your "test" database.
- To close your connection (so that you can re-open a new one with subsequent queries), just type "close" and hit Enter.
- Lastly, to see an (unrelated) demonstration for how to perform HTTP requests, type "reqres" and hit Enter to query the public API of the ReqRes.in website.
- To (gracefully) exit the program, just type "exit" and hit Enter. You will see that your connection to the Mongo server will be closed before shutting down.
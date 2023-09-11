import logging
import sys
from os import getenv

from pymongo import MongoClient
from pymongo.errors import ConfigurationError, ConnectionFailure, InvalidURI

logging.basicConfig(
    format="%(asctime)s | %(filename)s:%(lineno)s >>> %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level="DEBUG",
    filemode="a",
    filename="error.log",
)

logging.warning("Something bad is going to happen")


def connect_to_db(db_name: str):
    try:
        client = MongoClient(getenv("MONGO_URI"))
    except InvalidURI as err:
        print(f"Invalid URI provided! \n {err}")
        sys.exit(1)
    except ConfigurationError as err:
        print(f"Configuration error, Invalid credentials! \n {err}")
        sys.exit(1)
    except ConnectionFailure as err:
        print(f"Connection failure, Server Unavailable! \n {err}")
        sys.exit(1)
    except Exception as err:
        print(f"Unknown error! Please contact the devs here https://github.com/MCUxDaredevil/mongo-uploader \n\n {err}")
        if getenv("LOGGING") == "True":
            send_log(err)
        sys.exit(1)
    else:
        return client, client[db_name]


def send_log(err):
    # TODO: Implement logging
    pass

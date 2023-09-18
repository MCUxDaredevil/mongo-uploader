import logging
import sys
from os import getenv

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConfigurationError, ConnectionFailure, InvalidURI

load_dotenv(override=True)

logging.basicConfig(
    format="\n\n%(asctime)s | %(filename)s:%(lineno)s >>> %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level="DEBUG",
    filemode="a",
    filename="error.log",
)


def connect_to_db(db_name: str) -> tuple[MongoClient, Database]:
    """Connect to the database and return the client and the database"""
    try:
        print(getenv("MONGO_URI"))
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
        print("Unknown error! Please contact the devs - https://github.com/MCUxDaredevil/mongo-uploader/issues")
        print("You can find the log of this error in the error.log file\n")

        if getenv("LOGGING") == "True":
            logging.exception(err)
        sys.exit(1)
    else:
        return client, client[db_name]

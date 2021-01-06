import json
import requests
from pprint import pformat, pprint

from vault import Vault
from hue import Hue

from logger import logging, LOG_FILE, FORMATTER, TIMESTAMP, LOG_LEVEL
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

formatter = logging.Formatter(FORMATTER, TIMESTAMP)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def main():
    # find hue bridge
    # TODO: handle invalid ip
    logger.debug("Locating Hue Bridge")
    json_discover = Hue.get(url="https://discovery.meethue.com/")
    Vault.set_id(json_discover["id"])
    Vault.set_ip(json_discover["internalipaddress"])
    logger.info(f"Hue Bridge located at {Vault.get_ip()}")

    # get api username
    # TODO: check for non-existent file
    logger.info("Loading API username from file")
    with open("username.txt", "r") as file:
        Vault.set_username(file.read().strip())
    logger.info(f"username <{Vault.get_username()}> loaded from file")

    # test username
    # TODO: test the username somehow
    # Hue.test_username()

    # load lights
    lights = Hue.get_lights()
    pprint(lights)

    # load groups

    # load scenes


if __name__ == "__main__":
    logger.info("__INIT__")
    main()

    logger.info("__EOF__")

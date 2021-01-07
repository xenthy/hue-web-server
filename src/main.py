import json
import requests
from pprint import pformat, pprint

from vault import Vault
from hue import Hue
from light import Light
from group import Group
from scene import Scene

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
    light_list = [Light(k, v) for k, v in lights.items()]
    Vault.set_lights(light_list)
    pprint(light_list)

    # load groups
    groups = Hue.get_groups()
    group_list = [Group(k, v) for k, v in groups.items()]
    Vault.set_groups(group_list)
    pprint(group_list)

    # load scenes
    scenes = Hue.get_scenes()
    scene_list = [Scene(k, v) for k, v in scenes.items() if "group" in v]
    Vault.set_scenes(scene_list)
    pprint(scene_list)


def test():
    from random import randrange
    import time

    for light in Vault.get_lights():
        Hue.set_light(light.id, hue=randrange(0, 65535))

    time.sleep(2)

    Hue.set_group("1", randrange(0, 65535))

    time.sleep(2)

    scene_list = Vault.get_scenes()
    random_scene = scene_list[randrange(0, len(scene_list) - 1)]
    Hue.set_scene(random_scene)
    print(random_scene)


if __name__ == "__main__":
    logger.info("__INIT__")
    main()
    test()
    logger.info("__EOF__")

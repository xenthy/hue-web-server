import json
import requests

from pprint import pformat

from vault import Vault

from logger import logging, LOG_FILE, FORMATTER, TIMESTAMP, LOG_LEVEL
logger = logging.getLogger(__name__)

formatter = logging.Formatter(FORMATTER, TIMESTAMP)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Hue():
    @staticmethod
    def get(*args, url=None) -> dict:
        if url is not None:
            r = requests.get(url)
            return json.loads(r.content.decode())[0]
        r = requests.get(Vault.get_url() + "/".join(args))
        return Hue.validate(r)

    @staticmethod
    def put(*args, data=dict()) -> dict:
        r = requests.put(Vault.get_url() + "/".join(args), data=json.dumps(data))
        return Hue.validate(r)

    @staticmethod
    def post(*args, data=dict()):
        r = requests.post(Vault.get_url() + "/".join(args), data=json.dumps(data))
        return Hue.validate(r)

    @staticmethod
    def validate(r):
        r = json.loads(r.content.decode())
        if isinstance(r, list) and "error" in r[0]:
            logger.warning(f"API error: {r[0]['error']['description']}")
            return r[0]["error"]
        return r

    @staticmethod
    def test_key():
        r = Hue.get()

        print(pformat(r))

    @staticmethod
    def get_lights() -> dict:
        return Hue.get("lights")


if __name__ == "__main__":
    pass

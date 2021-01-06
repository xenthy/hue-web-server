from logger import logging, LOG_FILE, FORMATTER, TIMESTAMP, LOG_LEVEL
logger = logging.getLogger(__name__)

formatter = logging.Formatter(FORMATTER, TIMESTAMP)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Vault():
    @staticmethod
    def set_id(hue_id):
        Vault.__hue_id = hue_id

    @staticmethod
    def get_id():
        return Vault.__hue_id

    @staticmethod
    def set_ip(hue_ip):
        Vault.__hue_ip = hue_ip

    @staticmethod
    def get_ip():
        return Vault.__hue_ip

    @staticmethod
    def set_username(hue_username):
        Vault.__hue_username = hue_username

    @staticmethod
    def get_username():
        return Vault.__hue_username
    
    @staticmethod
    def get_url() -> str:
        return "http://" + Vault.get_ip() + "/api/" + Vault.get_username() + "/"


if __name__ == "__main__":
    pass

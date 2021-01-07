from logger import logging, LOG_FILE, FORMATTER, TIMESTAMP, LOG_LEVEL
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

formatter = logging.Formatter(FORMATTER, TIMESTAMP)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Scene:
    def __init__(self, k, v):
        self.id = k
        self.name = v["name"]
        try:
            self.group_id = v["group"]
        except:
            self.group_id = "0"

    def __repr__(self):
        return f"{self.id}: {self.name} - {self.group_id}"

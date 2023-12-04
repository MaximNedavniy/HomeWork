import logging
from logging import StreamHandler, FileHandler
logger = logging.getLogger("name1")
logger.addHandler(StreamHandler())
logger.setLevel(logging.DEBUG)
class MyContextManager:

    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.file_temp = open(self.file, self.mode)
        log_message = f"A file named '{self.file}' is opened, the file contains {len(self.file_temp.read())} characters"
        logger.info(log_message)
        self.file_temp.seek(0)
        return self.file_temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file_temp.close


if __name__ == "__main__":
    with MyContextManager("tests/testfile.json", "r") as my_file:
        print(my_file.read())


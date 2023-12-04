import re


class Mail:

    def __init__(self, email):
        self.validate(email)

    @staticmethod
    def validate(email):
        pattern = r'^[a-zA-Z0-9][a-zA-Z0-9]*(?:[._-](?![._-])[a-zA-Z0-9]+)*@[a-zA-Z]+(?:[.-][a-zA-Z]+)*\.[a-zA-Z]{2,}$'# Дякую ChatGPT за допомогу)
        if re.match(pattern, email):
            print("Ok")
        else:
            print("Error")


wrong = [
    "abc.def@mail.c",
    "abc.def@mail#archive.com",
    "abc.def@mail",
    "abc.def@mail..com"]
right = [
    "abc.def@mail.cc",
    "abc.def@mail-archive.com",
    "abc.def@mail.org",
    "abc.def@mail.com"]

for i in right:
    Mail.validate(i)


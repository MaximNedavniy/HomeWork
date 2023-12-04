class CustomException(Exception):
    def __init__(self, msg):

        with open("logs.txt", "a") as file:
            file.write(msg + "\n")


raise CustomException("Error")

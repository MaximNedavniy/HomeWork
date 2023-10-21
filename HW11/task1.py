def create_and_write_file():
    with open("myfile.txt", "w") as file:
        return file.write("Hello file World!\n")
def read_file():
    with open("myfile.txt", "r") as file:
        return print(file.readline())

#create_and_write_file()
read_file()

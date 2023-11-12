import json
import os


def available_dir():
    available_directories = [
        name.replace(
            ".json",
            "") for name in os.listdir(".") if ".json" in name]
    available_directories = ", ".join(available_directories)
    return available_directories


def select_dir(dir_name=None):
    while dir_name != available_dir():
        dir_name = input(
            f"Enter dir name (available name: {available_dir()}):")
        if dir_name != available_dir():
            print("There is no such directory.")
            continue
    else:
        print(f"Checked: {dir_name}")
        return user_select(dir_name)


def add_new_entries(args, first_name, last_name, number, city_or_state):
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": f"{first_name} {last_name}",
        "number": str(number),
        "city_or_state": city_or_state}
    try:
        with open(f"{args}.json", "r+") as jfile:
            data = json.load(jfile)
            data.append(user)
            jfile.seek(0)
            json.dump(data, jfile)
            print("Data added successfully")
    except json.JSONDecodeError:
        with open(f"{args}.json", "w") as jfile:
            data = []
            data.append(user)
            jfile.seek(0)
            json.dump(data, jfile)
            print("Data added successfully")


def search(args, search_data):
    list_result = []
    try:
        with open(f"{args}.json") as jfile:
            name = json.load(jfile)
            for index_list, i in enumerate(name, -1):
                index_list += 1
                for key, value in i.items():
                    if value == search_data:
                        list_result.append(name[index_list])
            for i in list_result:
                for key, val in i.items():
                    print(f"{key} {val}")
                else:
                    print("*" * 20)
    except json.JSONDecodeError:
        return print("File empty")


def delete_telephone_number(args, del_num=None):
    try:
        with open(f"{args}.json", "r") as jfile:
            data = json.load(jfile)
            for index_list, i in enumerate(data, -1):
                index_list += 1
                for key, value in i.items():
                    if value == del_num:
                        data.remove(data[index_list])
        with open(f"{args}.json", "w") as jfile:
            jfile.seek(0)
            json.dump(data, jfile)
            print(f"Delete number {del_num} successfully")
    except json.JSONDecodeError:
        print("File empty")


def update_telephone_number(args, update_num=None, select=None):
    try:
        with open(f"{args}.json", "r") as jfile:
            data = json.load(jfile)
        update_dict = {}
        for index_list, i in enumerate(data, -1):
            index_list += 1
            for key, value in i.items():
                if value == update_num:
                    pass
                    update_dict.update(data[index_list])
        print(update_dict)
        if select == 1:
            update_dict["first_name"] = input("Enter first name: ").lower()
            update_dict["full_name"] = f'{update_dict["first_name"]} {update_dict["last_name"]}'
            print(update_dict)
        elif select == 2:
            update_dict["last_name"] = input("Enter last name: ").lower()
            update_dict["full_name"] = f'{update_dict["first_name"]} {update_dict["last_name"]}'
            print(update_dict)
        elif select == 3:
            update_dict["first_name"] = input("Enter first name: ").lower()
            update_dict["last_name"] = input("Enter first name: ").lower()
            update_dict["full_name"] = f'{update_dict["first_name"]} {update_dict["last_name"]}'
            print(update_dict)
        elif select == 4:
            update_dict["number"] = input("Enter number: ")
            print(update_dict)
        else:
            update_dict["city_or_state"] = input(
                "Enter city or state: ").lower()
            print(update_dict)
        data[index_list] = update_dict
        with open(f"{args}.json", "w") as jfile:
            jfile.seek(0)
            json.dump(data, jfile)
            print(f"Update successfully")
    except json.JSONDecodeError:
        print("File empty")


def user_select(dir_name, args=None):
    args = int(input('''
        Enter the number:
        1-Add new entries
        2-Search by first name, last name, full name, phone number, city or state
        3-Delete a record for a given telephone number
        4-Update a record for a given telephone number
        5-Exit the program
        '''))
    if args == 1:
        return add_new_entries(
            dir_name,
            first_name=input("Enter first name:").lower(),
            last_name=input("Enter last name: ").lower(),
            number=int(
                input("Enter number: ")),
            city_or_state=input("Enter city or state: ").lower())
    elif args == 2:
        search(dir_name, search_data=input(
            """Enter what you want to find: first name, last name, full name, phone number, city or state (For example: Maxim). :\n""").lower())
    elif args == 3:
        delete_telephone_number(dir_name, del_num=input("Enter del num: "))
    elif args == 4:
        update_telephone_number(
            dir_name,
            update_num=input("Enter num update: "),
            select=int(
                input("""Select what exactly you want to change (update)?
            1-first_name
            2-last_name
            3-full_name
            4-number
            5-city or state\n""")))
    else:
        exit()


print("*" * 25, "Welcome to the telephone directory", "*" * 25)
select_dir()

number = "0955555555"
if number.isdigit() and len(number) <= 10:
    print("Ok")
elif number.isdigit():
    print("Maximum number length 10 digits")
elif len(number) <= 10:
    print("The number must contain digits only")
else:
    print("The number must contain only digits and the maximum length of the number is 10 digits")

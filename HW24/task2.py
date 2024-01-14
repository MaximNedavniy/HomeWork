class Stack:
    def __init__(self, *args):
        self.__stack = list(args)

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        if self.__stack:
            return self.__stack.pop()

    def __len__(self):
        return len(self.__stack)

    def get(self):
        if self.__stack:
            return self.__stack[-1]

    def __repr__(self):
        return f"{self.__stack}"


open_brackets = ["(", "{"]
close_brackets = [")", "}"]
stack = Stack()
error = False
some_string = input("Enter your string: ")
for i in some_string:
    if i in open_brackets:
        stack.push(i)
    elif i in close_brackets:
        if not stack:
            error = True
            print("Error")
            break
        else:
            stack.pop()
if not error and stack:
    print("Error")
else:
    if not error:
        print("Ok")

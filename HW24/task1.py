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


some_string = input("Enter your string: ")
stack = Stack()
revers_string = ""
for i in some_string:
    stack.push(i)

while not len(stack) == 0:
    revers_string += str(stack.pop())

print(revers_string)

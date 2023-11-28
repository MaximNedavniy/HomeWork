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

    def get_from_stack(self, args):
        return self.__stack.pop(self.__stack.index(args))


class Queue:
    def __init__(self, *args):
        self.__queue = list(args)

    def push(self, element):
        self.__queue.insert(0, element)
        print(self.__queue)

    def pop(self):
        if self.__queue:
            return self.__queue.pop()

    def get(self):
        if self.__queue:
            return self.__queue[-1]

    def __repr__(self):
        return f"{self.__queue}"

    def get_from_stack(self, args):
        return self.__queue.pop(self.__queue.index(args))


stack = Stack(1, 2, 3)
queue = Queue(1, 2, 3)
print(stack)
stack.get_from_stack(2)
print(stack)
print(queue)
queue.get_from_stack(2)
print(queue)

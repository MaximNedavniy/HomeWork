
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node(value={self.data}, next={self.next})"


class QueueLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.head.next = new_node
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack empty")
            return
        popped_data = self.tail.data
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            current_node = self.tail
            self.tail = self.tail.next
        return popped_data

    def get(self):
        return self.tail.data


    def __str__(self):
        current_node = self.tail
        list_repr = ""
        while current_node:
            list_repr += (str(current_node.data) + ",")
            current_node = current_node.next
        return "[" + list_repr + "]"


queueList = QueueLinkedList()
queueList.pop()
print(queueList)


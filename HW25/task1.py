class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next

    def __repr__(self):
        return str(self._data)


class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def append(self, item):
        temp = Node(item)
        if self._head is None:
            self._head = temp
        else:
            current = self._head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(temp)

    def __getitem__(self, item):
            current = self._head
            i = 0
            while i != item:
                current = current.get_next()
                i += 1
            return current.get_data()

    def pop(self):
        if self._head is None:
            print("Empty")
            return
        if not self._head.get_next():
            pop_data = self._head._data
            self._head = None
        else:
            current_node = self._head
            while current_node.get_next()._next is not None:
                current_node = current_node.get_next()
            pop_data = current_node.get_next()._data
            current_node.set_next(None)
        return pop_data

    def insert(self, index, data):
        temp=Node(data)
        if index == 0:
            temp.set_next(self._head)
            self._head=temp
        else:
            current = self._head
            i = 0
            while i != index-1:
                i += 1
                current = current.get_next()
            temp.set_next(current.get_next())
            current.set_next(temp)

    def __len__(self):
        if self._head is None:
            return 0
        else:
            count=1
            current_node=self._head
            while current_node.get_next() is not None:
                current_node=current_node.get_next()
                count+=1
            return count
    def slice(self, start, stop):
        current_node = self._head
        result=[]
        if self._head is None:
            return print("List empty")
        if start or stop > len(self):
            raise ValueError("Out of Range")
        i = 0
        while i < start:
            current_node = current_node.get_next()
            i += 1
        while i < stop:
            result.append(current_node)
            current_node = current_node.get_next()
            i += 1
        return result




if __name__ == "__main__":
    my_list = UnsortedList()
    my_list.add(10)
    my_list.add(200)
    my_list.add(40)
    my_list.add(30)
    my_list.add(20)
    my_list.add(100)
    print(my_list)
    my_list.pop()
    print(my_list)



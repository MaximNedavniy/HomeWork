class MyIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.my_list):
            val = self.my_list[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

    def __getitem__(self, item):
        if item >= 0 and item < len(self.my_list):
            return self.my_list[item]
        else:
            raise IndexError('Index out of range')


my_list = [1, 2, 3, 4, 5]
my_iter = MyIterator(my_list)

for item in my_iter:
    print(item)

print(my_iter[1])

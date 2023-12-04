class Mathematician:
    def square_nums(self, args: list) -> list:
        return [i**2 for i in args]

    def remove_positives(self, args: list) -> list:
        return [i for i in args if i < 0]

    def filter_leaps(self, args: list) -> list:
        return [i for i in args if i % 4 == 0]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

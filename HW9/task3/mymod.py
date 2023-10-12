def count_lines(name):
    with open(name, "r") as f:

        return len(f.readlines())
def count_chars(name):
    with open(name, "r") as f:
        f.seek(0)
        return len(f.read())
def test(name):
    return count_lines(name), count_chars(name)


# print(count_lines("text.txt"))
# print(count_chars("text.txt"))
# print(test("text.txt"))
#print(test("mymod.py"))
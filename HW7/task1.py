some_string=input("Enter some sentence:")
some_list=some_string.split()
some_dict={i:some_list.count(i) for i in some_list}
print(some_dict)

import random
some_list = []
some_list_2=[]
count=0
while count<100:
    count+=1
    some_list.append(count)
    if count % 7 == 0 and count % 5 != 0:
        some_list_2.append(count)
print(some_list_2)

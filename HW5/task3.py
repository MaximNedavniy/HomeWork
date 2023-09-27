import random
some_string=input("Enter a string:")
out_list=[]
for n in range(5):
  out_list.clear()
  for i in some_string:
    out_list.append(i)
  random.shuffle(out_list)
  print("".join(out_list))

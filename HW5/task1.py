import random
computer=random.randint(1, 10)
user=input("Enter a number:")
if int(user)==computer:
    print(f"You guessed the number-{computer}")
else:
    print(f"You didn't guess. The correct number is {computer}")

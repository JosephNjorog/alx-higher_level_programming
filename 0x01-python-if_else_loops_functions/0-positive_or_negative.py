#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"{number} is ", end="")
if number < 0:
    print("negative")
elif number > 0:
    print("positive")
else:
    print("zero")

from functools import reduce

first = input("")
second = input("")
third = input("")


print(str(int(first) + reduce(lambda a,b: int(a)+int(b), second.split())), third)

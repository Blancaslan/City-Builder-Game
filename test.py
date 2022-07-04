one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
num_list = [one, two, three, four, five, six]
print(num_list.index(six) / 5)
if isinstance(num_list.index(six) / 5, int):
    print("is instance")
else:
    print("not instance")

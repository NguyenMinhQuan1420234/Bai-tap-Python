import numbers

x = [int(x) for x in input("Enter multiple values: \n").split()]

print("Numbers of list is: ", x)

max = max(x)
min = min(x)

print("Max =", max)
print("Min =", min)
x = [str(x).strip() for x in input("List of animals: ").split(",")]

print("Number of list is: ", x) 
print("Numbers of animal: ",len(x))

tim = input("I want to find: \n")

for char in x:
    if char == tim:
        print(f"there is {tim} in list of animals")
        break
else:
    print(f"there is no {tim} in list of animals")

if tim in x:
    print(f"there is {tim} in list of animals")
else:
    print(f"there is no {tim} in list of animals")    
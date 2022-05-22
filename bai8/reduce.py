from functools import reduce

def do_sum(x1,x2):
    print("x1 = ",x1 , "x2 = ",x2)
    return x1 + x2

print(reduce(do_sum, [1,5,3,4]))
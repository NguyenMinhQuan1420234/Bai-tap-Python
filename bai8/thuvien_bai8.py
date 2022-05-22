from re import S


def tinh_S(n,x):
    s = 0
    if n == 0:
        s = 1
    else:
        s = pow((x*x+1),n)
    return s

def tinh_A(n,x):
    A = pow(pow(x, 2) + x + 1, n) + pow(pow(x,2) - x + 1 ,n)
    return A

def kiem_tra_so_NT(x):
    count = 0
    for i in range(1, x+1):
        if x%i == 0:
            count = count+1
    if count == 2:
        return True
    else:
        return False
    
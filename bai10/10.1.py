import math

def tinhGTBT(x, y):
    try:
        A = math.sqrt((5*x - y)/(2*x + 7*y))
        print(A)
    except:
        A = None
        print("An error has occurred... can't devide zero!" + " A =",A)
    return A

x = float(input("Nhập x: "))
y = float(input("Nhập y: "))

tinhGTBT(x,y)
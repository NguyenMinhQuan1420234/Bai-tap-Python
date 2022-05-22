def Congthuc_S1(x,n):
    A = x*x + 1
    S = pow(A,n)
    return S

def Congthuc_S2(x,n):
    A = x*x + x +1
    B = x*x - x +1
    S = pow(A,n) + pow(B,n)
    return S

def IsPrime(n):
    if n <=1 :
        print("%d khong phai la so nguyen to" %(n))
    else:
        b = True
        for i in range(2,n+1,1):
            if n%i != 0:
                pass
            else:
                break
        if n==i:
            print("%d la so nguyen to" %(n))
            return True
        else:
            print("%d khong phai so nguyen to" %(n))
            return False
    
x = int(input("Nhap so nguyen: "))
n = int(input("Nhap so nguyen: "))
print(Congthuc_S1(x,n))
print(Congthuc_S2(x,n))
IsPrime(x)

# kiem tra so nguyen to
n = int(input("nhap so n: \n"))
x = True

for i in range(2,n,1):
    if n % i == 0:
        print("%d khong phai so nguyen to" %(n))
        x = False
        break
    elif n == 2:
        print("%d la so nguyen to" %(n))
if x == True:
    print("%d la so nguyen to" %(n))

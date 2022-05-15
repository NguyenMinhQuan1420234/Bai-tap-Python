# kiem tra so nguyen to
n = int(input("nhap so n: \n"))

if n <=1 :
    print("%d khong phai la so nguyen to" %(n))
else:
    b = True
    for i in range(2,n,1):
        if n % i == 0:
            print("%d khong phai so nguyen to" %(n))
            b = False
            break
        elif n == 2:
            print("%d la so nguyen to" %(n))
    if b == True:
        print("%d la so nguyen to" %(n))

# if n<=1:
#     print("khong la so nguyen to")
# else:
#     j=2
#     while n%j !=0:
#         j+=1

#     if j==n:
#         print("la so nguyen to")
#     else:
#         print("khong la so nguyen to")

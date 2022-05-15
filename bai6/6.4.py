# (x2 + x + 1)^n + (x2 - x + 1)^n
x , n = [int(x) for x in input("Nhap x va n: \n").split()]

A = x*x + x +1
B = x*x - x +1

S = pow(A,n) + pow(B,n)

print("S = (%d^2 + %d + 1)^%d + (%d^2 - %d + 1)^%d = %d" %(x,x,n,x,x,n,S))
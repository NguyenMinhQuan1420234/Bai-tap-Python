x , n = [int(x) for x in input("Nhap x va n : \n").split()]

A = x*x + 1
S = pow(A,n)

print("S = (%d^2 + 1)^%d = %d" %(x,n,S))
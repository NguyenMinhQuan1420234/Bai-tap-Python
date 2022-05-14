n = eval(input("nhap n: \n"))
x = eval(input("nhap x: \n"))
S = x*x + n + 1
L = x*x - n + 1
if n == 0 or n == 1 :
    S = S**n
    L = L**n
    A = S + L
else :
    for i in range(2,n+1):
        S = S*(x*x + n + 1)
        L = L*(x*x - n + 1)
        print(S,L)
        A = S + L

print("A = (%d*%d + %d + 1)^%d + (%d*%d - %d + 1)^%d = %d" %(x,x,x,n,x,x,x,n,A))
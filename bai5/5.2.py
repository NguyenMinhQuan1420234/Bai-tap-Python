n = eval(input("nhap n: \n"))
x = eval(input("nhap x: \n"))
S = 1
if n == 0 :
    S = 1
else :
    for i in range(1,n):
        S = S*(x*x+1)
        print(S)

print("S = (%d*%d+1)^%d = %d" %(x,x,n,S))
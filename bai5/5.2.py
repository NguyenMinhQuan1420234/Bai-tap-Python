n = eval(input("nhap n: \n"))
x = eval(input("nhap x: \n"))
S = (x*x+1)
if n == 0 or n ==1 :
    S = S**n
else :
    for i in range(2,n+1):
        S = S*(x*x+1)
        print(S)

print("S = (%d*%d+1)^%d = %d" %(x,x,n,S))
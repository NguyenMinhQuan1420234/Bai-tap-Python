a = float(input("nhap a = \n"))
b = float(input("nhap b = \n"))
c = float(input("nhap c = \n"))
d = float(input("nhap d = \n"))

max = 0

if a>b and a>c and a>d  :
    max = a
elif b>a and b>c and b>d:
    max = b
elif c>a and c>b and c>d:
    max = c
else :
    max = d 

print("MAX = ", max)

min = 0

if a<b and a<c and a<d  :
    min = a
elif b<a and b<c and b<d:
    min = b
elif c<a and c<b and c<d:
    min = c
else :
    min = d 

print("MIN = ", min)
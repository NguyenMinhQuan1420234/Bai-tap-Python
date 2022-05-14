a = float(input("nhap a = \n"))
b = float(input("nhap b = \n"))
c = float(input("nhap c = \n"))
d = float(input("nhap d = \n"))
# a, b, c , d = eval(input("nhap a b c d:"))
max = a

if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d 

print("MAX = ", max)

min = a

if  b < min :
    min = b
if c < min:
    min = c
if d < min:
    min = d

print("MIN = ", min)
from operator import length_hint


s1 = str(input("nhap chuoi s1: "))
s2 = str(input("nhap chuoi s2: "))
s3 = str(input("nhap chuoi s3: "))
index = int(input("nhap index: "))
a = len(s1)
s4 =""
x = index
for index in range (index,a):
 s4 = s4 + s1[index]
print(s4)

print(s2*2)

print("chuoi s4 = ", s1[x:])
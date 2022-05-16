thislist = []
x = True

while x == True:
    y = input("Tiep tuc nhap gia tri? 1: Co, 0: Khong. Answer: ")
    if y == '0':
        x = False
    elif y == '1':
        thislist.append(int(input("Nhap gia tri: ")))
        print(thislist)

find = int(input("Nhap so can tim trong list: "))
dem = 0
S = 0
for a in thislist:
    S = S + a
    if a == find:
        dem+=1
else:
    print(f"Tong cac gia tri trong list la: {S}")
    print(f"So can tim xuat hien {dem} lan")


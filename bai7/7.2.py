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
BiggerList = []
for a in thislist:
    S = S + a
    if a == find:
        dem+=1
    elif a > find:
        BiggerList.append(a)
else:
    print(f"Tong cac gia tri trong list la: {S}")
    print(f"So can tim xuat hien {dem} lan")
    if len(BiggerList) > 0:
        print(f"{find} khong lon hon tat ca cac so trong list")
        print(f"Cac so lon hon {find} trong list la: ",BiggerList)
    else:
        print(f"{find} lon hon tat ca cac so trong list")

    # print("so phan tu cua List lon hon find: ", len(BiggerList))

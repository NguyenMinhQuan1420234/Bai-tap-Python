thislist = []
x = True

while x == True:
    y = input("Tiep tuc nhap gia tri? 1: Co, 0: Khong. Answer: ")
    if y == '0':
        x = False
    elif y == '1':
        thislist.append(int(input("Nhap gia tri: ")))
        print(thislist)

MangSoNT = []
MangDuong = []
MangAm = []
for a in thislist:
    if a >= 0:
        MangDuong.append(a)
    else:
        MangAm.append(a)
    for i in range(2,a+1,1):
        if a%i != 0:
            pass
        else:
            break
    if a==i:
        MangSoNT.append(a)
print("Cac so nguyen to trong List la: ", MangSoNT)
print("Cac phan tu am cua List: ",MangAm)
print("Cac phan tu duong cua List: ",MangDuong)


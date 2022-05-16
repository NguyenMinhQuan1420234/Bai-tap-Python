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
check = 0
for a in thislist:
    if a < 0:
        MangAm.append(a)
    elif a > 0:
        MangDuong.append(a)
        for i in range(2,a+1,1):
            if a % i != 0:
                pass
            else:
                break
            check = i
        if a == check or a == 2:
            MangSoNT.append(a)
        
print("Cac so nguyen to trong List la: ", MangSoNT)
print("Cac phan tu am cua List: ",MangAm)
print("Cac phan tu duong cua List: ",MangDuong)

tbc = 0
for a in MangDuong:
    tbc += a
if len(MangDuong) > 0 :
    print("Trung binh cong cac phan tu duong la: ", tbc/len(MangDuong))
tbc = 0
for a in MangAm:
    tbc += a
if len(MangAm) > 0 :
    print("Trung binh cong cac phan tu am la: ", tbc/len(MangAm))

print("List sap tang dan: ", sorted(thislist))
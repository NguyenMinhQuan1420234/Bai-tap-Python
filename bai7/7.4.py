BienTuple = ("red", "green", "yellow", "blue", "black", "white", "pink", "orange" ,"red", "blue")
print(BienTuple)
IndexDuong = eval(input("Nhap so tu 0 den 9: "))
IndexAm = eval(input("Nhap so tu -1 den -9: "))
s_find = input("Nhap chuoi can tim: ")
print(f"BienTuple[{IndexDuong}] = ",BienTuple[IndexDuong])
print(f"BienTuple[{IndexAm}] = ",BienTuple[IndexAm])
dem = 0
for i in BienTuple:
    if s_find == i:
        dem += 1
print(f"{s_find} xuat hien {dem} lan trong tuple")
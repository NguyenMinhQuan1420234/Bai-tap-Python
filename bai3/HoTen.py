HoTen = input("Nhap Ho va Ten: ")
HoTen = HoTen.strip()
print(HoTen)
vt1 = HoTen.find(" ")
vt2 = HoTen.rfind(" ")

print("Ho la :", HoTen[:vt1])
print("Ten la :", HoTen[vt2:])
print("Ten dem la :", HoTen[vt1:vt2])

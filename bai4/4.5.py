LoaiPhong = eval(input("Nhap loai phong (tu 1 den 8) : \n"))
SoDem = eval(input("Nhap so dem : \n"))

if LoaiPhong == 1:
        if SoDem == 1:
            ThanhTien = SoDem*1260000
        elif SoDem >= 2 and SoDem <= 3:
            ThanhTien = SoDem*1260000*(75/100)
        else :
            ThanhTien = SoDem*1260000*(70/100)
elif LoaiPhong == 2:
        if SoDem == 1:
            ThanhTien = SoDem*1550000
        elif SoDem >= 2 and SoDem <= 3:
            ThanhTien = SoDem*1550000*(75/100)
        else :
            ThanhTien = SoDem*1550000*(70/100)
elif LoaiPhong == 3 or LoaiPhong == 4:
        if SoDem == 1:
            ThanhTien = SoDem*1830000
        elif SoDem >= 2 and SoDem <= 3:
            ThanhTien = SoDem*1830000*(75/100)
        else :
            ThanhTien = SoDem*1830000*(70/100)
elif LoaiPhong == 5 or LoaiPhong == 6:
        if SoDem == 1:
            ThanhTien = SoDem*2120000
        elif SoDem >= 2 and SoDem <= 3:
            ThanhTien = SoDem*2120000*(75/100)
        else :
            ThanhTien = SoDem*2120000*(70/100)
elif LoaiPhong == 7:
        if SoDem == 1:
            ThanhTien = SoDem*2540000
        elif SoDem >= 2 and SoDem <= 3:
            ThanhTien = SoDem*2540000*(75/100)
        else :
            ThanhTien = SoDem*2540000*(70/100)
elif LoaiPhong == 8:
        if SoDem == 1:
            ThanhTien = SoDem*4800000
        elif SoDem >= 2 and SoDem <= 3:
            ThanhTien = SoDem*4800000*(75/100)
        else :
            ThanhTien = SoDem*4800000*(70/100)
else :
    print("There's such no room type")

print("Thanh Tien = ",ThanhTien)

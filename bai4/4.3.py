Kind = eval(input("Nhap loai xe 4 hay 7 cho~ : \n"))
Km = eval(input("Nhap so km di chuyen : \n"))
Wait = eval(input("Nhap so phut cho : \n"))

TienCho = 0
TienDiChuyen = 0
TienCuoc = 0

if Wait <= 5 :
    TienCho = 0
else :
    TienCho = (Wait - 5) * 750


if Kind == 4:
    if Km <=0.8:
        TienDiChuyen = 11000
    elif Km <= 30 :
        TienDiChuyen =  (Km - 0.8) * 15300 + 11000
    elif :
        TienDiChuyen = (30 - 0.8) * 15300 + (Km - 30) * 12100 + 11000
elif Kind == 7:
    if Km <=0.8 :
        TienDiChuyen == 12000
    elif Km <=30 :
        TienDiChuyen = (Km - 0.8) * 16100 + 12000 
    elif :
        TienDiChuyen = (30-0.8) * 16100 + (Km - 30) * 12100 + 12000 

print("Tien cho = ", TienCho)
print("Tien di chuyen = ", TienDiChuyen)
TienCuoc = TienCho + TienDiChuyen
print("Tien cuoc = ", TienCuoc)

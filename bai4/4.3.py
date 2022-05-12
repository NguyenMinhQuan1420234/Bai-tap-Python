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
if Kind == 4 and Km <= 30 :
    TienDiChuyen =  Km * 15300
elif Kind == 4 :
    TienDiChuyen = 30 * 15300 + (Km - 30) * 12100
elif Kind == 7 and Km <=30 :
    TienDiChuyen = Km * 16100
elif Kind == 7:
    TienDiChuyen = 30 * 16100 + (Km - 30) * 12100

print("Tien cho = ", TienCho)
print("Tien di chuyen = ", TienDiChuyen)
TienCuoc = TienCho + TienDiChuyen
print("Tien cuoc = ", TienCuoc)

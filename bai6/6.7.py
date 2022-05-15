import datetime

# x = datetime.datetime.now()

# print(x)
# print(x.year)
# print(x.strftime("%A"))

ngay = int(input("Nhap ngay: \n"))
thang = int(input("Nhap thang: \n"))
nam = int(input("Nhap nam: \n"))

x = datetime.datetime(nam,thang,ngay)
# in ngay thang nam
print(x)

# in thu cua ngay do

print(x.strftime("thu cua x la : %A"))
# x.strptime() chuyen chuoi nhap vao thanh ngay thang nam datetime

# Kiem tra nam nhuan
NamNhuan = False
if nam % 4 == 0:
    print(f"Nam {nam} la nam nhuan")
    NamNhuan = True
else:
    print(f"Nam {nam} khong phai la nam nhuan")

# Kiem tra so ngay trong thang



Thang30 = [1,3,5,7,8,10,12]
Thang31 = [4,6,9,11]
for i in Thang30:
    if thang == i:
        print(f"thang {thang} co 30 ngay")
        break
    elif NamNhuan == True and thang == 2:
        DayOfMonth = 29
        print(f"thang {thang} co 29 ngay")
        break
    elif NamNhuan == False and thang == 2:
        DayOfMonth = 28
        print(f"thang {thang} co 28 ngay")
        break
    else:
        print(f"thang {thang} co 31 ngay")
        break
    
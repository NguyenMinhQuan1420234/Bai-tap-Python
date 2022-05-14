n = int(input("nhap so nguyen n: \n"))
TongSoLe = 0
TongSoChan = 0
TichSo = 1
TichSoChia3 = 1
TongSoNguyenTo = 0

for i in range(1,n+1):
    if i % 2 ==  0:
        TongSoChan = TongSoChan + i
    else:
        TongSoLe = TongSoLe + i
    if n % 3 == 0:
        TichSoChia3 = TichSoChia3 * i
    TichSo = TichSo * i
    if i >= 2:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            TongSoNguyenTo = TongSoNguyenTo + i

print("Tong cac So le nho hon bang n: ", TongSoLe)
print("Tong cac So chan nho hon bang n: ", TongSoChan)
print("Tich cac so tu 1 den n: ", TichSo)
print("Tich cac so chia het cho 3 tu 1 den n: ", TichSoChia3)
print("Tong cac so nguyen to nho hon bang n: ", TongSoNguyenTo)
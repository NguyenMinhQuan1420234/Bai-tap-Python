import xu_ly_tap_tin as tv

tenfile = input("Ten tap tin: ")
print("Noi dung tap tin csv: ")
tv.read_file_csv(tenfile)

# listContent = [["Johnny Chi Nguyen", '5456 5464'], ["Con ma","2134 5785"]]

listContent = []
spt = 2

for i in range(0,spt):
    list = []
    ten = input("Nhap ten: ")
    sdt = input("Nhap sdt: ")
    list.append(ten)
    list.append(sdt)
    listContent.append(list)


tv.write_csv_file(tenfile,listContent)
tv.read_file_csv(tenfile)
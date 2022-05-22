import xu_ly_tap_tin as tv

filename = input("Nhap ten tap tin: ")
file = tv.read_file(filename)

print("Noi dung tap tin: \n")
print(file)

tv.read_report_file_cach1(filename)
tv.read_report_file_cach2(filename)

# str =[str(x) for x in input("Nhap du lieu: ")]
# print(str)

# for x in str:s
#     file.write(x)
#     if x == '\n':
#         file.write('\n')

# file.seek(0)
# print(file.read())
# file.close()
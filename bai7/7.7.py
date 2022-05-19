from gettext import find


n = int(input("enter a n value: "))
d = {}

for i in range(n):
    keys = str(input()) 
    values = str(input()) 
    d[keys] = values
print(d)
search_name = input("Nhap ten can tim: ")
TimRa = False
# for key in d:
#     if search_name == key:
#         print(f"tim thay {search_name} va thong tin la: ",search_name, d.get(search_name))
#         TimRa = True
# if TimRa == False:
#     print(f"khong tim thay {search_name} ")  

if search_name in d:
    print(f"tim thay {search_name} va thong tin la: ",search_name, d.get(search_name))
else:
    print(f"khong tim thay {search_name} ")

Ten = str(input("Them ten vao danh ba: ")) 
sdt = str(input("Them sdt vao danh ba: ")) 
d.update({Ten:sdt})     
print(d)
print(len(d))

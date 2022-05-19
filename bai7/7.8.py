#Nhap tu dien 
# n = int(input("enter a n value: "))
# d = {}

# for i in range(n):
#     keys = str(input()) 
#     values = str(input()) 
#     d[keys] = values
# print("Dictionary: \n", d)

d = {"Tu Anh":"Nghia Viet","cat": "meo","dog":"cho","ant": "kien","bear":"gau"}
print("Dictionary: \n", d)

loops = True
while loops == True:
    Choice = int(input("Ban muon lam gi? 1: Xem tu dien; 2: Tra tu; 3: Them tu; 4: Xoa tu \n"))
    if Choice == 1:
        print("Dictionary:")
        for x in d:
            print(x,'\t',d.get(x))
        
    elif Choice == 2:
        Search_word = input("Nhap tu tieng Anh muon tim kiem: ")

        if Search_word in d:
            print(f"Tu {Search_word} co nghia la: ", d.get(Search_word))
        else:
            print("Khong co trong  tu dien!")
        
    elif Choice == 3:
        TiengAnh = input("Them tu tieng Anh vao tu dien: ")
        TiengViet = input("Them tu tieng Viet vao tu dien: ")
        d.update({TiengAnh:TiengViet})
        print("Tu dien da duoc cap nhat: \n", d)

    elif Choice == 4:
        XoaTu = d.pop(input("Nhap tu muon xoa khoi tu dien: ")) # lam dung thi XoaTu phai input rieng de khong sai pop trong d
        print("Tu dien da duoc cap nhat: \n")
        for key, value in d.items():
            print(key,'\t',value)
        
    LuaChon = int(input("Tiep tuc lua chon? 1: Co, 0: Khong \n"))
    if LuaChon == 0:
        print("Thoat chuong trinh ....")
        loops = False

# list1 =  ["1", "2", "3"]
# list2 = ["a","b","c"]
# newdict = dict.fromkeys(list1,list2)
# print(newdict)

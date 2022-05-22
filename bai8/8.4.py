def them_vao_list(list_original):
    Them = input("Nhap chuoi muon them vao: ")
    list_original.append(Them)
    return list_original

def tinh_tong_list(list_original):
    S = 0
    for x in list_original:
        fact = isinstance(x,float)
        S = S + x
    return S

def tim_dem_slxh(tuple_original, x):
    dem = 0
    if x in tuple_original:
        dem+=1
    return dem

def in_dictionary(dictionary):
    print("Dictionary:")
    for x in dictionary:
        print("(",x,':',dictionary.get(x),")",end =" ")
    print("\n")
def tim_kiem_dictionary(dictionary, key_search): 
    key_search = input("Nhap tu tieng Anh muon tim kiem: ")
    if key_search in dictionary:
        print(f"Tu {key_search} co nghia la: ", d.get(key_search))
    else:
        print(f"{key_search} khong co trong tu dien!")
def them_dictionary(dictionary, key_insert,value_insert):
    dictionary.update({key_insert:value_insert})
    print("Tu dien da duoc cap nhat: \n", dictionary)

d = {"Tu Anh":"Nghia Viet","cat": "meo","dog":"cho","ant": "kien","bear":"gau"}
Tuple1 = ("apple","banana","orange")
List1 = ["apple","banana","orange"]
List2 = [5.5, 6, 8]
# them_vao_list(List1)
print(List1)
S = tinh_tong_list(List2)
print("Tổng trong các số trong List2 = ",S)
Chuoi = input("Nhap chuoi muon tim trong Tuple1: ")
dem = tim_dem_slxh(Tuple1,Chuoi)
print("So lan x xuat hien la", dem)
in_dictionary(d)
tim_kiem_dictionary(d,Chuoi)
TiengAnh = input("Them tu tieng Anh vao tu dien: ")
TiengViet = input("Them tu tieng Viet vao tu dien: ")
them_dictionary(d,TiengAnh,TiengViet)
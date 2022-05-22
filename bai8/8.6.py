import thuvien_bai8 as tv2
from operator import add 
from functools import reduce

list_int = [3,5,-8,-15,2,11,-6]

tong = reduce(add, list_int)
print("Tong gia tri trong list: ", tong)

x = eval(input("Nhap gia tri can tim x: "))
list_cac_so_lonhon_x = filter(lambda item: x < item, list_int)
print("Cac so trong list > x la: ",list(list_cac_so_lonhon_x))

list_snto = filter(tv2.kiem_tra_so_NT,list_int)
print("List so nguyen to: ",list(list_snto))

list_am = filter(lambda x: x<0, list_int)
print("cac phan tu am: ", list(list_am))

list_duong = filter(lambda x: x>0, list_int)
print("cac phan tu duong: ", list(list_duong))
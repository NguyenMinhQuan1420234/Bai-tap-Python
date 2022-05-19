# set1 = set()
# x = True

# while x == True:
#     y = input("Tiep tuc nhap gia tri set1 ? 1: Co, 0: Khong. Answer: ")
#     if y == '0':
#         x = False
#     elif y == '1':
#         set1.add(int(input("Nhap gia tri: ")))
#         print(set1)

# set2 = set()
# x = True

# while x == True:
#     y = input("Tiep tuc nhap gia tri set2 ? 1: Co, 0: Khong. Answer: ")
#     if y == '0':
#         x = False
#     elif y == '1':
#         set2.add(int(input("Nhap gia tri: ")))
#         print(set2)

set1 = {5,6,7,0,2,1}
set2 = {2,2,1,5,7,9}

print("set1 co ", len(set1),"phan tu")
print("set2 co ", len(set2),"phan tu")

print("max cua set1 la: ",max(set1))
print("min cua set1 la: ",min(set1))
print("max cua set2 la: ",max(set2))
print("min cua set2 la: ",min(set2))

PhanTu = set1.pop()
print("Phan tu bi lay ra khoi set1 la: ", PhanTu)

set3 = set1.union(set2)
print("Set1 union voi set2 la: ",set3)

set4 = set1.intersection(set2)
print("Set1 intersection voi set2 la: ",set3)

set5 = set1.difference(set2)
print("Set1 difference voi set2 la: ",set4)

set6 = set1.symmetric_difference(set2)
print("Set1 symmetric_difference voi set2 la: ",set6)

set7 = sorted(set1)
set8 = sorted(set2, reverse=True)
print("set1 sau khi sort tang dan: ",set7)
print("set2 sau khi sort giam dan: ",set8)



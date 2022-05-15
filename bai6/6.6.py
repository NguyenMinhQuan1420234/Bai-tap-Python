import string

s = input("Nhap chuoi s: \n")
s_sub = input("Nhap chuoi s_sub: \n")
s_find = input("Nhap chuoi s_find: \n")
s_replace = input("Nhap chuoi s_replace: \n")

#loai bo khoang trang
s.strip()
print("Chuoi s sau khi loai bo khoang trang dau cuoi chuoi: ",s)

#in hoa ki tu dau chuoi
s1 = s.capitalize()
print(s1)

#so lan s_sub xuat hien trong chuoi s
dem = 0
for char in s:
    if char == s_sub:
        dem += 1
print(f"so lan s_sub xuat hien trong chuoi s la {dem}")   

#thay the phan tu trong chuoi

s1 = s1.replace(s_find,s_replace)
print(s1)
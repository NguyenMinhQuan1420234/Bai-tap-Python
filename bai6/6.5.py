import math
 
"""
# Giải phương trình bậc 2: ax2 + bx + c = 0
# @param a: hệ số bậc 2
# @param b: hệ số bậc 1
# @param c: số hạng tự do
"""
def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print ("Phương trình vô nghiệm!");
        else:
            print ("Phương trình có một nghiệm: x = ", + (-c / b));
        return;
 
    # tính delta
    delta = b * b - 4 * a * c;
    # tính nghiệm
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
    else: #delta < 0
        print("Phương trình vô nghiệm!");
 
# Nhập các hệ số
a = float(input("Nhập hệ số bậc 2, a = "));
b = float(input("Nhập hệ số bậc 1, b = "));
c = float(input("Nhập hằng số tự do, c = "));
# Gọi hàm giải phương trình bậc 2
giaiPTBac2(a, b, c)
# a , b , c = [float(a) for a in input("Nhap intput a b c: \n").split()]

# # xu ly a b c
# if a == 0:
#     if b == 0:
#         print("Phuong trinh vo nghiem")
#     else:
#         print("Phuong trinh bac nhat 1 nghiem x =", (-c/b)) 
    
# # xu ly delta

# delta = b*b - 2*a*c

# # xu ly nghiem x1 , x2

# if delta > 0 : #pt 2 nghiem
#     x1 = (float)((-b + math.sqrt(delta)) / (2 * a)) 
#     x2 = (float)((-b - math.sqrt(delta)) / (2 * a)) 
#     print("Nghiem cua phuong trinh la x1 = %.2f va x2 = %.2f" %(x1, x2))
# elif delta == 0 : # pt nghiem kep
#     x = -b/(2*a)
#     print("Phuong trinh co nghiem kep x1 = x2 = ",x)
# else:
#     print("Phuong trinh vo nghiem")

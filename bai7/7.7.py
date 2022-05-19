n = int(input("enter a n value: "))
d = {}

for i in range(n):
    keys = str(input()) 
    values = str(input()) 
    d[keys] = values

dk = 1
while dk ==1:
    choice = int(input("Ban muon lam gi? 1: Xem danh ba; 2: Tim kiem; 3: Them moi    -   "))
    if choice == 1:  
        for keys, values in d.items():
            print(f"{keys:5s}  --  {values:5s}")
        
        # for key in d:
        #     if search_name == key:
        #         print(f"tim thay {search_name} va thong tin la: ",search_name, d.get(search_name))
        #         TimRa = True
        # if TimRa == False:
        #     print(f"khong tim thay {search_name} ")  
    elif choice == 2:
        search_name = input("Nhap ten can tim: ")
        TimRa = False
        if search_name in d:
            print(f"tim thay {search_name} va thong tin la: ",search_name, d.get(search_name))
        else:
            print(f"khong tim thay {search_name} ")
    elif choice == 3:
        Ten = str(input("Them ten vao danh ba: ")) 
        if d.get(Ten) == None:
            sdt = str(input("Them sdt vao danh ba: ")) 
            d.update({Ten:sdt})     
            print("Danh ba update: \n", d)
            print(len(d))
        else:
            print("Da co ten trong danh ba!")
    dk = int(input("Tiep tuc lua chon? 1: co; 2: khong      -       "))


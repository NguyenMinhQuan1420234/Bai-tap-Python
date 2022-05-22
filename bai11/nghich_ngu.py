import os 

loop = True
file = open("test.txt","a+", encoding="utf-8")
while loop == True :
    x = input("Ban muon lam gi? 1: Nhap file, 2: Doc File, 3: Thoat, 4: xoa du lieu\t") 
    if x == '1':
        file.write(input("Viet them vo file: "))
        file.write('\n')
    elif x == '2':
        file.seek(0)
        nd = file.read()
        print(nd)
    elif x == '3':
        file.close()
        loop = False
    elif x == '4':
        file.truncate(0)
        

    
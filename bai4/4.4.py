SoDien = eval(input("Nhap so Kwh Tieu thu : \n"))

if SoDien <= 50 :
    SoDien*=1484
elif SoDien > 50 and SoDien <= 100 :
    SoDien = 50*1484 + (SoDien-50)*1533
elif SoDien > 100 and SoDien <= 200 :
    SoDien = 50*1484 + 50*1533 + (SoDien - 100)*1786
elif SoDien > 200 and SoDien <= 300 : 
    SoDien = 50*1484 + 50*1533 + 100*1786 + (SoDien - 200)*2242
elif SoDien > 300 & SoDien <= 400 :
    SoDien = 50*1484 + 50*1533 + 100*1786 + 100*2242 + (SoDien - 300)*2503
else :
    SoDien = SoDien = 50*1484 + 50*1533 + 100*1786 + 100*2242 + 100*2503 + (SoDien - 400)*2587

print("Tien dien phai tra: %.2f" %(SoDien))

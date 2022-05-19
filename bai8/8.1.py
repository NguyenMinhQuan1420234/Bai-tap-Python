def TinhCan(nam):
    # while nam > 0:
    Can = nam%10
    print(Can)
    if Can == 0:
        return "Canh"
    elif Can == 1:
        return "Tân"
    elif Can == 2:
        return "Nhâm"
    elif Can == 3:
        return "Quý"
    elif Can == 4:
        return "Giáp"
    elif Can == 5:
        return "Ất"
    elif Can == 6:
        return "Bính"
    elif Can == 7:
        return "Đinh"
    elif Can == 8:
        return "Mậu"
    else:
        return "Kỷ"    

def TinhChi(nam):
    # while nam > 0:
    Chi = nam%12
    print(Chi)
    if Chi == 0:
        return "Thân"
    elif Chi == 1:
        return "Dậu"
    elif Chi == 2:
        return "Tuất"
    elif Chi == 3:
        return "Hợi"
    elif Chi == 4:
        return "Tý"
    elif Chi == 5:
        return "Sửu"
    elif Chi == 6:
        return "Dần"
    elif Chi == 7:
        return "Mão"
    elif Chi == 8:
        return "Thìn"
    elif Chi == 9:
        return "Tỵ"
    elif Chi == 10:
        return "Ngọ"
    else:
        return "Mùi"    

nam = int(input("Nhap nam muon doi qua Am Lich: "))
Can = TinhCan(nam)
Chi = TinhChi(nam)
print(f"Năm {nam} âm lịch là năm {Can} {Chi}")
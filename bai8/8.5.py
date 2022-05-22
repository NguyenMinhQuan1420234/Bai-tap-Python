import  math

def TinhDThinhtron(r):
    s_tron = lambda r: math.pi * math.pow(r,2)
    return s_tron

def TinhDThcn(Chieudai,Chieurong):
    return lambda a,b : Chieudai*Chieurong


s_tron = TinhDThinhtron(5)
print(s_tron(5))

s_hcn = TinhDThcn(2,3)
print(s_hcn(2,3))
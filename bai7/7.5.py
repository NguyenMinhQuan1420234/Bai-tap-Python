TupleA = tuple(int(x) for x in input("nhap tuple a: ").split())
TupleB = tuple(int(x) for x in input("nhap tuple b: ").split())
print("a:",TupleA)
print("b:",TupleB)
TupleC = TupleA + TupleB
print("c:",TupleC)
TupleD = sorted(TupleC)
print("d: ",TupleD)
print("phan tu thu 3 cua d:", TupleD[2])
if len(TupleD) >= 3:
    print("3 phan tu cuoi cung cua d: ", TupleD[-1],TupleD[-2],TupleD[-3])
x = 10
y = 4
print('x = %d, y = %d'%(x,y))
equivelence = x==y #false
print('x==y is', equivelence)
equivelence = x!=y #true
print('x!=y is', equivelence)
equivelence = x>y #true
print('x>y is', equivelence)
x = 8
y = 9
print('x = %d, y = %d'%(x,y))
equivelence = x>=y #false
print('x>=y is', equivelence)
equivelence = x<y #true
print('x<y is', equivelence)
equivelence = x<=y #true
print('x<=y is', equivelence)
x = 15
y = 12
print('Binary of x =', bin(x), ', Binary of y =', bin(y)) # 1111 1100
print('x & y =', bin(x & y)) # 1100 12
print('x | y =', bin(x | y)) # 1111 15
print('x ^ y =', bin(x ^ y)) # 0011  3
print('~x =', bin(~x)) # 0000 0
print('x << 2 =', bin(x << 2)) # 111100
print('y >> 2 =', bin(y >> 2)) # 0011
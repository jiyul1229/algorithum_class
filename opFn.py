def opDn():
    print(5 / 3) #1.6666666667(소숫점 16개)
    print(5 // 3) #1
    print(5 % 3) #2
    print(5 % 3.0) #2.0
    print(5.2 % 3.0) #2.2
    print(5 ** 3) #125
    
    print(f'{type(range(5))}') #range
    print(f"{type('문자열')}") #str
    print(f'{type([1, 2, 3])}') #list
    print(f'{type((1, 2, 3))}') #tuple
    print(f'{type([1, 2, 3])}') #list
    
opDn()
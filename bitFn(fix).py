import math

def bitFn():
    a = 13
    b = 7
    
    print(bin(a)); print(bin(b))
    print(f'{a & b}')
    print(f'{a | b}')
    print(f'{a ^ b}')
    print(f'{~a}')
    print(f'{~b}')
    
    a = 0b01010101
    b = 0o123
    print(bin(b))
    
    print(f'{3e3}, {3.14E5}')
    
    c = math.inf
    
    print(c)
    
    print(0.3 + 0.5)
    
    # print(bin(0.3))
    # print(bin(0.6))
    #오류뜬다!!
    
    
bitFn()
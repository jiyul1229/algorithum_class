def maxFn():
    a = 3; b = 5
    if a > b:
        max = a
    else:
        max = b
    print(f'큰 값: {max}')
    
    a = 5; b = 7
    max = a if a > b else b
    print(f'큰 값: {max}')
    
maxFn()
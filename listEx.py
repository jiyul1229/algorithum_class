def listEc():
    a = list()
    b = []
    
    a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a2 = list(range(1, 10)) #실수는 numpy.arange()을 써야함. 
    a3 = [i for i in range(1, 10)]
    print(a1, a2, a3)
    
    a4 = [0] * 10
    a5 = [0 for _ in range(10)]
    print(a4, a5)
    
    a6 = [1, 2, 3, 4]
    a7 = a6[:-1] #맨 뒤에 하나 빼고 출력 [1, 2, 3]
    a8 = a6[::-1] #거꾸로 출력 [4, 3, 2, 1]
    print(a7, a8)
    
listEc()
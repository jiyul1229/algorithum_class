def twolist():
    r = 3; c = 4
    
    # l1 = [[0] * c] * r
    # print(l1)
    # # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 출력 의도한 바와 달라 오류 발생
    
    # l1[2][2] = 5
    # print(l1)
    
    l2 = [[0] * c for _ in range(r)]
    print(l2)
    l2[2][2] = 5
    print(l2)
    l2[1][3] = 7
    print(l2)
    
    l3 = [[0, 0, 0, 0]] * 3
    print(l3)
    l3[2][2] = 5
    print(l3)
    
    l4 = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
    
    print(l4)
    l4[2][2] = 5
    print(l4)
    
twolist()
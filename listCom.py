def listCom():
    a1 = [i for i in range(10)]
    print(a1)
    
    a2 = [i ** 2 for i in range(10)]
    print(a2)
    
    event_a = ['아반떼', '투싼', '넥쏘']
    event_b = ['흰색', '실버', '검정']
    a3 = [[x, y] for x in event_a for y in event_b]
    print(a3)
    a4 = [len(i) for i in event_a]
    print(a4)
    a5 = [i[0] for i in event_a]
    print(a5)
    
    a6 = [i for i in range(10) if i % 2 != 0]
    print(a6)
    
    a7 = [i if i % 2 != 0 else '짝수' for i in range(10)]
    print(a7)
    
listCom()
    
    
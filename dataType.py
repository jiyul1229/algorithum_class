def datatypeFn():
    iData = 3
    fData = 3.14
    cData = 3 + 4j
    
    print(f"iData type: {type(iData)}") #int
    print(f"fData type: {type(fData)}") #float
    print(f"cData type: {type(cData)}") #complex
    print("파이썬은 모든 데이터 타입을 개체처리합니다.")
    
    data1 = range(5)
    print(f'{type(data1)}') #range
    data2 = '문자열'
    print(f'{type(data2)}') #str
    data3 = [1, 2, 3]
    print(f'{type(data3)}') #list
    data4 = (1, 2, 3)
    print(f'{type(data4)}') #tuple
    data5 = {1, 2, 3}
    print(f'{type(data5)}') #set
    data6 = {'a':'apple', 'b':'bannana'}
    print(f'{type(data6)}') #dict
    data7 = True
    print(f'{type(data7)}') #bool
    
datatypeFn()
    
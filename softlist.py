def softlist():
    l1 = [1, 5, 9, 2, 7]
    l2 = l1.sort()
    print(l2)
    
    l1 = [1, 5, 9, 2, 7]
    l3 = sorted(l1)
    print(l3)
    
    a = [1, 2, 3]
    b = a
    b[2] = 100
    a[1] = 1000
    print(a, b)
    
    del a, b
    
    a = 3; b= a
    a= 1000
    print(a, b)
    
    a = [1, 2, 3, 4, 5, 5, 5]
    r_s = {3, 5}
    
    result = [i for i in a if i not in r_s]
    print(result)
    
    result.remove(1)
    print(result)
    
    r_v = 100
    if r_v in result:
        result.remove(r_v)
    else:
        pass
    print(result)
    
    try:
        result.remove(r_v)
    except Exception as e:
        print(f"에러 메시지: {e}")
        

if __name__ == "__main__":
    softlist()

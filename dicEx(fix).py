def dictEx():
    dict1 = {"사과":"apple", "바나나":"banana", "코코넛":"coconut"}
    
    print(dict1)
    
    for i in dict1:
        print(i)
        
    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())
    
    for i in dict1.values():
        print(i)
        
    for i in dict1.items():
        print(i)
        
    for i in dict1.keys():
        print(i, ":", dict1[i])
        
    dict1['사과'] = '미안'
    print(dict1)
    
if __name__ == "__main__":
    dictEx()
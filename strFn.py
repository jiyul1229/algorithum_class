def strFn():
    print("Test" * 3)
    print([0] * 5)
    print(["Test"])
    print(list("Test"))
    
    str1 = "ILoveYou"
    print(str1[2:5])
    
    print(id(str1))
    
if __name__ == "__main__":
    strFn()
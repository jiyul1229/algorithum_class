# def testFn(*args, **kwargs):  #keyword argument: **kwargs
#     print("test")
#     print(args, type(args))
#     print(kwargs, type(kwargs))
    
# def testFn(*args): #kwargs):  #keyword argument: **kwargs
#     print("test")
#     print(args, type(args))
#     #print(kwargs, type(kwargs))
    
    #파이썬 함수 값 넘기기
def testFn(aa, bb, *args, **kwargs):  #keyword argument: **kwargs
    print("test")
    print(aa, bb)
    print(args, type(args))
    print(kwargs, type(kwargs))
    
#public 외부로부터 모든 접근 허용, _: protected 자기자신과 자손까지 접근 허용, __: private 자기자신만 접근 허용    

import sys

def datareadFn():
    #debug
    # data = sys.stdin.readline().rstrip()
    # print(data)
    
    # # 중요
    # data1 = list(map(int, sys.stdin.readline().rstrip().split())) 
    # print(data1)
    
    #read(), readlinses(), open ~ close(), with open()
    
#별표! eval()함수: 문자열을 수식으로 만들어줌. 
    result = eval("3+4")
    print(result)
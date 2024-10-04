def EvenOddSum(TestString):
   print(TestString) 
   InputData = int(input("값 입력: "))
   EvenSum = 0; OddSum = 0
   EvenSum = sum(list(range(0, InputData + 1, 2)))
   OddSum = sum(list(range(1, InputData + 1, 2)))
   print(OddSum, EvenSum)
   
EvenOddSum("숫자 합계 계산")

# EvenOddSum() 함수를 호출할 때 매개변수인 TestString에 값을 전달하지 않으면, Python은 오류를 발생시킵니다. 이는 매개변수가 필수적이기 때문입니다. 아래에서 그 이유를 자세히 설명하겠습니다.

# 1. 매개변수의 필요성
# 필수 매개변수: 함수 정의에서 TestString은 매개변수로 정의되어 있습니다. 이 매개변수는 함수가 호출될 때 반드시 값을 받아야 합니다.
# 값의 전달: EvenOddSum("숫자 합계 계산")처럼 호출하면 문자열 "숫자 합계 계산"이 TestString에 전달됩니다.

def Dalist():
    DataList = [1, 2, 4, 6, 1, 2, 5, 7, 9]
    #C style
    EvenSum = 0; OddSum = 0
    for i in range(len(Datalist)):
        print(Datalist[i])
        if Datalist[i] % 2 == 0:
            EvenSum += Datalist[i]
        else:
            OddSum += Datalist[i]
    print("1: ", OddSum, EvenSum)
    
    #Python Style
    OddSum  = 0, EvenSum = 0
    for i in DataList:
        if i % 2 == 0:
            EvenSum += i
        else:
            OddSum += i
    print("2: ", OddSum, EvenSum)
    
    Datalist = [1, 1, 1, 1, 2, 2, 2, 2]
    Evensum = sum([i for i in Datalist if i % 2 == 0])    
    Oddsum = sum([i for i in Datalist if i % 2 != 0])
    print("3: ", OddSum, EvenSum)
    
    
    EvenSum = 0; OddSum = 0
    for i in range(InputData + 1):
        if i % 2 == 0:
            EvenSum += i
        else:
            OddSum += i
    print(OddSum, EvenSum)
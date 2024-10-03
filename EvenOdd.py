def SumEvenOdd():
    inputData = int(input("입력받은 값 입력: "))
    EvenSum = 0
    OddSum = 0
    
    EvenSum = sum(list(range(0, inputData + 1, 2)))
    OddSum = sum(list(range(1, inputData + 1, 2)))
    
    print(f"짝수의 합 = {EvenSum}, 홀수의 합 = {OddSum}")
    
SumEvenOdd()


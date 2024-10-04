def ifEx():
    a = 100
    
    if a > 10:
        print("크다")
    else:
        print("작다")
        
def listRemove():
    a = list(range(1, 6))
    for _ in range(3):
    #여기서 _를 쓴 이유는 정의를 할 필요가 없기 때문이다.
    #for _ in range(3):
    #    print("hello")를 하게되면 hello가 3번 출력된다.
        a.append(5)
        
    print(a)
    
    removeSet = {3, 5}
    
    result = [i for i in a if i not in removeSet]
    #for i in a: 리스트 a의 각 요소를 i라는 변수에 할당하면서 반복합니다.

# 첫 번째 반복: i = 1
# 두 번째 반복: i = 2
# 세 번째 반복: i = 3
# 네 번째 반복: i = 4
# 다섯 번째 반복: i = 5 (여기서 다섯 번 반복이 있지만, 5는 여러 번 존재합니다.)
# if i not in removeSet: i가 removeSet에 포함되지 않는 경우만 조건을 만족합니다.

# i = 1: 조건 만족, 1이 결과 리스트에 추가됩니다.
# i = 2: 조건 만족, 2가 결과 리스트에 추가됩니다.
# i = 3: 조건 불만족, 3은 결과 리스트에 추가되지 않습니다.
# i = 4: 조건 만족, 4가 결과 리스트에 추가됩니다.
# i = 5: 조건 불만족 (모든 5는 제거될 것), 5는 결과 리스트에 추가되지 않습니다.
# 결과 리스트 생성: 최종적으로 조건을 만족하는 요소만 포함된 새로운 리스트가 생성됩니다. 이 경우 result는 [1, 2, 4]가 됩니다.
  
    a = 150
    if 0 < a < 20:
        print("Success")
    else:
        print("Failure")
        
if __name__ == "__main__":
    listRemove()
# 초기 스택 리스트 생성
stk = [10, 20, 30]
print(f'기존값 : {stk}')

# 스택에 요소 추가 (push 연산)
stk.append(40)
print(f'추가값 : {stk}')

# 스택에서 요소 제거 (pop 연산)
topNum = stk.pop(-1)  # 가장 마지막 요소 제거 후 반환
# topNum = stk.pop()  # 위 코드와 동일한 동작

# 삭제된 요소 출력
print("topNum =%d" % topNum)
print("topNum =", topNum)

# 삭제 후 스택 상태 출력
print(f'40 삭제후 결과 : {stk}')

# 사용자 정의 스택을 위한 함수 정의
def push(item):
    """스택에 요소를 추가하는 함수"""
    global top
    stack.append(item)
    top += 1  # top 포인터 증가

def pop():
    """스택에서 요소를 제거하는 함수"""
    global top
    if top == -1:
        print("스택이 비어있습니다.")  # 스택이 비었을 경우 메시지 출력
    else:
        removed_item = stack.pop()  # 마지막 요소 제거
        top -= 1  # top 포인터 감소
        print(f"삭제된 값: {removed_item}")

# 사용자 정의 스택 리스트 및 top 포인터 초기화
stack = [] 
top = -1  # 스택이 비어있음을 의미

# 메인 실행 코드
if __name__ == "__main__": 
    while True:
        # 사용자 입력을 받아 동작 선택
        num = int(input("1:삽입, 2:삭제, 3:종료 => "))
        
        if num == 1:  # 삽입 연산 선택
            val = int(input("삽입할 데이터 => "))
            push(val)
            print("stack =", stack)
        
        elif num == 2:  # 삭제 연산 선택
            pop()
            print("stack =", stack)
        
        elif num == 3:  # 프로그램 종료 선택
            print("프로그램 종료")
            break
        
        else:  # 잘못된 입력 처리
            print("잘못된 입력입니다. 다시 입력하세요.")

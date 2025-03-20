
stk = [10, 20, 30]

print(f'기존값 : {stk}')
stk.append(40)
print(f'추가값 : {stk}')
topNum = stk.pop(-1)
#topNUm = stk.pop()
print("topNum =%d" % topNum)
print("topNum =", topNum)
print(f'40 삭제후 결과 : {stk}')

def push(item):
    global top
    stack.append(item)
    top += 1  # top = top + 1

def pop():
    global top
    if top == -1:
        print("스택이 비어있습니다.")
    else:
        removed_item = stack.pop()
        top -= 1
        print(f"삭제된 값: {removed_item}")

stack = [] 
top = -1

if __name__ == "__main__": 
    while True:
        num = int(input("1:삽입, 2:삭제, 3:종료 => "))
        if num == 1: 
            val = int(input("삽입할 데이터 => "))
            push(val)
            print("stack =", stack)
        elif num == 2:
            pop()
            print("stack =", stack)
        elif num == 3:
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
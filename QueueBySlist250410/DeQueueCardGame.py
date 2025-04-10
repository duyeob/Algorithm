from collections import deque

def card_game(n):
    if n > 500000:
        return

    myQueue = deque(range(1, n + 1))
    step = 1

    print(f"초기 카드 상태: {list(myQueue) if n <= 100 else '[생략됨]'}")

    while len(myQueue) > 1:
        removed = myQueue.popleft()
        moved = myQueue.popleft()
        myQueue.append(moved)

        if n <= 100:
            print(f"Step {step}: 버림={removed}, 이동={moved}, 현재 상태={list(myQueue)}")
        step += 1

    print(f"\n 마지막으로 남은 카드: {myQueue[0]}")

try:
    n = int(input("카드 개수 N을 입력하세요 (최대 500000): "))
    card_game(n)
except ValueError:
    print("유효한 숫자를 입력해주세요.")

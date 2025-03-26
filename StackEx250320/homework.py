def num11():
    n = int(input())
    target = [int(input()) for _ in range(n)]  

    stack = []
    result = []
    num = 1  # 변수 이름 변경

    for t in target:
        while num <= t:
            stack.append(num)
            result.append('+')
            num += 1

        if not stack or stack[-1] != t:
            print("NO")
            return

        stack.pop()
        result.append('-')

    for r in result:
        print(r)

num11()
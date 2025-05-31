def binSearch(nlist, skey):
    global count
    start = 0
    end = len(nlist) - 1

    while start <= end:
        count += 1
        mid = (start + end) // 2

        if skey == nlist[mid]:
            return mid
        elif skey > nlist[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1  # 못 찾았을 때


# 전역 변수
count = 0

# main 코드 부분
if __name__ == "__main__":
    num = []
    print("정수 10개를 입력하세요.")
    for i in range(10):
        su = int(input(f"{i + 1}번째 정수 입력: "))
        num.append(su)

    print("입력된 정수들 =", num)

    # 오름차순 정렬
    ascSort = sorted(num)
    print("오름차순 정렬 =", ascSort)

    # 내림차순 정렬
    descSort = sorted(num, reverse=True)
    print("내림차순 정렬 =", descSort)

    keyNum = int(input("탐색할 정수 입력: "))
    keyIndex = binSearch(ascSort, keyNum)  # 오름차순 기준으로 탐색

    if keyIndex != -1:
        print("검색된 키값의 index =", keyIndex)
        print("검색된 키값 =", ascSort[keyIndex])
    else:
        print("해당 값은 리스트에 없습니다.")

    print("비교 횟수 =", count)
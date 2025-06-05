class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

memory=[]
root=None
nameList=['블랙핑크', '아이브', '뉴진스', '레드벨벳', '트와이스', '소녀시대',]

#main 코드 영역#

# 이진탐색 트리 생성
if __name__=="__main__":
    node = TreeNode()
    node.data=nameList[0]
    root = node
    memory.append(node)


    for name in nameList[1: ]:
        node=TreeNode()
        node.data=name
        current = root

        while True:
            if name < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right

        memory.append(node)

    print("이진탐색트리 생성 완료")
    print("memory 리스트의 값들 출력")
    for node in memory:
        print(node.data, end=' ')
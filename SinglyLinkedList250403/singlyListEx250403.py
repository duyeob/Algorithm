class SList:
    class Node:
        def __init__(self, item , link):
            self.item = item
            self.next = link
    def __init__(self):
        print("나는 SList의 Constructor method")
        self.head = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0

    def insert_front(self , item):
        if self.isEmpty():
            self.head = self.Node(item , None)
        else :
            self.head = self.Node(item,
                                  self.head)
        self.size += 1

    def insert_after(self, item , p):
        p.next = self.Node(item, p.next)
        self.size += 1
    
    def find(self,target):
        p = self.head
        # k 0 , 1 , 2
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next 
    
    def remove_front(self):
        if self.isEmpty():
            print("삭제작업 불가")
            return None
        else:
            temp=self.head
            self.head = self.head.next
            del temp
            self.size -= 1
    
    def remove_after(self,p):
        if self.isEmpty():
            print("리스트가 텅비어서 삭제불가")
            return None
        else:
            temp = p.next
            p.next = temp.next
            del temp
            self.size -= 1

    #사용자가 원하는 인덱스에 새로운 노드 삽입하는 함수
    def insert_index(self,index,item):
        pass
    #사용자가 원하는 인덱스에 있는 노드를 삭제하는 함수
    def delete_index(self,index):
        pass
    #연결리스트의 맨 마지막 노드를 삭제하는 함수
    def delete_final(self):
        pass

    def showList(self):
        p = self.head
        while p:
            if p.next is not None:
                print(p.item , "=>" , end="")
            else:
                print(p.item)

            p = p.next    

if __name__ == "__main__":
    s = SList()
    s.insert_front("mango")
    s.insert_front("apple")
    s.showList()
    s.insert_after("cherry",s.head.next)
    s.showList()
    #index = s.find("cherry")
    #print("cherry는 %d번째 노드에 있음" % index)
    print("cherry는 %d번째 노드에 있음" % 
                (s.find("cherry")+1) )
    
    s.remove_front()
    print("첫번째 노드인 apple을 삭제후 = ")
    s.showList()
    s.insert_front("melon")
    s.remove_after(s.head)
    print("mango노드 삭제후")
    s.showList()

    #실습과제를 위해 추가된 코드
    s.insert_front('kiwi')
    s.insert_front('strawberry')
    s.insert_front('grape')
    s.insert_front('peach')
    s.insert_front('banana')

    s.insert_index(2,"pear")
    s.delete_index(3)
    s.delete_final()
    s.showList()
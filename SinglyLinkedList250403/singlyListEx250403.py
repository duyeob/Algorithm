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

class SList: # s 리스트 생성 하면서 노드 크래스 생성 노드 클ㄹ스가 slist 안에 들어가야댐 중첩 클래스:
    class Node:
        def __init__(self, item , link):  # node 클래스 멤버 함수
            self.item = item 
            self.next = link

    def __init__(self): # SList의 멤버 함수 # 생성자 counstrudct
            print("나는 SList의 Constructor method")
            self.head = None
            self.size = 0
    
    def isEmpty(self):
         return self.size == 0
    
    def insert_front(self, item): # 안에있느건 파라미터로 mango
         if self.isEmpty(): 
            self.head = self.Node(item, None)
         else:
              self.head = self.Node(item, 
                                    self.head)
         self.size += 1

    def insert_after(self,item,p):
         p.next = self.Node(item,p.next)
         self.size +=1
         

    def showList(self):
         p = self.head
         while p:
              if p.next is not None:
                   print(p.item,"=>", end=" ")
              else:
                   print(p.item)

              p = p.next

if __name__ == "__main__":
     s = SList() # self 100번지가 숨겨져 있음 셀프를 쓰면아댐
     s.insert_front("mango")
     s.insert_front("apple")
     s.showList()
     s.insert_after("cherry",s.head.next)
     s.showList()
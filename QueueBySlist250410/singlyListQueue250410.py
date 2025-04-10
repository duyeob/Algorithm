#큐
class LinkedQueue:
    class Node:
        def __init__(self,item,next):
            self.item = item
            self.next = next
    def __init__(self):
        self.front = None
        self.rear = None
        self.size=0

    def isEmpty(self):
        return self.size == 0

    def add(self,item):
        newnode = self.Node(item,None)
        if self.isEmpty():
            self.front = newnode
        else:
            self.rear.next = newnode

        self.rear = newnode
        self.size += 1 
    def showq(self):
        p=self.front
        print("front => " , end='')
        while p:
            if p.next != None:
                print("{!s:7<}".format(p.item),"->",
                      end="")
            else:
                print(p.item ,end="")
            p = p.next
        print(" <= rear") 
    
    def remove(self):
        if self.isEmpty():
            raise EmptyError("queue안에 아무것도 없음")
        else:
            fitem = self.front.item
            prefront = self.front
            self.front = self.front.next
            self.size -= 1
            del prefront
            if self.isEmpty():
                self.rear = None
            return fitem

class EmptyError(Exception):        
    pass

if __name__=="__main__":
    q = LinkedQueue() 
    q.add("apple") 
    q.add("orange")
    q.add("cherry")
    q.showq()
    removeitem = q.remove()
    print("front인 사과삭제후 removeitem = ",removeitem)
    q.showq()
     
    removeitem = q.remove()
    print("front인 오렌지삭제후 removeitem = ",removeitem)

    q.showq()
    q.add("grape")
    print("포도(grape) 추가후 = ")
    q.showq()
# 队列 & 双端队列

# 双端队列
class Deque:
    # 假设队尾在列表的 0 位置，即头在右边
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):   # 队首插入
        self.items.append(item)
    
    def addRear(self, item):    # 队尾插入
        self.items.insert(0, item)
        
    def removeFront(self):  # 队首删除
        return self.items.pop()
    
    def removeRear(self):   # 队尾删除
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
d=Deque()  
print(d.isEmpty())  
d.addRear(4)  
d.addRear('dog')  
d.addFront('cat')  
d.addFront(True)  
print(d.size())  
print(d.isEmpty())  
d.addRear(8.4)  
print(d.removeRear())  
print(d.removeFront()) 
print(d)
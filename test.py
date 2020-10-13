# 输入输出
# aName = input('please enter your name:')
# print("your name in all capitals is ", aName.upper(), "and has length", len(aName))

# 队首在右，队尾在列表的 0 位置
class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self, item):
        self.items.pop()
        
    def size(self):
        return len(self.items)

# q = Queue()
# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)
# print(q.size())

def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
    
# print(list_sum([1,2,3,4,5]))

print(ord(str(3)))



# test add 1
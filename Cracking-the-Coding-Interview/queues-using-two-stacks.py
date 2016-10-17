class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        while(len(self.first)>0):
            self.second.append(self.first.pop())
        return self.second[-1]
        
    def pop(self):
        while(len(self.first)>0):
            self.second.append(self.first.pop())
        return self.second.pop()
        
    def put(self, value):
        while (len(self.second)>0):
            self.first.append(self.second.pop())
        self.first.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = [int(i) for i in raw_input().split()]
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()

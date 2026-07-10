class MyStack:

    def __init__(self):
        self.li=[]
        self.count=-1

    def push(self, x: int) -> None:
        self.li.append(x)
        self.count+=1

    def pop(self) -> int:
        t= self.li.pop(self.count)
        self.count-=1
        return t

    def top(self) -> int:
        return self.li[self.count]
        

    def empty(self) -> bool:
        return self.count==-1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
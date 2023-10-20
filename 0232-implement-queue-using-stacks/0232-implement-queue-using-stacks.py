class MyQueue:

    def __init__(self):
        self.front=[]
        self.back=[]
        

    def push(self, x: int) -> None:
        self.back.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.front.pop()

    def peek(self) -> int:
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())

        return self.front[-1]

    def empty(self) -> bool:
        if self.front==[] and self.back==[]:
            return True
        return False
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
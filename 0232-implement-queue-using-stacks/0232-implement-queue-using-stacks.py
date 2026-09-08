
class MyQueue:

    def __init__(self):
        self.front: list[int] = []
        self.back: list[int] = []

    def push(self, x: int) -> None:
        self.front.append(x)

    def pop(self) -> int:
        if len(self.back) == 0:
            while len(self.front) != 0:
                self.back.append(self.front.pop())

        return self.back.pop()

    def peek(self) -> int:
        if len(self.back) == 0:
            while len(self.front) != 0:
                self.back.append(self.front.pop())

        return self.back[-1]


    def empty(self) -> bool:
        return (len(self.front) + len(self.back)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
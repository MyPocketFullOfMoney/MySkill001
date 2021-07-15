class CQueue:

    def __init__(self):

        self.stack_1 = []

        self.stack_2 = []


    def appendTail(self, value: int) -> None:

        self.stack_1.append(value)
        return self.stack_1


    def deleteHead(self) -> int:

        if self.stack_2:
            return self.stack_2.pop()

        if not self.stack_1:
            return -1
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()


obj = CQueue()

obj.appendTail(2)

obj.appendTail(5)

obj.deleteHead()

obj.deleteHead()
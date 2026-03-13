class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.pop())
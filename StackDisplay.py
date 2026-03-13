class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def display(self):
        # show top on the right
        return self.items


if __name__ == "__main__":
    s = Stack()
    s.push("A")
    s.push("B")
    print(s.display())
    print(s.pop())
    print(s.display())
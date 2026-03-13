class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = Node(value)
                    return
                cur = cur.left
            elif value > cur.value:
                if cur.right is None:
                    cur.right = Node(value)
                    return
                cur = cur.right
            else:
                return  # ignore duplicates

    def search(self, value):
        cur = self.root
        while cur is not None:
            if value == cur.value:
                return True
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    for v in [10, 5, 15, 3, 7]:
        bst.insert(v)
    print(bst.search(7))
    print(bst.search(99))
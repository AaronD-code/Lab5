class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def delete_value(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        prev = self.head
        cur = self.head.next
        while cur is not None:
            if cur.data == value:
                prev.next = cur.next
                return True
            prev = cur
            cur = cur.next

        return False

    def display(self):
        vals = []
        cur = self.head
        while cur is not None:
            vals.append(cur.data)
            cur = cur.next
        return vals


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)
    print(ll.display())
    ll.delete_value(20)
    print(ll.display())
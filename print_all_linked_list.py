class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

        def append(self,data):
            cur = self.head
            while cur.next is not None:
                cur = cur.next
                cur.next = Node(data)
                print(cur)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

linked_list = LinkedList(3)

linked_list.append(4)
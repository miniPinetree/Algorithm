#head
#[4]

def stack_push(self, value):
    new_head = Node(value) # new_head = Node(3)
    new_head.next = self.head  #[3] -> [4]
    self.head = new_head #현재 head의 값을 [3]으로 바꿔준다.
    return

def stack_pop(self):
    delete_head = self.head
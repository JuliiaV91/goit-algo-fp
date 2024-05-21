
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_list(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
           return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insertion_sort(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            
        self.head = None
        for data in arr:
            self.insert_at_end(data)

    def merge_2lists (self, list1, list2):
        dummy = Node ()
        tail = dummy

        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Друк реверсованого зв'язного списку
reversed_head = llist.reverse_list(llist.head)
llist.head = reversed_head

print("Реверсований зв'язний список:")
llist.print_list()

# Сортування списку вставками
llist.insertion_sort()

# Друк відсортованого зв'язного списку
print("Відсортований зв'язний список:")
llist.print_list()

# Злиття двох зв'язних списків
list1 = llist

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

merged_list = LinkedList()
result = merged_list.merge_2lists(list1.head, list2.head)
merged_list.head = result
print ("Результат злиття:")
merged_list.print_list()


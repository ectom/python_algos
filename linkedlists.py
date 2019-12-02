class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval:
            print(printval.val)
            printval = printval.next

    def add_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def first_val(self):
        return self.head.val

    def length(self):
        count = 0
        head = self.head
        while head:
            count += 1
            head = head.next
        return count

    def display_list(self):
        arr = []
        head = self.head
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def max(self):
        head = self.head
        maximum = head.val
        while head:
            if head.val > maximum:
                maximum = head.val
            head = head.next
        return maximum

    def min(self):
        head = self.head
        minimum = head.val
        while head:
            if head.val < minimum:
                minimum = head.val
            head = head.next
        return minimum

    def average(self):
        length = self.length()
        head = self.head
        total = 0
        while head:
            total += head.val
            head = head.next
        return total/length

    def last_val(self):
        head = self.head
        while head.next:
            head = head.next
        return head.val

    def remove_last(self):
        head = self.head
        while head.next.next:
            head = head.next
        head.next = None

    def add_last(self, val):
        head = self.head
        while head.next:
            head = head.next
        node = Node(val)
        head.next = node

    def min_to_front(self):
        prev = None
        after = None
        head = self.head
        smallest = head.val
        while head.next:
            if head.next.val < smallest:
                smallest = head.next.val
                prev = head
                if head.next.next:
                    after = head.next.next
                else:
                    after = None
            head = head.next
        prev.next = after
        front = Node(smallest)
        front.next = self.head
        self.head = front


# ---- Create Linked list ----
node_list = SLinkedList()
node_list.head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(0)
n9 = Node(9)
n10 = Node(10)
node_list.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
# node_list.add_front(0)
# ----------------------------

# node_list.listprint()
# print(node_list.first_val())
# print(node_list.length())
# print(node_list.display_list())
# print(node_list.max())
# print(node_list.min())
# print(node_list.average())
# print(node_list.last_val())
# node_list.remove_last()
# node_list.add_last(11)
# node_list.min_to_front()

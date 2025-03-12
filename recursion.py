def fibonacci(n):
    if n <= 0:
        return "invalid output"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last =  self.head
        while last.next:
            last.next = new_node

    def print_recursion(self, node):
        if node is None:
            return
        print(node.data)
        self.print_recursion(node.next)

    def start_recusrion_traversal(self):
        self.print_recusrion(self.head)

if __name__ == "__main__":
    linklist = LinkedList()

    linkslist.insert(10)
    linkslist.insert(20)
    linkslist.insert(30)
    linkslist.insert(40)

    print("Linked list")
    linklist.start_recursion_traversal()
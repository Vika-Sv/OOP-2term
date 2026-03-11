class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        return True

    def pop(self):
        if self.isEmpty():
            raise Exception("Стек порожній!")
        
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Стек (Top -> Bottom):", " -> ".join(elements) if elements else "Порожній")
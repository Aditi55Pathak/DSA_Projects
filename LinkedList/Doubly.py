class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_bookmark(self, url):
        new_node = Node(url)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_bookmark(self, url):
        current = self.head
        while current:
            if current.data == url:
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                break
            current = current.next

    def display_bookmarks(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Example usage
bookmarks = DoublyLinkedList()
bookmarks.add_bookmark("https://www.google.com")
bookmarks.add_bookmark("https://www.github.com")
bookmarks.add_bookmark("https://www.youtube.com")

print("Bookmarks:")
bookmarks.display_bookmarks()

print("\nRemoving https://www.github.com")
bookmarks.remove_bookmark("https://www.github.com")

print("\nUpdated Bookmarks:")
bookmarks.display_bookmarks()

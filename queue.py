# Fast af queue implementation O(n) size but whos counting

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue(object):
    """
    Lets try it with a linked list
    Still slow somehow my max_queue_size is way bigger than his?
    Changing the concatentation operator to self.length = self.length + 1 helped
    """
    def __init__(self):
        # The queue holds the head and the tail its the actual "List" of Nodes
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, item):
        temp = Node(item)
        if not self.head and not self.tail:
            self.head = self.tail = temp
            self.length = 1
            return
        else:
            self.tail.next = temp
            self.tail = temp
        self.length = self.length + 1

    def dequeue(self):
        if self.head is None:
            return None
        if self.tail is None:
            value = self.head.value
            self.head = None
            self.length = 0
            return value
        temp = self.head
        self.head = temp.next
        self.length = self.length - 1
        return temp.value

    def size(self):
        # somehow python is doing a better job of resizing this than i am
        return self.length

    def is_empty(self):
        # This is faster than self.head is None thanks python
        return not self.length

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue(object):
    """
    Use a linked list as the storage
    TODO figure out why size() is so much different
    between mine and len(self._items) as in the original
    Max queue size is Number of enqueues minus one... hmmm....
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
        self.length = self.length - 1
        temp = self.head
        self.head = temp.next
        return temp.value

    def size(self):
        # Python seems to do a better job resizing this
        return self.length

    def is_empty(self):
        # This is faster than self.head is None
        return not self.length

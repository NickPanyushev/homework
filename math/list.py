class Node:
    def __init__(self, data = None):
        self.data = data
        self.next_node = None
        self.next_node = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def get_prev(self):
        return self.prev_node
    def set_next(self):
        self.next_node = new_next
    def set_prev(self):
        self.prev_node = new_prev

class LinkedList:
    def __init__(self, head = None ):
        self.head = head
    def __Add__(self, elem):
        if self.head != None:
            new_node = Node(elem)
            new_node.set_next = head
            head.set_prev = new_node
            self.head = new_node
        else:
            new_node = Node(elem)
            self.head = new_node
           




    def __delete__(self, instance):
        song = "Song \"%s\" by  %s" % (self.name, self.artist)
        return song
    def __find__ (self, instance):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False
    def __add__ (self, other):
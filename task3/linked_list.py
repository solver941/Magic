class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
        self.length += 1

    def insert(self, data, index):
        index = self.check_index(index)


        if index == self.length:  # na konci
            self.append(data)
            return

        if index == self.length:
            self.append(data)
            self.head.prev_node = None
            node = Node()
            self.head = node
            self.length += 1
            return

        prev_node = self.get_node(index - 1)
        node = Node(prev_node, data, prev_node.next_node)
        prev_node.next_node.prev_node = node
        prev_node.next_node = node
        self.length += 1


    def check_index(self, index):
        if index < -self.length or index >= self.length:
            raise IndexError("Index out of range")
        if index < 0:
            index += self.length
        return index

    def get_node(self, index):
        current = self.head
        for i in range(index):
            current = current.next_node
        return current


    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return list(self)[index]
        """
        node = self.head
        for i in range(index):
            node = node.next_node
        return node"""

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return list(self)[index]

    def __setitem__(self, key, value):
        pass


    def __delitem__(self, index):
        index = self.check_index(index)
        node = self.get_node(index)
        prev = node.prev_node
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = prev
        del node
        self.length -= 1


    def __iter__(self):
        self.position = 0
        return self

    def __next__(self):
        if self.position < len(self.data):
            return_data = self.data[self.position]
            self.position += 1
            return return_data
        else:
            raise StopIteration





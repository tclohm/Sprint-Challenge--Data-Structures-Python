from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # head ==> [3] <== tail
        # head ==> [2], [3] <== tail
        # head ==> [1], [2], [3] <== tail
        if self.storage.length < self.capacity:
            # add the item to the head, current will hold tail, which is the oldest
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        elif self.current is self.storage.tail and self.capacity == self.storage.length:
            # because our tail is oldest, lets remove and replace
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            # move to our next oldest
            self.current = self.current.prev
        elif self.current is self.storage.head and self.capacity == self.storage.length:
            # if the head is our oldest, remove and replace
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            # loop back to tail, since it now the oldest
            self.current = self.storage.tail
        else:
            #                                   <========= flow ========
            # if we are in the middle ex; head [1], *[2], ==> [4] <=== [3] tail
            self.current.insert_after(item)
            self.current.delete()
            self.current = self.current.prev

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr = self.storage.head
        while curr != None:
            list_buffer_contents.append(curr.value)
            if curr.next == None:
                break
            curr = curr.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

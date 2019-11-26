"""module ringqueue
 Implements a ring queue (list wrapped into a ring).
 When ring size reaches max_ring_size new additions overwrite oldest:
  max_ring_size: the maximum size of the buffer -keep modest!
  size: integer up to max_ring_size, current size of the queue
  head_ptr:  points to head of list
  tail_ptr: point to tail of list
  queue_head_add(item): add item to head
  dequeue_tail(): remove item from head
  dequeue_head(): remove item from tail
  queue_inspect_head(): return copy of item at head without removal
  queue_inspect_tail(): return copy of item at tail without removal
  queue_inspect_item(n): return copy of item at position
  queue_list_size(): return length of list"""


class RingQueue:
    def __init__(self):
        self.max_ring_size = 4
        self.size = 0
        self.queue = list()
        self.head_ptr = -1  # if head and tail pointers = 0 then there is one item in list
        self.tail_ptr = 0  # head_ptr == -1 means the list is empty

    def queue_head_add(self, item):
        if self.size == self.head_ptr:  # first the list has to grow to its maximum size
            self.queue.append(item)
            self.size += 1
            self.head_ptr += 1
        else:  # after list hits maximum size it wraps and over writes itself
            self.head_ptr = (self.head_ptr + 1) % self.max_ring_size
            self.queue[self.head_ptr] = item
            if self.tail_ptr == self.head_ptr:  # if the tail has been overwritten then increment the tail_ptr
                self.tail_ptr = (self.tail_ptr + 1) % self.max_ring_size

    def dequeue_head(self):
        temp_ptr = self.head_ptr
        if (self.head_ptr == self.tail_ptr) or self.head_ptr = -1: #  Emptied the list so reset but preserve size
            self.head_ptr = -1
            self.tail_ptr = 0
            print('Queue Emptied')
            return
        else:
            if self.head_ptr == 0:
                self.head_ptr = self.size - 1
            else:
                self.head_ptr -= 1

        return self.queue[temp_ptr]


class Empty(Exception):
    pass

class LinkedQueue:
    """
    FIFO queue implementation using singly linked list
    """

    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node
        """
        __slots__  = '_element', '_next'

        def __init__(self, element, next ):
            self._element = element
            self._next = next


    def __init__(self):
        """
        Create an empty Queue
        """
        self._head = None
        self._size = 0              #   number of queue elements
        self._tail = None


    def __len__(self):
        """
        Return the number of element in the queue
        """
        return self._size

    def is_empty(self):
        """
        Return True if queue is Empty
        """
        return self._size == 0

    def first(self):
        """
        Return (but not remove) the element from the front of the Queue
        """
        if self.is_empty():
            raise Empty('Queue is empty')

        return self._head._element          # front aligned with head of the list


    def dequeue(self):
        """
        Remove and return the first element of the queue(i.e., FIFO)
        Raise exception if the Queue is empty
        """

        if self.is_empty():
            raise Empty('Queue is empty')

        answer = self._head._element        # get the current value/element from Front of the Queue
        self._head = self._head._next       # note how the address/pointer of next node is set here
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return answer


    def enqueue(self,value):
        """
        Add element to the back of the queue
        """

        new_data_node = self._Node(value, None)         # node will be new tail node

        if self.is_empty():
            self._head = new_data_node                  # special case: previous empty Queue
        else:
            self._tail._next = new_data_node

        self._tail = new_data_node                      # update reference to tail node
        self._size += 1


if __name__ == '__main__':
    bookingQueue = LinkedQueue()

    # print bookingQueue.first()
    bookingQueue.enqueue(3)
    print 'first element is ' + str(bookingQueue.first())
    bookingQueue.enqueue(4)
    print 'first element is ' + str(bookingQueue.first())
    bookingQueue.enqueue(5)
    print 'first element is ' + str(bookingQueue.first())

    print bookingQueue.dequeue()
    print 'first element after dequeue is ' + str(bookingQueue.first())



class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class ArrayQueue():
    """FIFO queue implementation using Python list as underlying storage"""

    DEFAULT_CAPACITY = 10       #moderate capacity for all new queues


    def __init__(self):
        """Create initially an empty Queue"""

        self._data  = [None] * ArrayQueue.DEFAULT_CAPACITY         # initialise an empty list with default capacity blocked at the begining itslef
        self._size  = 0
        self._front = 0                                            # 'front' is the index of the first element


    def __len__(self):
        """Return the number of elements in the Queue"""

        return self._size


    def is_empty(self):
        """Checks if queue is Empty or Not"""
        return self._size == 0



    def first(self):
        """
        Return (But NOT remove ) the element at the Front of the queue

        Raise Empty exception if the queue is empty

        """

        if self.is_empty():
            raise Empty('Queue is empty')

        return self._data[self._front]



    def dequeue(self):
        """
        Remove and return First element of the queue (FIFO)

        Raise an exception if queue is empty

        """

        if self.is_empty():
            raise Empty('Queue is empty Nothing to remove!')

        answer = self._data[self._front]

        self._data[self._front] = None                          # set the data of front element to None
                                                                # This helps in Garbage Collection

        self._front = (self._front + 1) % len(self._data)       # setting the front based on algo
                                                                # f = (f+1)% N
                                                                # where f is the front element index
                                                                # and N is the total predefined size(capacity) of the queue

        self._size = self._size - 1                             #update the size value as the element is now removed from the queue

        return answer










    def enqueue(self,e):
        """
        Add element to the back of the queue

        """

        if self._size == len(self._data):
            self._resize(2*len(self._data))                                         # if the max capacity of queue is
                                                                                    # reached then double the capacity

        available_index_position = (self._front + self._size) % len(self._data)

        self._data[available_index_position] = e

        self._size += 1


    def _resize(self,cap):
        """
        Resize to a new list of capacity >= len(self)
        """

        old = self._data                                                            # Keep Track of existing list
        self._data = [None]*cap                                                     # allocating new list with new capacity
        walk = self._front
        for k in range(self._size):                                                 # only consider existing elements
            self._data[k] = old[walk]                                               # intentionally shifting the indices
            walk = (1 + walk) % len(old)                                            # use old size as modulus

        self._front = 0                                                             # front has been realigned








if __name__ == '__main__':

    q = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)

    print "lenght is : " + str(len(q))
    print q.first()
    print q.dequeue()
    print q.first()

    q.enqueue(10)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print "lenght is : " + str(len(q))
    print  q.first()
    print  q.dequeue()
    print  q.dequeue()
    print  q.dequeue()
    print  q.dequeue()






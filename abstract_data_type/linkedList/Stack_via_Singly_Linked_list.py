# Operation 	Running Time
# S.push(e) 	O(1)
# S.pop() 	    O(1)
# S.top() 	    O(1)
# len(S) 	    O(1)
# S.is_empty() 	O(1)

# All bounds are worst-case and our space usage is O(n), where n is the current number of elements in the stack.


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class LinkedStack:
    """
    LIFO Stack Implementation using a singly linked list for storage
    """

    # Nested _Node class
    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node
        """
        __slots__ = '_element', '_next'             # streamline memory usage

        def __init__(self, element, next):          # initialize node's field
            self._element = element                 # reference to user's element
            self._next    = next                    # reference to next node


    #-----------------Stack Method--------------------------#

    def __init__(self):
        """
        Create and empty Stack
        """
        self._head = None                            # reference to head node
        self._size = 0                               # number of stack elements


    def __len__(self):
        """
        Return the number of elements in a stack
        """
        return self._size


    def is_empty(self):
        """
        Return True if the Stack is empty
        """
        return self._size == 0


    def push(self,e):
        """
        Add element e to the top of the stack
        """
        self._head = self._Node(e, self._head)      # create a new Node and Link it
        self._size += 1


    def top(self):
        """
        Return (but do not remove) the Top element from the Stack
        Raise empty exception if no data
        """

        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            return self._head._element


    def pop(self):
        """
        Return and Remove the Top element from the Stack

        Raise empty exception if no data
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            answer = self._head._element
            self._head = self._head._next
            self._size -= 1
            return answer

if __name__ == "__main__":
    Stack = LinkedStack()

    Stack.push(3)

    print Stack.top()

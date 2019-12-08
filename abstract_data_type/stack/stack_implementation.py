
#   S.push(e)   : 	    Add element e to the top of stack S.
#   S.pop()     : 	    Remove and return the top element from the stack S; an error occurs if the stack is empty.
#   S.top()     : 	    Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
#   S.is_empty(): 	    Return True if stack S does not contain any elements.
#   len(S)      : 	    Return the number of elements in stack S; in Python, we implement this with the special method _ _len_ _.

class Empty(Exception):
    """Exception attempting to Access element from an empty container"""
    pass

class ArrayStack():
    """LIFO Stack Implementation using a Python List as underlying storage"""

    def __init__(self):
        """Create an empty Stack"""
        self._data = []         #nonpublic list instance

    def __len__(self):
        """Return number of element in a Stack"""
        return len(self._data)

    def is_empty(self):
        """Retuns True if the Stack is Empty"""
        return len(self._data) == 0

    def push(self,e):
        """Add element 'e' to the top of the stack."""
        self._data.append(e)    #new item is stored at the end of the list

    def pop(self):
        """
        Remove and return the top element from the stack (i.e LIFO)

        Raise Empty Stack exception if stack is empty

        """

        if self.is_empty():
            raise Empty('Stack is empty!')

        return self._data.pop()         # remove last item from list

    def top(self):
        """
        Return (but not remove) the element from the top of the Stack

        Raise Empty Stack Exception is the stack is empty

        """
        if self.is_empty():
            raise Empty('Stack is empty!')

        return self._data[-1]           # last item from the list



if __name__ == '__main__':
    print "Hello World!"

    print "Lets create an empty stack        "
    stk = ArrayStack()

    print "Check if the stack is empty     : " + str(stk.is_empty())

    print "Add '5' to Stack                  "
    stk.push(5)

    print "Add '4' element to Stack          "
    stk.push(4)

    print "Get the top element from stack  : " + str(stk.top())

    print "Lets do a pop                   : " + str(stk.pop())

    print "Then check for top element      : " + str(stk.top())

    print "Another pop                     : " + str(stk.pop())

    print "Last pop                        : " + str(stk.pop())



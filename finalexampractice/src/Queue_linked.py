'''

--------------------------------------------
[CP164 A1]
--------------------------------------------

Author: Nabeel Shaikh
ID: 190741640
Email: shai1640@mylaurier.ca
__updated__:
---------------------------------------------
'''
# Imports
from copy import deepcopy

class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        val = _Queue_Node(deepcopy(value),None)
        if self._front is None:
            self._front = val
            self._rear = self._front
            self._count += 1
        else:
            curr = self._front
            while curr._next is not None:
                curr = curr._next
            curr._next = val
            self._rear = curr._next
            self._count += 1
            
        
        return deepcopy(val)

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"
        val = self._front._value
        self._count -=1
        
        if self._front._next is None:
            self._front = None
            self._rear = None
        else:
            self._front = self._front._next
        
        
        return val

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        return deepcopy(self._front._value)

    def _move_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"
        val = source._front
        source._front = source._front._next
        source._count -=1
        
        if self._rear is None:
            self._front = val
            self._rear = val
        else: 
            self._rear._next = val
            self._rear = self._rear._next
            self._rear._next = None
        self._count += 1
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        while not source.is_empty():
            self._move_front(source)
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while not source1._front is None and not source2._front is None:
            self._move_front(source1)
            self._move_front(source2)
        if source1._front is not None:
            self._append_queue(source1)
        if source2._front is not None:
            self._append_queue(source2)
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based queue (Queue)
            source2 - an array-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()
        
        while not self._front is None:
            target1._move_front(self)
            if self._front is not None:
                target2._move_front(self)     
        
        return target1,target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (recursive algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        # your code here
        return

    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        identical = True
        if self._count != target._count:
            identical = False
        else:
            curr = self._front
            targetcurr = target._front
            while identical is True and curr is not None and targetcurr is not None:
                if curr._value != targetcurr._value:
                    identical = False
                else:
                    curr = curr._next
                    targetcurr = targetcurr._next
            
        return identical

    def is_identical_r(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Entries of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (recursive algorithm)
        Use: b = source.is_identical_r(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
x=Queue()
x.insert(1)     
x.insert(2)
x.insert(3)
x.insert(4)
target1,target2 = x.split_alt() 
for a in target1:
    print(a)

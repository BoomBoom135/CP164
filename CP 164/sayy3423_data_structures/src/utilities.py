"""
-------------------------------------------------------
utilities
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-24"
-------------------------------------------------------
"""
# imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
# function for #2


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        stack.push(source.pop())

    return


# function for #3


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while stack.is_empty() != True:
        target.insert(0, stack.pop())

    return


# function for #4


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    for line in source:
        if not stack.is_empty():
            print(f"Stack Not Empty!: {stack.is_empty()}")
            print(f"Peeking Stack: {stack.peek()}")
            print(f"Popping Stack: {stack.pop()}")
        else:
            print("Empty Stack!")
        stack.push(line)
        print(f"Pushed {line}")
    return
# ----------------------------------------------------------------------------------------------


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        queue.insert(source.pop(0))

    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while queue.is_empty() != True:
        target.append(queue.remove())
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand
    for item in a:
        if not q.is_empty():
            print("Queue Not Empty")
            print("Peaked:", q.peek())
            print("Removed:", q.remove())
        else:
            print("Queue Empty")
        q.insert(item)
        print("Pushed {} into Queue".format(item))

    return

# ----------------------------------------------------------------------------------------------


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        pq.insert(source.pop(0))

    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while pq.is_empty() != True:
        target.append(pq.remove())

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand
    for data in a:
        if not pq.is_empty():
            print("PQ Empty")
            print("Peaked:", pq.peek())
            print("Removed:", pq.remove())
        else:
            print('Queue Empty')
        pq.insert(data)
        print('Pushed {} into PQ'.format(data))

    return

'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        for x in (1,len(self.queue)):
            self.queue.append(self.queue.pop(0)) # Pop's the top most element.
        self.queue.pop(0)

    def top(self):
        """
        :rtype: int
        """
        top = None
        for x in range(len(self.queue)):
            top = self.queue.pop()
            self.queue.append(top)
        return top

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue is None





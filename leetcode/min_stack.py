'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''



class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

        if len((self.stack2) is None) or (x < self.stack2[-1]):
            self.stack2.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        top_value = self.stack1[-1]
        self.stack1.pop()
        if top_value is self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]


    def getMin(self):
        """
        :rtype: int
        """
        ## Minimum value since located at the top of stack2.
        return self.stack2[-1]
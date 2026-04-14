# from collections import deque
class MyQueue(object):

    def __init__(self):
        self.stack=[]

    def push(self, x):
        self.stack.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if len(self.stack)==1:
            return self.stack.pop()
        temp=self.stack.pop()
        item=self.pop()
        self.stack.append(temp)
        return item
        """
        :rtype: int
        """
        

    def peek(self):
        if len(self.stack)==1:
            return self.stack[-1]
        temp=self.stack.pop()
        item=self.peek()
        self.stack.append(temp)
        return item
        
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.stack)==0
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
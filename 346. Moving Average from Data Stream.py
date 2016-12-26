#   Question: 346. Moving Average from Data Stream
# Difficulty: Easy
#       Tags: Design, Queue
'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

'''

class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.data = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.data.append(val)
        if len(self.data) == 0:
            return 0
        if len(self.data) == self.size + 1:
            self.data.pop(0)
        return float(sum(self.data)) / len(self.data)


m = MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.next(4))

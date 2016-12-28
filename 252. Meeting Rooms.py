#   Question: 252. Meeting Rooms
# Difficulty: Easy
#       Tags: Sort
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine
if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) == 0:
            return True
        sorted_intervals = sorted(intervals, key = lambda e: e.start)
        start = sorted_intervals[0].start
        end = sorted_intervals[0].end
        for i in range(1,len(sorted_intervals)):
            if sorted_intervals[i].start < end:
                return False
            else:
                end = sorted_intervals[i].end
        return True
#   Question: 455. Assign Cookies
# Difficulty: Easy
#       Tags: Math
'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most
one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will
be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
and the child i will be content. Your goal is to maximize the number of your content children and output
the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

'''

from collections import deque
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = deque(sorted(g)), deque(sorted(s))
        satisfy = len(g)
        i, j = 0, 0
        while g and s:
            if g[0] <= s[0]:
                g.popleft()
            s.popleft()
        satisfy = satisfy - len(g)
        return satisfy

s = Solution()
print(s.findContentChildren([1,2,3], [1,2]))
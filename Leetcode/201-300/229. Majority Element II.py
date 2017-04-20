class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        if nums == []: return []
        if len(nums) < 3:
            ret = list(set(nums))
        else:
            nums = sorted(nums)
            if len(nums) == 3:
                if nums[0] == nums[1] or nums[1] == nums[2]:
                    ret.append(nums[1])
            elif len(nums) > 3:
                p1, p2 = nums[len(nums) / 3], nums[-(1 + len(nums) / 3)]
                if p1 == p2:
                    ret.append(p1)
                else:
                    p1_cnt, p2_cnt = 0, 0
                    for i in nums:
                        if i == p1: p1_cnt += 1
                        if i == p2: p2_cnt += 1

                    if p1_cnt > len(nums) / 3: ret.append(p1)
                    if p2_cnt > len(nums) / 3: ret.append(p2)
        return ret
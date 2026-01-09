class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortnums = sorted(nums)
        longest, cur_longest = 0, min(1, len(sortnums))
        for i in range(1, len(sortnums)):
            if sortnums[i] == sortnums[i-1]: continue
            if sortnums[i] == sortnums[i-1] + 1:
                cur_longest += 1
            else:
                longest, cur_longest = max(longest, cur_longest), 1
        return max(longest, cur_longest)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        res = 0
        
        while nums_set:
            curr = 1
            num = nums_set.pop()
            lower = num - 1
            higher = num + 1
            while lower in nums_set:
                nums_set.remove(lower)
                lower -= 1
                curr += 1
            while higher in nums_set:
                nums_set.remove(higher)
                higher += 1
                curr += 1
            res = max(res, curr)

        return res
        
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        result = []

        for num in nums:
            right = total - left - num
            result.append(abs(left - right))
            left += num

        return result
        
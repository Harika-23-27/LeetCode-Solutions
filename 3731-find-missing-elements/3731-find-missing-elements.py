class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        num_set=set(nums)
        min_num=min(nums)
        max_num=max(nums)
        missing=[]

        for i in range(min_num, max_num + 1):
            if i not in num_set:
                missing.append(i)
        return missing
        
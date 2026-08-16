class Solution(object):
    def sortColors(self, nums):
        low,temp,high=0,0,len(nums)-1
        while temp<=high:
            if nums[temp]==0:
                nums[low],nums[temp]=nums[temp],nums[low]
                low+=1
                temp+=1
            elif nums[temp]==1:
                temp+=1
            else:
                nums[temp],nums[high]=nums[high],nums[temp]
                high-=1
        return nums
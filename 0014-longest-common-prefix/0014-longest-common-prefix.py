class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        ans=""
        left,right=strs[0],strs[-1]
        for i in range(min(len(left),len(right))):
            if left[i]==right[i]:
                ans+=left[i]
            else:
                break
        return ans



        
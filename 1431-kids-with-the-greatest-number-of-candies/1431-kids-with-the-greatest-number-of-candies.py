class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l=[]
        for i in candies:
            l.append((i+extraCandies) >= max(candies))
        return l


                
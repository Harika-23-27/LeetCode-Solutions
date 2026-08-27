class Solution:
    def maxDifference(self, s: str) -> int:
        
        a={}
        for char in s:
            if char in a:
                a[char]+=1
            else:
                a[char]=1
        odd =[]
        even=[]
        for freq in a.values():
            if freq % 2:
                odd.append(freq)
            else:
                even.append(freq)
        return max(odd)-min(even)

        
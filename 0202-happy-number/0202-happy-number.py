class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            s_1=0
            for i in str(n):
                s=int(i)**2
                s_1+=s
            n=s_1
        return True





        
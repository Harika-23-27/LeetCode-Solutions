class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        for i in str(n):
            s+=int(i)
            p*=int(i)
        a=s+p
        if n%a==0:
            return True
        return False


        
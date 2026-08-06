class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=10:
            a=str(num)
            total=0
            for i in a:
                s=int(i)
                total+=s
                num=total
        return num


                



        
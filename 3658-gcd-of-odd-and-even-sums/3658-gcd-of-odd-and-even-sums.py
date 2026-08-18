class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        n1=n*2
        sumOdd=0
        sumEven=0
        for i in range(1,n1+1):
            if i%2!=0:
                sumOdd+=i
            else:
                sumEven+=i
        return math.gcd(sumOdd, sumEven)


        
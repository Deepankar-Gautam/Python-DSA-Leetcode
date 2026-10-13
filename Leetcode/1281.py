class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        while n != 0:
            l = n % 10
            n = n // 10
            p = p * l
            s = s + l

        return (p - s)
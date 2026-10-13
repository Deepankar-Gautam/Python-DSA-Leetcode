class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        c = 0
        for i in nums:
            t = 0
            x = i
            for j in (str(i)):
                x //= 10
                t += 1
            if t % 2 == 0:
                c += 1
        return c
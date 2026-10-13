class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        o = 0
        x = str (num)
        n = ""
        for i in range (len(x) - k + 1):
            n = ""
            for j in range (k):
                n += x [i + j]
            n = int (n)
            if n != 0 and num % n == 0:
                o += 1
        return o
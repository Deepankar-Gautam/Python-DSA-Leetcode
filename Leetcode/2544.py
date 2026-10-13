class Solution:
    def alternateDigitSum(self, n: int) -> int:
        x = str (n)
        result = 0
        for i in range (0, len(x)):
            if i % 2 == 0:
                result += int (x[i])
            else:
                result -= int (x[i])
        return result
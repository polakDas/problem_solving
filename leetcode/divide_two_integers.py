class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        sign = 1
        if divisor < 0:
            sign *= -1
            divisor *= -1
        if dividend < 0:
            sign *= -1
            dividend *= -1
        while divisor <= dividend:
            dividend -= divisor
            result += 1
        return result*sign

if __name__ == "__main__":
    dividend = 7
    divisor = -3

    solve = Solution()
    print(solve.divide(dividend=dividend, divisor=divisor))
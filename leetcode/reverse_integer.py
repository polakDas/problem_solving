class Solution:
    def reverse(self, x: int) -> int:
        # isNegative = False
        # if x < 0:
        #     isNegative = True
        #     x = -x
        
        # reverse = 0
        # while x > 0:
        #     reverse = reverse * 10 + x % 10
        #     x //= 10
        
        # if reverse >= 2 ** 31 - 1 or reverse <= -2 ** 31 - 1:
        #     return 0
        
        # return -reverse if isNegative else reverse

        if x >= 0:
            reverse = int(str(x)[::-1])
        else:
            reverse = -int(str(x)[::-1][:-1])
        return reverse if -2 ** 31 -1 <= reverse and reverse <= 2 ** 31 - 1 else 0

if __name__ == '__main__':
    solve = Solution()

    number = 0
    result = solve.reverse(number)
    print(result)

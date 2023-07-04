class Solution:
    def addDigits(self, num):
        '''
        I learn an amezing trick today. 
        The problem is "Given an integer num, repeatedly add all its digits until the result has only one digit, and return it."
        And the beautiful trick is
        If number is divisible by 9 completely then digital root(ans) is 9,else the digital root is remainder obtained.
        '''
        if num % 9 == 0 and num != 0:
            return 9
        else:
            return num % 9

if __name__=="__main__":
    solve = Solution()
    print(solve.addDigits(6))
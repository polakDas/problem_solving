class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # without built-in functions
        # result = 0
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] != ' ':
        #         result += 1
        #     elif result > 0:
        #         break
        # return result

        # with built-in function
        return len(s.split()[-1])


if __name__=="__main__":
    s = "   fly me   to   the moon   "

    solve = Solution()
    print(solve.lengthOfLastWord(s=s))
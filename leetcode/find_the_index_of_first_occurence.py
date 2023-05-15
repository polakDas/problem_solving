class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if len(needle) > len(haystack) - i:
                break
            if haystack[i] == needle[0]:
                temp = len(needle)
                for j in range(temp):
                    if haystack[i+j] != needle[j]:
                        break
                    else:
                        if temp == j + 1:
                            return i
        return -1

if __name__ == "__main__":
    solve = Solution()
    haystack = "mississippi"
    needle = "issippi"
    print(solve.strStr(haystack=haystack, needle=needle))
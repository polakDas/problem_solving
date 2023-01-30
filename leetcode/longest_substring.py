class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            result = max(result, right - left + 1)
        return result

if __name__ == '__main__':
    s = 'abcabcbb'
    s = 'pwwkew'
    solve = Solution()
    print(solve.lengthOfLongestSubstring(s=s))
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in mapping.keys():
                stack.append(mapping[char])
            elif not stack or stack[-1] != char:
                return False
            else:
                stack.pop()
        return len(s) == 0

if __name__ == '__main__':
    s = "()[]{}"
    s = "(]"
    s="["
    solve = Solution()
    print(solve.isValid(s))

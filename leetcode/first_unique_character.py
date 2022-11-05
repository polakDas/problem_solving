class Solution:
    def firstUnique(self, s: str) -> int:
        result = {}
        for c in s:
            if c in result:
                result[c] += 1
            else:
                result[c] =1
            
        for i in result:
            if result[i] == 1:
                return s.index(i)
        return -1

if __name__ == "__main__":
    s = "leetcode"
    s = 'loveleetcode'
    s = 'aabb'
    solve = Solution()

    print(solve.firstUnique(s=s))
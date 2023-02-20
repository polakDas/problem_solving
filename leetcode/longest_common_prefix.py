# leetcode problem no 14. Longest common prefix

class Solution:
    def longest_common_prefix(self, strs):
        result = ""

        sn = 0
        while True:
            for s in strs:
                if sn == len(s) or s[sn] != strs[0][sn]:
                    return result
            result += strs[0][sn]
            sn += 1
        
        return result

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    solve = Solution()
    print(solve.longest_common_prefix(strs=strs))
class Solution:
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= i
        return result

if __name__=="__main__":
    nums = [4,1,2,1,2,4,50]

    solve = Solution()

    print(solve.singleNumber(nums=nums))

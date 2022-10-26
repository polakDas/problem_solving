# Leetcode problem no. 56. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)

        return maxSub

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solve = Solution()
    print(solve.maxSubArray(nums=nums))

if __name__ == "__main__":
    main()

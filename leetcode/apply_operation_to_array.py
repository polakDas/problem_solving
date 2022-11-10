# Leetcode problem no 2460. Apply Operations to an Array

class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i] = 0
                nums[i-1] *= 2

        flag = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != flag:
                    nums[flag] = nums[i]
                    nums[i] = 0
                flag += 1
        return nums

if __name__ == "__main__":
    nums = [1,2,2,1,1,0]
    nums = [0, 1]
    solve = Solution()
    print(solve.applyOperations(nums=nums))
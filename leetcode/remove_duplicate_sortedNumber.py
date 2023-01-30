# Leetcode problem 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # left = 1    left and right are two flags, used to modifie list
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
        return left

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 3, 5, 7, 7, 8]
    solve = Solution()
    print(nums[:solve.removeDuplicates(nums=nums)])
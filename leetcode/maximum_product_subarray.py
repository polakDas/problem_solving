# Leetcode problem no 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]

        temp_max = 1
        temp_min = 1

        for num in nums:
            temp = temp_max * num
            temp_max = max(temp, temp_min * num, num)
            temp_min = min(temp, temp_min * num, num)
            max_product = max(temp_max, max_product)

        return max_product

if __name__ == '__main__':
    nums = [2,3,-2,4]
    solve = Solution()
    print(solve.maxProduct(nums=nums))
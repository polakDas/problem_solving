# Leetcode problem number 238. Product of array except self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        prefix = 1
        for i  in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result

def main():
    nums = [5, 2, 1, 3, 2, 6]
    solve = Solution()
    print(solve.productExceptSelf(nums=nums))

if __name__ == "__main__":
    main()
        
# leetcode problem no 27. Remove Element

class Solution:
    def moveZeros(self, nums: list[int]) -> list[int]:
        if len(nums) < 1:
            return nums

        flag = 0
        # [1, 2, 3, 4]
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != flag:
                    nums[flag] = nums[i]
                    nums[i] = 0
                flag += 1
        return nums

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    solve = Solution()
    print(solve.moveZeros(nums=nums))
    print(nums)

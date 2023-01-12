# leetcode problem no 27. Remove Element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        flag = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[flag] = nums[i]
                flag += 1
        return flag

if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    solve = Solution()
    print(solve.removeElement(nums=nums, val=3))
    print(nums)

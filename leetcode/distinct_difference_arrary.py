class Solution:
    def distinctDifferenceArray(self, nums):
        # result = []
        # for i in range(len(nums)):
        #     result += [len(set(nums[:i+1])) - len(set(nums[i+1:]))]
        # return result

        # single line solution
        return [len(set(nums[:i+1])) - len(set(nums[i+1:])) for i in range(len(nums))]

if __name__=="__main__":
    # nums = [1,2,3,4,5]
    nums = [3,2,3,4,2]

    solve = Solution()
    print(solve.distinctDifferenceArray(nums=nums))
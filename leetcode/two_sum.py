class Solution:
    def twoSum(self, nums, target):
        result = {}
        for i in nums:
            if(target-i in result):
                print(nums.index(i))
                return [nums.index(i), nums.index(result.get(i))]
            else:
                # print(nums.index(i))
                result[i] = target - i
        # return result

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    
    solve = Solution()
    print(solve.twoSum(nums=nums, target=target))

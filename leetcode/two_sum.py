class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            tempTarget = target - nums[i]
            if tempTarget in hashmap:
                return [i, hashmap[tempTarget]]
            hashmap[nums[i]] = i
            
        # hashmap = {}
        # for i in nums:
        #     tempTarget = target - i
        #     # hashmap[i] = tempTarget
        #     if tempTarget in hashmap:
        #         return [nums.index(tempTarget), nums.index(i)]
        #     hashmap[i] = tempTarget
        #     # else:
        #         # print(nums.index(i))
        #         # hashmap[i] = tempTarget
        # # return result

if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9
    # nums = [3,2,4]
    # target = 6
    nums = [3,3]
    target = 6
    
    solve = Solution()
    print(solve.twoSum(nums=nums, target=target))

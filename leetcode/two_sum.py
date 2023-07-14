# This is one of my favourite problem.
# I've solve this problem many times


class Solution:
    def twoSum(self, nums, target):
        # using bruteforce
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return list((i, j))

        # using dictionary
        # hashmap = {}
        # for i in range(len(nums)):
        #     tempTarget = target - nums[i]
        #     if tempTarget in hashmap:
        #         return [i, hashmap[tempTarget]]
        #     hashmap[nums[i]] = i

        # using tuple
        storage = tuple()
        for i in range(len(nums)):
            tempTarget = target - nums[i]
            if tempTarget in storage:
                return [storage.index(tempTarget), i]
            storage += nums[i],


if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9
    # nums = [3,2,4]
    # target = 6
    nums = [3,3]
    target = 6
    
    solve = Solution()
    print(solve.twoSum(nums=nums, target=target))

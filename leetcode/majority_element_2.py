from collections import defaultdict
import math

class Solution:
    def majorityElement(self, nums):
        hash = defaultdict(int)
        result = []
        oneThird = len(nums)//3

        for num in nums:
            hash[num] += 1

        for key, value in hash.items():
            if value > oneThird:
                result.append(key)
            
        return result

if __name__=="__main__":
    nums = [2,2,1,1,1,2,2]

    solve = Solution()
    print(solve.majorityElement(nums=nums))

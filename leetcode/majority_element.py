from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        '''
        If a single element repeat more than half of total elements then
        the count will more than zero for that element
        '''
        count = 0
        element = 0
        for n in nums:
            if count == 0:
                element = n
            
            if element == n:
                count += 1
            else:
                count -= 1
        return element

if __name__=="__main__":
    nums = [2,2,1,1,1,2,2]

    solve = Solution()
    print(solve.majorityElement(nums=nums))

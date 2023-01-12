# Leetcode problem no 1331. Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sortedArr = arr.copy()
        sortedArr.sort()
        ranks = {}

        rank = 1
        for i in range(len(sortedArr)):
            if sortedArr[i] not in ranks:
                ranks[sortedArr[i]] = rank
                rank += 1
        
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]

        return arr

if __name__ == "__main__":
    solve = Solution()
    arr = [40,10,20,30]
    arr = [100,100,100]
    arr = [37,12,28,9,100,56,80,5,12]
    print(solve.arrayRankTransform(arr=arr))


# Awesome solution found in leetcode solution section

# class Solution:
#     def arrayRankTransform(self, arr: List[int]) -> List[int]:
#         hmap = {val: i+1 for i, val in enumerate(sorted(set(arr)))}
#         return [hmap[val] for val in arr]


# Another great solution

# class Solution:
#     def arrayRankTransform(self, arr: List[int]) -> List[int]:
#         rank = {}
#         for a in sorted(arr):
#             rank.setdefault(a, len(rank) + 1)
#         return map(rank.get, arr)
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        l, h = 0, ROWS - 1
        while h >= l:
            c = (h + l) // 2
            if target > matrix[c][-1]:
                l = c + 1
            elif target < matrix[c][0]:
                h = c - 1
            else:
                break
        
        if not h >= l:
            return False

        row = (h + l) // 2
        left, right = 0, COLUMNS - 1
        while(left <= right):
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False

if __name__ == '__main__':
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 3
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    solve = Solution()
    print(solve.searchMatrix(matrix=matrix, target=target))

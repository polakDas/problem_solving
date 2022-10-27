# Leetcode problem no 118. Pascal's Triangle

# I just love this solution. The idea of a temporary array with first and last empty index is just awesome.
# Video link of solve: https://youtu.be/nPVEaB3AjUM

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Assign the first value
        result = [[1]]

        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]   # Assign value zero in first and last index
            row = []

            for j in range(len(result[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            result.append(row)
        
        return result
    
def main():
    numRows = 5

    solve = Solution()
    
    print(solve.generate(numRows=numRows))

if __name__ == "__main__":
    main()
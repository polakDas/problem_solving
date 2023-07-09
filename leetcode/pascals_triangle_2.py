import time

class Solution:
    def getRow(self, rowIndex):
        '''
        We can find the row's element by this formula
        C(n, k) = n!//(k!*(n-k)!)
        where n is the row number and k is the column number

        There's a python math function to generate this combinition.
        math.comb(row, column)
        '''
        def factorial(num):
            if num < 1:
                return 1
            return num * factorial(num - 1)
        
        result = []
        for i in range(rowIndex + 1):
            result.append( factorial(rowIndex) // (factorial(i) * factorial(rowIndex - i)))
        return result

if __name__=="__main__":
    rowIndex = 33
    start_time = time.time()

    solve = Solution()
    print(solve.getRow(rowIndex=rowIndex))

    end_time = time.time()

    print(f"Time taken {end_time - start_time}s")


# 2nd solution without recursion
# class Solution:
#     def getRow(self, rowIndex: int):
#         row = [1]  # The first element of each row is always 1

#         for i in range(rowIndex):
#             # Calculate the elements of the current row based on the previous row
#             for j in range(len(row) - 1, 0, -1):
#                 row[j] += row[j - 1]

#             # Append 1 at the end of the current row
#             row.append(1)

#         return row

# if __name__=="__main__":
#     numRows = 5
#     solve = Solution()
#     print(solve.getRow(rowIndex=numRows))

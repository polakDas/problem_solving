# Leetcode problem no 566. Reshape the matrix

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        result = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(m * n):
            result[i // c][i % c] = mat[i // n][i % n]
        
        return result

def main():
    # mat = [[1,2],[3,4]]
    # r = 1
    # c = 4
    mat = [[1, 2, 3, 4], [5, 6, 7, 8]]
    r = 4
    c = 2

    solve = Solution()
    print(solve.matrixReshape(mat=mat, r=r, c=c))

if __name__ == "__main__":
    main()

class Solution:
    def licenseKeyFormatting(self, s, k):
        result = ""
        dashCount = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '-':
                continue
            if dashCount % (k + 1) == 0:
                result += '-'
                dashCount = 1
            result += s[i].upper()
            dashCount += 1
        return result[::-1]

if __name__=="__main__":
    solve = Solution()
    s = "5F3Z-2e-9-w"
    k = 4

    # solve.licenseKeyFormatting(s, k)
    print(solve.licenseKeyFormatting(s=s, k=k))
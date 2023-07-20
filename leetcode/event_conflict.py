class Solution:
    def haveConflict(self, event1, event2):
        return event1[0] <= event2[0] <= event1[1] or event2[0] <= event1[0] <= event2[1]

if __name__=="__main__":
    event1 = ["01:15","02:00"]
    event2 = ["02:00","03:00"]

    solve = Solution()
    print(solve.haveConflict(event1, event2))
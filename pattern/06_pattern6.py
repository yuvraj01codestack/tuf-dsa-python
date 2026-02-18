class Solution:
    def pattern6(self,n):
        for i in range(n):
            for j in range(n - i):
                print(j + 1, end="")
            print()



if __name__ == "__main__":
    Solution().pattern6(5)
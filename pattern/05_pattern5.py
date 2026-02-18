class Solution:
    def pattern5(self,n):
        for i in range(n):
            for j in range(n - i):
                print("*", end="")
            print()



if __name__ == "__main__":
    Solution().pattern5(5)
class Solution:
    def pattern7(self,n):
        for i in range(n , 0 , -1):
            for j in range(i):
                print(" ", end="")
            for k in range((n + 1) - i):
                print("*", end="")
            for k in range(n - i):
                print("*", end="")
            print()









if __name__ == "__main__":
    Solution().pattern7(5)



class Solution:
    def pattern8(self,n):
        for i in range(n , 0 , -1):
            for k in range(n - i):
                print(" ", end="")
            for k in range(i-1):
                print("*", end="")
            for k in range(i):
                print("*", end="")
            print()









if __name__ == "__main__":
    Solution().pattern8(5)



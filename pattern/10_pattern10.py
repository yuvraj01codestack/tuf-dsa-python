

class Solution:
    def pattern10(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()

        for k in range(n):
            for l in range(n - k - 1):
                print("*", end="")
            print()



if __name__ == "__main__":
    Solution().pattern10(5)
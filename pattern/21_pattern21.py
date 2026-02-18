class Solution:
    def pattern21(self, n):
        for i in range(1, n + 1):
            for k in range(i):
                print("*", end="")
            for z in range((n-i) * 2):
                print(" ", end="")
            for z in range(i):
                print("*", end="")
            print()

        for i in range(n - 1, 0, - 1):
            for k in range(i):
                print("*", end="")
            for z in range((n-i) * 2):
                print(" ", end="")
            for z in range(i):
                print("*", end="")
            print()




if __name__ == "__main__":
    Solution().pattern21(4)

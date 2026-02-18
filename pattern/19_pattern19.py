class Solution:
    def pattern19(self, n):
        for i in range(n, 0, -1):
            for k in range(i):
                print("*", end="")
            for z in range((n-i) * 2):
                print(" ", end="")
            for z in range(i):
                print("*", end="")
            print()

        for i in range(n):
            for k in range(i + 1):
                print("*", end="")
            for z in range((n - i - 1) * 2):
                print(" ", end="")
            for z in range(i + 1):
                print("*", end="")
            print()


if __name__ == "__main__":
    Solution().pattern19(4)

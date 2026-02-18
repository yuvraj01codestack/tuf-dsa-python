class Solution:
    def pattern17(self, n):
        for i in range(n):
            for j in range(n - i):
                print(" ", end="")
            for k in range(i):
                print(chr(65 + k), end="")
            for z in range(i, -1, -1):
                print(chr(65 + z), end="")


            print()


if __name__ == "__main__":
    Solution().pattern17(5)

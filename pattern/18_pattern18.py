class Solution:
    def pattern18(self, n):
        z = 65 + n - 1
        for i in range(n):
            for k in range(i + 1):
                print(chr(z - i + k), end="")
            print()


if __name__ == "__main__":
    Solution().pattern18(4)

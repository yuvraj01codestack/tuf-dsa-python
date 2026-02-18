class Solution:
    def pattern12(self,n):
        width = len(str(n))

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(f"{j:>{width}}", end="")

            for _ in range(2 * (n - i)):
                print(" " * width, end="")

            for j in range(i, 0, -1):
                print(f"{j:>{width}}", end="")

            print()



if __name__ == "__main__":
    Solution().pattern12(10)
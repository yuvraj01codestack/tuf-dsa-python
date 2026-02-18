class Solution:
    def pattern20(self, n):
        for i in range( n):
            for k in range(n):
                if (i == 0 or k == 0) or (i == n -1 or k == n-1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()






if __name__ == "__main__":
    Solution().pattern20(4)

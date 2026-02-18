

class Solution:
    def pattern4(self,n):
        for i in range(n):
            for j in range(i + 1):
                print(i + 1, end="")
            print()



if __name__ == "__main__":
    Solution().pattern4(5)
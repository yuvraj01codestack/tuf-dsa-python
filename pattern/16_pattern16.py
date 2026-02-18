class Solution:
    def pattern16(self,n):
        for i in range(n):
            for j in range(i + 1):
                print(chr(65 + i) , end="")
            print()



if __name__ == "__main__":
    Solution().pattern16(10)
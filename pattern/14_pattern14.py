class Solution:
    def pattern14(self,n):
        for i in range(n):
            for j in range(i + 1):
                print(chr(ord("A") + j) , end="")
            print()



if __name__ == "__main__":
    Solution().pattern14(10)
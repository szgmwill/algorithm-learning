class Solution :
    def generateParanthesis(self, n) :
        self.list = []
        self._recursion(0, 0, n, "")
        return self.list

    def _recursion(self, left, right, n, result) : 
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._recursion(left + 1, right, n, result + "(")
        if right < n and right < left:
            self._recursion(left, right + 1, n, result + ")")

if __name__ == "__main__":
    solution = Solution()
    solution.generateParanthesis(6)
    print(solution.list)

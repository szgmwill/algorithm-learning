# 1. Clarification
# 2. Always think about brute-force solution firstly
# 3. Step by step find other efficient possible solutions
# 3. Coding
# 4. Testing


import Tier
class Solution:

    # Quick Sort
    def minmum_total_Sort(self, triangle: [[]]) -> int:
        row_len = len(triangle)
        if row_len == 0 or len(triangle[0]) == 0:
            return 0
        minmum = 0
        for cur_row in range(row_len):
            print(f'cur_row is {cur_row}, array is {triangle[cur_row]}')
            cur_minmum = sorted(triangle[cur_row])
            print(f'cur_minmum array is {cur_minmum}')
            minmum += cur_minmum
            print(f'Current cur_minmum is {cur_minmum}, total is {minmum}')

        return minmum


    # DP solution
    def minmum_total_DP(self, triangle: [[]]) -> int:
        row_len = len(triangle)
        if row_len == 0 or len(triangle[0]) == 0:
            return 0

        # init the start values
        # for j in range(len(triangle[row_len - 1])):
        #     print(f'================ j is {j}')
        #     DP[row_len - 1][j] = triangle[row_len - 1][j]
        
        rows = row_len - 2 # start from the second row
        for row_index in range(rows, -1, -1): 
            cols = len(triangle[row_index]) - 1
            for col_index in range (cols, -1, -1): # start from last col to the first col of 0
                # DP formula
                triangle[row_index][col_index] = min(triangle[row_index + 1][col_index], triangle[row_index + 1][col_index + 1]) + triangle[row_index][col_index]
                print(f'triangle[{row_index}][{col_index}] is {triangle[row_index][col_index]}')

        return triangle[0][0]
    
    # Brute-force
    def minmum_total_DFS(self, triangle: [[]]) -> int:
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0

        return self._dfs(triangle,0, 0, '', 0)

    def _dfs(self, triangle: [[]], i: int, j: int, path: '', sum: int) -> int:
        #1. teminator
        if i == (len(triangle) - 1): #already to the bottom
            path += f'{triangle[i][j]} #'
            print(f'Recursion terminated. min path: {path}')
            return sum + triangle[i][j]

        #2. process
        path += f'{triangle[i][j]} -> '
        sum += triangle[i][j]

        #3. drill down
        left_bottom_min = self._dfs(triangle, i + 1, j, path, sum)
        right_bottom_min = self._dfs(triangle, i + 1, j + 1, path, sum)

        #4. clear states (anything done in the step 2)
        #Note: no need to clear up since result is not used

        return min(left_bottom_min, right_bottom_min)

if __name__ == "__main__":
    solution = Solution()
    triangle = [[2], [1, 2], [3, 1, 2]]
    result1 = solution.minmum_total_DP(triangle)
    result2 = solution.minmum_total_DFS(triangle)
    result3 = solution.minmum_total_Sort(triangle)
    #result = solution.minmumTotal([[], []])
    print(f"=============result1 is : {result1}, result2 is : {result2}")
    print(f"=============result3 is : {result3}")



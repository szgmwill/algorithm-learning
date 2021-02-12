'''
887. Super Egg Drop
Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
'''
class Solution:
    memo = dict()
    def _dp(self, K: int, N: int) -> int:
        # terminate condition, base case
        if K == 1:
            return N
        elif N == 0:
            return 0
        
        # avoid repeat cal
        if (K, N) in self.memo:
            return self.memo[(K, N)]

        # log the result
        res = float('INF') 
        # scan each floor
        for i in range(1, N+1) :
            print("This is the %sth floor" % i)
            res = min(
                max(
                    # broken
                    self._dp(K - 1, i - 1),
                    self._dp(K, N - i)
                ) + 1,
                res
            )
        #store in mem
        self.memo[(K, N)] = res
        return res
    
    def superEggDrop(self, K: int, N: int) -> int:
        if K < 0 or N < 0:
            return 0

        return self._dp(K, N)

if __name__ == "__main__":
    print("Running in progress")
    solution = Solution()
    K = 4 
    N = 1000
    res = solution.superEggDrop(K, N)
    print("Result is {res}".format(res = res))


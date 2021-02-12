from heapq import heapify
from heapq import heappop
from heapq import heappush
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: [], Capital: []) -> int:
        H1, H2 = list(zip(Capital, Profits)), []
        heapify(H1)
        for _ in range(k):
            while H1 and H1[0][0] <= W:
                heappush(H2, -heappop(H1)[1])
            if not H2:
                break
            W -= heappop(H2)
        return W
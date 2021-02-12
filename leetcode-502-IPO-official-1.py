from heapq import nlargest
from sys import maxsize
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: [], Capital: []) -> int:
        print("Need to loop %d times" % k)
        print("The current capital is {}".format(W))

        project_count = len(Profits)
        # check all inputs are valid
        if k <= 0 or project_count == 0 or len(Capital) != project_count:
            print("Wooo, something went wrong, {}, {}, {}".format(k, project_count, W))
            return W
        
        # To speed up, if all projects can be selected
        max_capital = max(Capital)
        if W > max_capital:
            print("Speed up! All projects can be selected, {W}, {max}".format(W=W, max=max_capital))
            # use n-largets heap
            return W + sum(nlargest(k, Profits))
        
        # enter normal process
        for times in range(min(k, project_count)):
            print("This is the {} times loop".format(times))
            # current selected index
            selected_idx = -1
            for idx in range(project_count):
                if W >= Capital[idx]:
                    # this index project is selected
                    if selected_idx == -1 or Profits[selected_idx] < Profits[idx]:
                        selected_idx = idx

            # no project can be selected, that means the initial capital is not avaliable to select any of project, break and return
            if selected_idx == -1:
                print("no project can be selected due to not enough capital %d" % W)
                break

            #  markdown the selected
            Capital[selected_idx] = maxsize
            W += Profits[selected_idx]
        
        return W

solution = Solution()
result = solution.findMaximizedCapital(2, 0, [1,2,3], [0,1,1])
print("Total result is", result)



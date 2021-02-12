class Solution:
    def findMaximizedCapital(self, k: int, W: int, Capitals: [], Profits: []) -> int:
        if k <= 0 or len(Profits) == 0 or len(Capitals) == 0:
            print("something went wrong")
            return 0
        if W >= max(Capitals):
            Profits.sort(reverse=True)
            return W + sum(Profits[:k])
        # mark down the selected project to deduplicate
        selected_project_index = set()
        # dynamic available captial, init value = W
        #available_capitals = W
        for times in range(k):
            # the selected project index and profit
            current_selected_index = -1
            maxmized_profit = 0
            for index, required_capital in enumerate(Capitals):
                if index not in selected_project_index and W >= required_capital:
                    current_profits = Profits[index]
                    if current_profits > maxmized_profit:
                        maxmized_profit = current_profits
                        current_selected_index = index
            if current_selected_index >= 0:
                print("current_selected_index is", current_selected_index)
                W = W + maxmized_profit
                selected_project_index.add(current_selected_index)
                #available_capitals += (maxmized_profit - Capitals[current_selected_index])
        return W

if __name__ == "__main__":
    solution = Solution()
    #result = solution.findMaximizedCapital(3, 0, [0,2,1,5], [1,2,4,10])
    result = solution.findMaximizedCapital(1, 2, [1,1,2], [1,2,3])
    print("Total result is", result)



class NQueensSolution : 
    def solveNQueens(self, n) :
        if n < 1: return []
        # the final result, 2-deminsion array
        self.result = []
        # store column index
        self.cols = set()
        # store row+column 
        self.pie = set()
        # store row-column
        self.na = set()
        # start recursion
        self._DFS(n, 0, [])
        # generate the result strings
        result_print = self.generate_string(n)
        print(result_print)
    
    def _DFS(self, n, row, cur_col_index) :
        # break condidtion
        if row >= n:
            self.result.append(cur_col_index)
            return

        for col in range(n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                # die
                continue
            
            # add to the current die list
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)

            self._DFS(n, row+1, cur_col_index + [col])

            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def generate_string(self, n) :
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i: i+n] for i in range(0, len(board), n)]

if __name__ == "__main__":
    test = NQueensSolution()
    test.solveNQueens(5)




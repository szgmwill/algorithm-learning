import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class NQueenSolution {

    // result is like [["*Q**", "**Q*", "", ""],[]]
    private static List<List<String>> resultList = new ArrayList<List<String>>();

    // store the attach areas
    private static HashSet<Integer> columnSet = new HashSet<>();
    private static HashSet<Integer> pieSet = new HashSet<>();
    private static HashSet<Integer> naSet = new HashSet<>();


    public static void main(String[] args) {
        runNQueen(4);
    }
    
    // a bit example
    private static void runNQueen(int n) {
        
        // init the current the Qipan
        char[][] solution = new char[n][n];

        // init the result with 0 value
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                solution[i][j] = '*';
            }
        }

        DFS(0, n, solution);

        // print result
        printResult();

    }

    private static void DFS(int row, int n, char[][] solution) {
        // quit condition
        if (row >= n) {
            // store the current solution as string list
            List<String> curSolution = new ArrayList<>(n);
            for (int i = 0; i < row; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < solution[i].length; j++) {
                    sb.append(solution[i][j]);
                }
                curSolution.add(sb.toString());
            }
            // add to final result list
            resultList.add(curSolution);
            return;
        }

        for (int col = 0; col < n; col++) {
            // not in column set
            if (columnSet.contains(col)) {
                continue;
            }
            // not in pie set
            int calPie = row + col;
            if (pieSet.contains(calPie)) {
                continue;
            }
            // not in na set
            int calNa = row - col;
            if (naSet.contains(calNa)) {
                continue;
            }

            // select this one, and update the three set
            solution[row][col] = 'Q';

            columnSet.add(col);
            pieSet.add(calPie);
            naSet.add(calNa);

            // DFS
            // contiune resursion with next row
            DFS(row + 1, n, solution);

            //when track back to upper level, clean the selected
            solution[row][col] = '*';
            columnSet.remove(col);
            pieSet.remove(calPie);
            naSet.remove(calNa);

            //return and continue next column
        }

        
    }
    private static void printResult() {
        int row = 0;
        for (List<String> solution : resultList) {
            //solution.stream().forEach(n -> {System.out.print(n);});
            System.out.println(solution.toString());
        }
    }
}
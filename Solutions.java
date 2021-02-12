public class Solutions {
    
    public int findMaxStringsCount(String[] strings, int m, int n) {
        if (strings == null || strings.length == 0 || m < 0 || n < 0) {
            return 0;
        }

        int stringLen = strings.length;
        
        //define state
        int[][] dp = new int[m+1][n+1];

        // loop strings
        for (int i = 1; i <= stringLen; i++) {
            // count current string zero and one
            String curString = strings[i - 1];
            int curStrLen = curString.length();
            int zeroCount = countZeroStrings(curString); // start from 0
            int oneCount = curStrLen - zeroCount;

            // loop
            for (int zero = m; zero >= zeroCount; zero--) {
                for (int one = n; one >= oneCount; one--) {

                    dp[zero][one] = Math.max(dp[zero - zeroCount][one - oneCount] + 1, dp[zero][one]);
                }
            }
        }

        return dp[m][n];
    }

    public int countZeroStrings(String str) {
        char[] chars = str.toCharArray();
        int len = chars.length;
        int count = 0;
        while (len > 0) {
            if (chars[len - 1] == '0') {
                count++;
            }
            len--;
        }
        return count;
    }

    public int findMaxForm(String[] strs, int m, int n) {
        int M = m+1;
        int N = n+1;
        int[][][] dp = new int[strs.length+1][M][N]; // dp[插入/不插入第i个字符串][m个1][n个0] 组合最多的字符串数量
        for (int i=1;i<strs.length+1;i++) {
            String str = strs[i-1];
            int zeroCount = countZeroStrings(str);
            int oneCount = str.length()-zeroCount;
            for (int j = 0; j < M; j++) {
                for (int k = 0; k < N; k++) {
                    if(j >= zeroCount && k >= oneCount) {
                        dp[i][j][k] = Math.max(dp[i-1][j-zeroCount][k-oneCount]+1,dp[i][j][k]);
                    } else {
                        dp[i][j][k] = Math.max(dp[i-1][j][k],dp[i][j][k]);
                    }
                }
            }
        }
        return dp[strs.length][m][n];
    }

    public static void main(String[] args) {
        Solutions solutions = new Solutions();
        String[] testStringList = new String[3];
        testStringList[0] = "0";
        testStringList[1] = "00";
        testStringList[2] = "1";
        int maxZero = 1;
        int maxOne = 0;
        int result1 = solutions.findMaxStringsCount(testStringList, maxZero, maxOne);
        int result2 = solutions.findMaxForm(testStringList, maxZero, maxOne);

        System.out.println("Result1 is ==================: " + result1);
        System.out.println("Result2 is ==================: " + result2);
    }
}
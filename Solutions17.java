import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solutions17 {

    public static void main(String[] args) {
        String test1 = "23";
        String test2 = "";
        String test3 = "2";

        List<String> result3 = listCombinations(test3);
        System.out.println("===============result3: " + result3);
    }

    static List<String> listCombinations(String digits) {
        if (digits == null || digits.length() == 0) {
            return Collections.emptyList();
        }
        
        // store the phone number mapping
        Map<String, String> phoneNumMap = new HashMap<>();
        phoneNumMap.put("2", "abc");
        phoneNumMap.put("3", "def");
        phoneNumMap.put("4", "ghi");
        phoneNumMap.put("5", "jkl");
        phoneNumMap.put("6", "mno");
        phoneNumMap.put("7", "pqrs");
        phoneNumMap.put("8", "tuv");
        phoneNumMap.put("9", "wxyz");
        phoneNumMap.put("1", "");

        // store the selected result
        List<String> resultList = new ArrayList<>();

        String[] digitsList = digits.split("");

        // backtrack solution

        backtrack(0, new StringBuffer(), digitsList, resultList, phoneNumMap);

        return resultList;

    }
    // "23" -> "2", "3"
    static void backtrack(int index, StringBuffer temp, String[] digits, List<String> resultList, Map<String, String> phoneNumMap) {
        // end loop condition
        if (index == digits.length) {
            // add to result
            resultList.add(temp.toString());

            return;
        }

        // for select
        String digitalKey = digits[index];
        String[] selectOptions = phoneNumMap.get(digitalKey).split("");
        for (String curChar : selectOptions) {
            temp.append(curChar);
            // backtrack recurison
            backtrack(index + 1, temp, digits, resultList, phoneNumMap);

            // clean up selection
            temp.deleteCharAt(temp.length() - 1);
        }        
    }
}

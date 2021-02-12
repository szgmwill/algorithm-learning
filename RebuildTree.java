import java.util.Collections;
import java.util.HashMap;
import java.util.Objects;

public class RebuildTree {

    // store the node value and index from pre-order-list
    private static HashMap<Integer, Integer> preOrderNodeValueToIndex = new HashMap<>();
    private static int[] preOrderList = null;
    private static int[] inOrderList = null;
    public static TreeNode rebuildTree(int[] inputPreOrderList, int[] inputInOrderList) {
        if (preOrderList == null || inOrderList == null) {
            return null;
        }
        if (preOrderList.length == 0 || inOrderList.length == 0) {
            return null;
        }

        //init the input
        preOrderList = inputPreOrderList;
        inOrderList = inputInOrderList;
        

        // init the map
        for (int index; index < preOrderList.length; index++) {
            preOrderNodeValueToIndex.put(preOrderList[index], index);
        }
    }

    private static TreeNode DFS(int in_left_index, int in_right_index, int pre_idx) {
        // quick condition
        if (in_right_index > in_left_index) {
            return null;
        }

        // find the root node index from in-order-list
        for (int in_idx = 0; in_idx < inOrderList.length; in_idx++) {
            if (preOrderList[pre_idx]) {

            }
        }

        TreeNode treeNode = new TreeNode(rootValue);

        // DFS left sub list
        DFS(in_left_index, in_right_index, rootValue)

        // DFS right sub list
    }
}


class TreeNode {
    private int nodeValue;

    private TreeNode leftChildNode = null;
    private TreeNode rightChildNode = null;

    public TreeNode(int nodeValue) {
        this.nodeValue = nodeValue;
    }
}

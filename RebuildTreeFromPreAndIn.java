public class RebuildTreeFromPreAndIn {
    
    public TreeNode rebuildTree(int[] preOrderList, int[] inOrderList) {
        if (preOrderList == null || inOrderList == null) {
            return null;
        }
        if (preOrderList.length == 0 || inOrderList.length == 0) {
            return null;
        }
        
        return DFS(preOrderList, inOrderList);
    }

    private TreeNode DFS(int[] preorder, int[] inorder) {
        return null;
    }

    public static void main(String[] args) {
        int[] preOrderList = new int[]{3,9,20,15,7};
        int[] inOrderList = new int[]{9,3,15,20,7};

        RebuildTreeFromPreAndIn reBuild = new RebuildTreeFromPreAndIn();
        TreeNode root = reBuild.rebuildTree(preOrderList, inOrderList);

        System.out.println("========:" + root);
    }

}


class TreeNode {
    private int nodeValue;

    private TreeNode leftNode;
    private TreeNode rightNode;

    public TreeNode (int value, TreeNode left, TreeNode right) {
        this.nodeValue = value;
        this.leftNode = left;
        this.rightNode = right;
    }
} 

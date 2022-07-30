import java.util.*;



public class GreaterKeysBinarySearchTree {

    public static void main(String[] args) {
        int[] arr = new int[]{5, 3, 2, 8, 4, 6, 10};

        BST bst = new BST(arr);

        System.out.println("\nOriginal Tree:");
        bst.printTree();
        System.out.println("\nModified Tree:");
        bst.printModifiedTree();
        System.out.println();
    }
}



class BST {

    private Node root;


    BST() {
        root = null;
    }


    BST(int[] values) {
        this();
        for (int val : values) {
            add(val);
        }
    }



    BST(Node root) {
        this();
        ArrayList<ArrayList<Integer>> toBeCopied = levelOrderTraversal(root);
        for (ArrayList<Integer> level : toBeCopied) {
            for (Integer val : level) {
                add(val);
            }
        }
    }



    public void add(int val) {
        Node newNode = new Node(val);

        if (root == null) {
            root = newNode;
        }
        else {
            Node current = root;
            
            while (true) {

                if (val <= current.getVal()) {
                    if (current.getLeft() == null) {
                        current.setLeft(newNode);
                        return;
                    }
                    current = current.getLeft();
                }
                else {
                    if (current.getRight() == null) {
                        current.setRight(newNode);
                        return;
                    }
                    current = current.getRight();
                }
            }
        }
    }



    public void printModifiedTree() {
        ArrayList<Integer> sum = new ArrayList<>();
        sum.add(0);

        // create a copied tree so that the current tree is not modified
        BST copy = new BST(this.root);
        copy.addGreaterKeys(copy.root, sum);
        copy.printTree();
    }



    private void addGreaterKeys(Node root, ArrayList<Integer> sum) {
        if (root == null)
            return;

        addGreaterKeys(root.getRight(), sum);

        sum.set(0, sum.get(0) + root.getVal());
        root.setVal(sum.get(0));

        addGreaterKeys(root.getLeft(), sum);
    }



    public void printTree() {
        ArrayList<ArrayList<Integer>> tree = levelOrderTraversal(root);

        for (ArrayList<Integer> level : tree) {
            for (int val : level) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }



    public ArrayList<ArrayList<Integer>> levelOrderTraversal(Node root) {
        
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(root);

        ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();

        while (!queue.isEmpty()) {
            int size = queue.size();
            ArrayList<Integer> subarr = new ArrayList<Integer>();

            for (int i = 0; i < size; i++) {
                Node temp = queue.remove();
                subarr.add(temp.getVal());
                
                if (temp.getLeft() != null) {
                    queue.add(temp.getLeft());
                }
                if (temp.getRight() != null) {
                    queue.add(temp.getRight());
                }
            }
            arr.add(subarr);
        }
        return arr;
    }



    private class Node {
        private int val;
        private Node left;
        private Node right;
    
        Node(int val) {
            this(val, null, null);
        }
    
        Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    
        public void setVal(int val) {
            this.val = val;
        }
    
        public void setLeft(Node left) {
            this.left = left;
        }
    
        public void setRight(Node right) {
            this.right = right;
        }
    
        public int getVal() {
            return val;
        }
    
        public Node getLeft() {
            return left;
        }
    
        public Node getRight() {
            return right;
        }
    }
}









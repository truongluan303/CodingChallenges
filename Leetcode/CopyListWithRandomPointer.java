import java.util.HashMap;



class CopyListWithRandomPointer {
    
    public Node copyRandomList(Node head) {
        
        HashMap<Node, Node> map = new HashMap<>();
        
        Node cHead = new Node(0);
        Node current = head;
        Node cCurrent = cHead;
        
        while (current != null) {
            Node newNode = new Node(current.val);
            cCurrent.next = newNode;
            map.put(current, cCurrent.next);
            current = current.next;
            cCurrent = cCurrent.next;
        }
        
        cCurrent = cHead.next;
        current = head;
        
        while (current != null) {
            if (current.random == null) {
                cCurrent.random = null;
            }
            else {
                Node rand = map.get(current.random);
                cCurrent.random = rand;
            }
            current = current.next;
            cCurrent = cCurrent.next;
        }
        
        return cHead.next;
    }
}



class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
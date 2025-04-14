
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        long  first = convertFromList(l1);
        long  second = convertFromList(l2);
        
        first = first + second;
        ListNode results = convertToList(first);
        return convertToList(first);
    }

    public long  convertFromList(ListNode l1){
        long  result = 0;
        long  tens = 0;
        while( l1 != null){
            long  exp = (long ) Math.pow(10, tens);
            result = result + l1.val * exp;
            tens++;
            l1 = l1.next;
        }
        return result;
    }

    public ListNode convertToList(long  val){
        ListNode start = new ListNode(val % 10 );
        val = val - val % 10;
        val = val / 10;

        ListNode ptr = start;
        while( val > 0){
            ptr.next = new ListNode(val % 10);
            val = val - val % 10;
            val = val / 10;
            ptr = ptr.next;
        }
        return start;
    }


    public static void main(String[] args){
        Solution s = new Solution();
    
        ListNode l1 = new ListNode(9);
        
        ListNode l2 = new ListNode(1);
        l2.next = new ListNode(9);
        l2.next.next = new ListNode(9);
        l2.next.next.next = new ListNode(9);
        l2.next.next.next.next = new ListNode(9);
        l2.next.next.next.next.next = new ListNode(9);
        l2.next.next.next.next.next.next = new ListNode(9);
        l2.next.next.next.next.next.next.next = new ListNode(9);
        l2.next.next.next.next.next.next.next.next = new ListNode(9);
        l2.next.next.next.next.next.next.next.next.next = new ListNode(9);
        ListNode test = s.addTwoNumbers(l1, l2);
        System.out.println(s.convertFromList(test));
    }
}



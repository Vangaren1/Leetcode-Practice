/*
 * The java version and the python version differ because although the 
 * largest int in python is greater than a regular int in java, 
 * you don't notice because python makes no distinction between 
 * int and long, but java does.  This means the two pointer 
 * approach for java is better. 
 */


class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ptr1 = l1;
        ListNode ptr2 = l2;

        int main = 0;
        int carry = 0;

        while(ptr1 != null && ptr2 != null){
            main = ptr1.val + ptr2.val + carry;
            if(main > 9){
                carry = 1;
            }else{
                carry = 0;
            }
            main = main % 10;
            ptr1.val = main;
            ptr2.val = main;
            ptr1 = ptr1.next;
            ptr2 = ptr2.next;
        }

        if(ptr1 != null){
            while(ptr1 != null){
                main = ptr1.val + carry;
                if(main > 9){
                    carry = 1;
                }else{
                    carry = 0;
                }
                main = main % 10;
                ptr1.val = main;
                ptr1 = ptr1.next;
            }  
            if(carry == 1){
                ListNode lastPtr = l1;
                while(lastPtr.next != null){
                    lastPtr = lastPtr.next;
                }
                lastPtr.next = new ListNode(1);
            }
            return l1;            
        }

        while(ptr2 != null){
            main = ptr2.val + carry;
            if(main > 9){
                carry = 1;
            }else{
                carry = 0;
            }
            main = main % 10;
            ptr2.val = main;
            ptr2 = ptr2.next;
        }
        if(carry == 1){
            ListNode lastPtr = l2;
            while(lastPtr.next != null){
                lastPtr = lastPtr.next;
            }
            lastPtr.next = new ListNode(1);
        }
        return l2;
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
        while(test != null){
            System.out.println(test.val);
            test = test.next;
        }
        
    }
}



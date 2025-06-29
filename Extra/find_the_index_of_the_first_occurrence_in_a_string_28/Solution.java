package Extra.find_the_index_of_the_first_occurrence_in_a_string_28;

class Solution {

    public int strStr(String haystack, String needle) {
    
        int ptr1 = -1;
        int ptr2 = needle.length() -1;
        
        while ( ptr1 < haystack.length() &&  ptr2 < haystack.length() ) {
            ptr1++;
            ptr2++;

            String curr = haystack.substring(ptr1, ptr2);
            if (curr.compareTo(needle)== 0){
                return ptr1;
            }
        }

        return -1;

    }
    public static void main(String[] args) {
        System.out.println("Running find_the_index_of_the_first_occurrence_in_a_string_28...");
    }
}

package Grind75.week5.account_merge_721;

import java.util.*;

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        
        QuickUnion qu = new QuickUnion(accounts.size());

        Map<String, Integer> emailToAccount = new HashMap<>();

        for ( int index = 0; index < accounts.size(); index ++  ){
            List<String> acct = accounts.get(index);
            for ( int j = 1; j < acct.size(); j++){
                if ( emailToAccount.containsKey( acct.get(j))){
                    qu.union( index , emailToAccount.get(acct.get(j)));
                }else{
                    emailToAccount.put( acct.get(j), index);
                }
            }
        }

        
        Map<Integer, List<String>> newAcct = new HashMap<>();

        int leadAcct = 0;
        for (Map.Entry<String, Integer> entry : emailToAccount.entrySet()) {
            String email = entry.getKey();
            Integer index = entry.getValue();

            leadAcct = qu.root(index);
            
            boolean keyExists = newAcct.containsKey(leadAcct);

            if ( keyExists ){
                newAcct.get(leadAcct).add(email);
            }else{
                List<String> curr = new ArrayList<>();
                curr.add(email);
                newAcct.put(leadAcct, curr);
            }
        }

        List<List<String>> result = new ArrayList<>();

        for ( int acctnum : newAcct.keySet()){
            String name = accounts.get(acctnum).get(0);
            List<String> emails = newAcct.get(acctnum);
            Collections.sort(emails);
            emails.add(0, name);
            result.add(emails);
        }

        return result;

    }

    class QuickUnion{

        int[] id;

        public QuickUnion(int size){
            id = new int[size];
            for ( int i = 0; i < size; i++){
                id[i] = i;
            }
        }

        public int root(int index){
            while (index != id[index]){
                index = id[index];
            }
            return index;
        }

        public boolean connected(int p, int q){
            return root(p) == root(q);
        }

        public void union(int p, int q){
            int rootp = root(p);
            int rootq = root(q);
            id[rootp] = rootq;
        }
    }


    public static void main(String[] args) {
        System.out.println("Running account_merge_721...");
    }
}

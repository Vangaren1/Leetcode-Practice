#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> indexMap;
            for(int i= 0; i< nums.size(); i++){
                indexMap[nums[i]]=i;
            }

            for(int j = 0; j < nums.size(); j++){
                int curr = nums[j];
                int needed = target-curr;
                if(indexMap.count(needed) > 0 and indexMap[needed] != j){
                    return {j,indexMap[needed]};
                }
            }
            return {-1,-1};

        }
    };

int main() {
        Solution sol;
    
        vector<int> nums = {2, 7, 11, 15};
        int target = 9;
    
        vector<int> result = sol.twoSum(nums, target);
    
        cout << "Indices: ";
        for (int index : result) {
            cout << index << " ";
        }
        cout << endl;
    
        return 0;
    }
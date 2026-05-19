// Jump_Game_II.cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int n = nums.size()-1;
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        int curr= 0;
        int future = 0;
        for( int index = n-1; index > -1; index--){
            for( int j = 1; j < nums[index]+1; j++){
                if(index + j <= n){
                    curr = dp[index];
                    future = 1 + dp[index+j];
                    dp[index] = min(curr, future);
                }
            }
        }
        return dp[0];
    }
};

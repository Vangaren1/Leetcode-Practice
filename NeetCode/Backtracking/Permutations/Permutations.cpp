// Permutations.cpp
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
    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<vector<int>> results;

        if (nums.size() == 0)
        {
            return results;
        }

        if (nums.size() == 1)
        {
            results.push_back(nums);
            return results;
        }

        for (int index = 0; index < nums.size(); index++)
        {
            vector<int> arr = nums;
            int curr = arr[index];
            arr.erase(arr.begin() + index);
            vector<vector<int>> tmp = permute(arr);

            for (vector<int> sub : tmp)
            {
                sub.insert(sub.begin(), curr);
                results.push_back(sub);
            }
        }
        return results;
    }
};

int main()
{
    Solution sol;

    vector<int> n = {1, 2, 3};

    vector<vector<int>> r = sol.permute(n);

    for (vector<int> p : r)
    {
        for (int i : p)
        {
            cout << i << " ";
        }
        cout << "\n";
    }
}

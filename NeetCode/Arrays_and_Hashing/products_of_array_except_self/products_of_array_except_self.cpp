// products_of_array_except_self.cpp
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
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        int r = 1;
        vector<int> result(n, 1);

        for (int j = 1; j < n; j++)
        {
            result[j] = result[j - 1] * nums[j - 1];
        }
        for (int i = n - 1; i >= 0; i--)
        {
            result[i] = result[i] * r;
            r *= nums[i];
        }

        return result;
    }
};

int main()
{
    Solution sol;

    vector<int> test = {1, 2, 3, 4};

    vector<int> result = sol.productExceptSelf(test);

    for (int n : result)
    {
        cout << n << " ";
    }
    cout << endl;

    return 0;
}

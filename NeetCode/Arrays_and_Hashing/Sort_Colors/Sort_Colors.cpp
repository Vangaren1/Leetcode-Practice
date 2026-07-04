// Sort_Colors.cpp
//
// Compile locally with:
// clang++ Sort_Colors.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
//
// NOTE:
// - Remove main() before submitting to LeetCode.
// - Keep only the class Solution definition.
//

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
    void sortColors(vector<int> &nums)
    {
        vector<int> count = {0, 0, 0};
        for (auto &num : nums)
        {
            count[num]++;
        }
        int ptr = 0;
        for (int i = 0; i < 3; i++)
        {
            while (count[i])
            {
                nums[ptr] = i;
                count[i]--;
                ptr++;
            }
        }
    }
};

int main()
{
    cout << "Running Sort_Colors.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

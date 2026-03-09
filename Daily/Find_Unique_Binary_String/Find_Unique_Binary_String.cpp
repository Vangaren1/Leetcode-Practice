// Find_Unique_Binary_String.cpp
//
// Compile locally with:
// clang++ Find_Unique_Binary_String.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    string findDifferentBinaryString(vector<string> &nums)
    {
        string result = "";

        for (int index = 0; index < nums.size(); index++)
        {
            result += (nums[index][index] == '0' ? '1' : '0');
        }
        return result;
    }
};

int main()
{
    cout << "Running Find_Unique_Binary_String.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

// Check_If_Binary_String_Has_At_Most_One_Segment_Of_Ones.cpp
//
// Compile locally with:
// clang++ Check_If_Binary_String_Has_At_Most_One_Segment_Of_Ones.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool checkOnesSegment(string s)
    {
        bool segFinished = false;
        for (char ch : s)
        {
            if (ch == '0')
            {
                segFinished = true;
                continue;
            }
            if (segFinished)
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    cout << "Running Check_If_Binary_String_Has_At_Most_One_Segment_Of_Ones.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

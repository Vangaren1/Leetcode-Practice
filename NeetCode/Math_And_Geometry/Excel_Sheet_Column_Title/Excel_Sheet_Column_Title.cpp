// Excel_Sheet_Column_Title.cpp
//
// Compile locally with:
// clang++ Excel_Sheet_Column_Title.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    string convertToTitle(int columnNumber)
    {
        string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string results = "";
        int m = 0;
        while (columnNumber)
        {
            columnNumber--;
            m = columnNumber % 26;
            results += letters[m];
            columnNumber -= m;
            columnNumber = columnNumber / 26;
        }
        reverse(results.begin(), results.end());
        return results;
    }
};

int main()
{
    cout << "Running Excel_Sheet_Column_Title.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

// N_Queens_II.cpp
//
// Compile locally with:
// clang++ N_Queens_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
private:
    int count, rows;
    unordered_set<int> columns;
    unordered_set<int> posDiag;
    unordered_set<int> negDiag;

public:
    int totalNQueens(int n)
    {
        count = 0;
        rows = n;
        backtrack(0);
        return count;
    }
    void backtrack(int row)
    {
        if (row == rows)
        {
            count++;
            return;
        }
        for (int col = 0; col < rows; col++)
        {
            if (columns.count(col) || posDiag.count(row - col) || negDiag.count(row + col))
            {
                continue;
            }

            columns.insert(col);
            posDiag.insert(row - col);
            negDiag.insert(row + col);

            backtrack(row + 1);

            columns.erase(col);
            posDiag.erase(row - col);
            negDiag.erase(row + col);
        }
    }
};

int main()
{
    cout << "Running N_Queens_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

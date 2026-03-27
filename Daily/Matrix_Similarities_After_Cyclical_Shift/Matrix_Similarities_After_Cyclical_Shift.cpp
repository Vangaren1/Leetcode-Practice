// Matrix_Similarities_After_Cyclical_Shift.cpp
//
// Compile locally with:
// clang++ Matrix_Similarities_After_Cyclical_Shift.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool areSimilar(vector<vector<int>> &mat, int k)
    {
        int n = mat[0].size();

        for (vector<int> row : mat)
        {
            for (int idx = 0; idx < n; idx++)
            {
                if (row[idx] != row[(k + idx) % n])
                {
                    return false;
                }
            }
        }
        return true;
    }
};

int main()
{
    cout << "Running Matrix_Similarities_After_Cyclical_Shift.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

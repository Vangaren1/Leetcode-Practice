// Special_Position_In_Binary_Matrix.cpp
//
// Compile locally with:
// clang++ Special_Position_In_Binary_Matrix.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int numSpecial(vector<vector<int>> &mat)
    {
        int height = mat.size();
        int width = mat[0].size();
        int total = 0;
        vector<int> rowSum(height, 0);
        vector<int> colSum(width, 0);

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (mat[y][x] == 1)
                {
                    rowSum[y]++;
                    colSum[x]++;
                }
            }
        }

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (mat[y][x] == 1 && rowSum[y] == 1 && colSum[x] == 1)
                {
                    total++;
                }
            }
        }
        return total;
    }
};

int main()
{
    cout << "Running Special_Position_In_Binary_Matrix.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

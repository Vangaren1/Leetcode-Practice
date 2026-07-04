// Range_Sum_Query_2D_Immutable.cpp
//
// Compile locally with:
// clang++ Range_Sum_Query_2D_Immutable.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class NumMatrix
{
private:
    vector<vector<int>> sumMatrix;
    int height;
    int width;

public:
    NumMatrix(vector<vector<int>> &matrix)
    {
        height = matrix.size();
        width = matrix[0].size();
        sumMatrix = vector<vector<int>>(height + 1, vector<int>(width + 1, 0));
        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                sumMatrix[y + 1][x + 1] = matrix[y][x] + sumMatrix[y][x + 1] + sumMatrix[y + 1][x] - sumMatrix[y][x];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2)
    {
        return sumMatrix[row2 + 1][col2 + 1] - sumMatrix[row2 + 1][col1] - sumMatrix[row1][col2 + 1] + sumMatrix[row1][col1];
    }
};

int main()
{
    cout << "Running Range_Sum_Query_2D_Immutable.cpp..." << endl;

    // TODO:
    // Add local test calls here

    return 0;
}

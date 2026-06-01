// Set_Matrix_Zeros.cpp
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
    void setZeroes(vector<vector<int>> &matrix)
    {
        vector<pair<int, int>> found;

        for (int y = 0; y < matrix.size(); y++)
        {
            for (int x = 0; x < matrix[0].size(); x++)
            {
                if (matrix[y][x] == 0)
                {
                    found.push_back({y, x});
                }
            }
        }
        for (pair<int, int> coord : found)
        {
            func(matrix, coord.first, coord.second);
        }
    }
    void func(vector<vector<int>> &matrix, int row, int col)
    {
        matrix[row] = vector<int>(matrix[0].size(), 0);
        for (int r = 0; r < matrix.size(); r++)
        {
            matrix[r][col] = 0;
        }
    }
};

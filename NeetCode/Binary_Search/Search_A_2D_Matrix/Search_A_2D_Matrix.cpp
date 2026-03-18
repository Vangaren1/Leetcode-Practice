// Search_A_2D_Matrix.cpp
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
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int left{0}, mid{0}, tmp{0};
        int right = matrix.size() * matrix[0].size();

        while (left < right)
        {
            mid = (left + right) / 2;
            tmp = matrix[mid / matrix[0].size()][mid % matrix[0].size()];
            if (tmp == target)
            {
                return true;
            }
            else if (tmp > target)
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }

        return false;
    }
};

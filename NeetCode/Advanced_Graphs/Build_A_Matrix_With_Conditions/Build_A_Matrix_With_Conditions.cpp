// Build_A_Matrix_With_Conditions.cpp
//
// Compile locally with:
// clang++ Build_A_Matrix_With_Conditions.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    unordered_set<int> visitedRow, visitedCol, pathRow, pathCol;
    unordered_map<int, vector<int>> rowMap, colMap;
    vector<int> rowOrder, colOrder;

public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>> &rowConditions, vector<vector<int>> &colConditions)
    {
        vector<vector<int>> result(k, vector<int>(k, 0));

        for (auto &tmp : rowConditions)
        {
            rowMap[tmp[0]].push_back(tmp[1]);
        }
        for (auto &tmp2 : colConditions)
        {
            colMap[tmp2[0]].push_back(tmp2[1]);
        }

        for (int i = 1; i <= k; i++)
        {
            if (!dfs(i, true))
            {
                return {};
            }
            if (!dfs(i, false))
            {
                return {};
            }
        }
        reverse(rowOrder.begin(), rowOrder.end());
        reverse(colOrder.begin(), colOrder.end());

        for (int index = 0; index < k; index++)
        {
            int yVal = rowOrder[index];
            auto xiter = find(colOrder.begin(), colOrder.end(), yVal);
            int x = xiter - colOrder.begin();
            result[index][x] = rowOrder[index];
        }
        return result;
    }

    bool dfs(int node, bool rowOrCol)
    {
        unordered_map<int, vector<int>> &map = rowOrCol ? rowMap : colMap;
        unordered_set<int> &path = rowOrCol ? pathRow : pathCol;
        unordered_set<int> &visited = rowOrCol ? visitedRow : visitedCol;
        vector<int> &order = rowOrCol ? rowOrder : colOrder;

        if (path.count(node))
        {
            return false;
        }
        if (visited.count(node))
        {
            return true;
        }
        path.insert(node);

        for (auto &child : map[node])
        {
            if (!dfs(child, rowOrCol))
            {
                return false;
            }
        }
        path.erase(node);
        visited.insert(node);
        order.push_back(node);
        return true;
    }
};

int main()
{
    cout << "Running Build_A_Matrix_With_Conditions.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

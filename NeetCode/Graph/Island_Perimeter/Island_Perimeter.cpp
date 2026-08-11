// Island_Perimeter.cpp
//
// Compile locally with:
// clang++ Island_Perimeter.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int islandPerimeter(vector<vector<int>> &grid)
    {
        int height = grid.size();
        int width = grid[0].size();

        int perimeter = 0;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] == 0)
                {
                    continue;
                }
                perimeter += 4;
                if (y > 0 && grid[y - 1][x] == 1)
                {
                    perimeter = perimeter - 2;
                }
                if (x > 0 && grid[y][x - 1] == 1)
                {
                    perimeter = perimeter - 2;
                }
            }
        }
        return perimeter;
    }
};

int main()
{
    cout << "Running Island_Perimeter.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

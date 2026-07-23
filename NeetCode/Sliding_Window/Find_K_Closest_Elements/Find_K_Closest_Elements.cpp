// Find_K_Closest_Elements.cpp
//
// Compile locally with:
// clang++ Find_K_Closest_Elements.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> findClosestElements(vector<int> &arr, int k, int x)
    {
        int left(0), mid(0);
        int right = arr.size() - k;

        while (left < right)
        {
            mid = left + (right - left) / 2;

            if (x - arr[mid] > arr[mid + k] - x)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};

int main()
{
    cout << "Running Find_K_Closest_Elements.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

// Sort_An_Array.cpp
//
// Compile locally with:
// clang++ Sort_An_Array.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> sortArray(vector<int> &nums)
    {
        return mergeSort(nums);
    }
    vector<int> mergeSort(vector<int> &arr)
    {
        if (arr.size() <= 1)
        {
            return arr;
        }
        int mid = arr.size() / 2;
        vector<int> left(arr.begin(), arr.begin() + mid);
        vector<int> right(arr.begin() + mid, arr.end());
        left = mergeSort(left);
        right = mergeSort(right);
        return merge(left, right);
    }
    vector<int> merge(vector<int> &left, vector<int> &right)
    {
        vector<int> result;
        int i(0), j(0);
        while (i < left.size() && j < right.size())
        {
            if (left[i] <= right[j])
            {
                result.push_back(left[i]);
                i++;
            }
            else
            {
                result.push_back(right[j]);
                j++;
            }
        }

        while (i < left.size())
        {
            result.push_back(left[i]);
            i++;
        }

        while (j < right.size())
        {
            result.push_back(right[j]);
            j++;
        }

        return result;
    }
};

int main()
{
    cout << "Running Sort_An_Array.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

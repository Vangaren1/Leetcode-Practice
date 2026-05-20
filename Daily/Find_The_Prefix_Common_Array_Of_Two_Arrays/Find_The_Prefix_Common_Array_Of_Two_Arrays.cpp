// Find_The_Prefix_Common_Array_Of_Two_Arrays.cpp
//
// Compile locally with:
// clang++ Find_The_Prefix_Common_Array_Of_Two_Arrays.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> findThePrefixCommonArray(vector<int> &A, vector<int> &B)
    {
        int n = A.size();
        vector<int> count(n + 1, 0);
        int total = 0;
        vector<int> results;
        for (int i = 0; i < n; i++)
        {
            count[A[i]]++;
            if (count[A[i]] == 2)
            {
                total++;
            }
            count[B[i]]++;
            if (count[B[i]] == 2)
            {
                total++;
            }

            results.push_back(total);
        }
        return results;
    }
};

int main()
{
    cout << "Running Find_The_Prefix_Common_Array_Of_Two_Arrays.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

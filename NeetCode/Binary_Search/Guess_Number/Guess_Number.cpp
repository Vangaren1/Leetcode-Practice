// Guess_Number.cpp
//
// Compile locally with:
// clang++ Guess_Number.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int guessNumber(int n)
    {
        int left(0), right(n), mid(0), g(0);
        while (left < right)
        {
            mid = (left + right) / 2;
            g = guess(mid);
            if (g == 0)
            {
                return mid;
            }
            if (g == -1)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        return left;
    }
};

int main()
{
    cout << "Running Guess_Number.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

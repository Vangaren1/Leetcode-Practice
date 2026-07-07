// Concatenate_Nonzero_digits_And_Multiple_By_Sum.cpp
//
// Compile locally with:
// clang++ Concatenate_Nonzero_digits_And_Multiple_By_Sum.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    long long sumAndMultiply(int n)
    {
        int place(1);
        int digit_sum(0);
        int x(0);
        int tmp(0);
        while (n != 0)
        {
            tmp = n % 10;
            if (tmp != 0)
            {
                digit_sum += tmp;
                x += tmp * place;
                place *= 10;
            }
            n /= 10;
        }
        return digit_sum * x;
    }
};

int main()
{
    cout << "Running Concatenate_Nonzero_digits_And_Multiple_By_Sum.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

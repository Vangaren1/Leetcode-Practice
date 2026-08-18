// Lemonade_Change.cpp
//
// Compile locally with:
// clang++ Lemonade_Change.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool lemonadeChange(vector<int> &bills)
    {
        int fives(0), tens(0);

        for (auto bill : bills)
        {
            switch (bill)
            {
            case 5:
                fives++;
                break;
            case 10:
                if (fives == 0)
                {
                    return false;
                }
                fives--;
                tens++;
                break;
            case 20:
                if (fives == 0)
                {
                    return false;
                }
                if (tens == 0)
                {
                    if (fives < 3)
                    {
                        return false;
                    }
                    fives -= 3;
                    break;
                }
                if (fives == 0)
                {
                    return false;
                }
                tens--;
                fives--;
                break;
            }
        }
        return true;
    }
};

int main()
{
    cout << "Running Lemonade_Change.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

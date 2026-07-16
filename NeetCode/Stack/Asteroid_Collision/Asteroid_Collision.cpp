// Asteroid_Collision.cpp
//
// Compile locally with:
// clang++ Asteroid_Collision.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> asteroidCollision(vector<int> &asteroids)
    {
        vector<int> stk;
        for (auto &asteroid : asteroids)
        {
            bool alive = true;
            while (alive && !stk.empty() && stk.back() > 0 && asteroid < 0)
            {
                if (stk.back() < -asteroid)
                {
                    stk.pop_back();
                }
                else if (stk.back() == -asteroid)
                {
                    stk.pop_back();
                    alive = false;
                }
                else
                {
                    alive = false;
                }
            }
            if (alive)
            {
                stk.push_back(asteroid);
            }
        }
        return stk;
    }
};

int main()
{
    cout << "Running Asteroid_Collision.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

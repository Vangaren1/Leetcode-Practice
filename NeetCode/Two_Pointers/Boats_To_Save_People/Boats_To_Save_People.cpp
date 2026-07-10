// Boats_To_Save_People.cpp
//
// Compile locally with:
// clang++ Boats_To_Save_People.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int numRescueBoats(vector<int> &people, int limit)
    {
        sort(people.begin(), people.end());
        int boatCount(0), left(0), right((int)people.size());
        while (left <= right)
        {
            if (people[left] + people[right] <= limit)
            {
                left++;
            }
            right--;
            boatCount++;
        }
        return boatCount;
    }
};

int main()
{
    cout << "Running Boats_To_Save_People.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

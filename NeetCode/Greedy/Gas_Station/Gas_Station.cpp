// Gas_Station.cpp
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
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        int totalCost = accumulate(cost.begin(), cost.end(), 0);
        int totalGas = accumulate(gas.begin(), gas.end(), 0);
        if (totalGas < totalCost)
        {
            return -1;
        }

        int start(0);
        totalGas = 0;
        for (int index = 0; index < gas.size(); index++)
        {
            totalGas = totalGas + gas[index] - cost[index];
            if (totalGas < 0)
            {
                totalGas = 0;
                start = index + 1;
            }
        }
        return start;
    }
};

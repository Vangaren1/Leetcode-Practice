// K_Closest_Points_To_Origin.cpp
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
    vector<vector<int>> kClosest(vector<vector<int>> &points, int k)
    {
        priority_queue<pair<int, vector<int>>> distList;
        for (const vector<int> &point : points)
        {
            int dist = point[0] * point[0] + point[1] * point[1];
            pair<int, vector<int>> tmp = {dist, point};
            distList.push(tmp);
            if (distList.size() > k)
            {
                distList.pop();
            }
        }

        vector<vector<int>> results;
        while (!distList.empty())
        {
            results.push_back(distList.top().second);
            distList.pop();
        }
        return results;
    }
};

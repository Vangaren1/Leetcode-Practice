// top_k_frequent_elements.cpp
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
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> freq;
        for (const int &num : nums)
        {
            freq[num]++;
        }
        priority_queue<pair<int, int>> pq;
        for (const auto &[key, value] : freq)
        {
            pq.push({value, key});
        }
        vector<int> results;
        for (int i = 0; i < k; i++)
        {
            pair<int, int> tmp = pq.top();
            pq.pop();
            results.push_back(tmp.second);
        }
        return results;
    }
};

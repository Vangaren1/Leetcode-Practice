// LFU_Cache.cpp
//
// Compile locally with:
// clang++ LFU_Cache.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class LFUCache
{
private:
    unordered_map<int, int> keyVal;
    unordered_map<int, int> count;
    unordered_map<int, list<int>> freq;
    unordered_map<int, list<int>::iterator> keyIter;
    int least;
    int cap;

public:
    LFUCache(int capacity)
    {
        cap = capacity;
        least = 0;
    }

    int get(int key)
    {
        if (!keyVal.count(key))
        {
            return -1;
        }
        _increaseFreq(key);
        return keyVal[key];
    }

    void put(int key, int value)
    {
        if (cap == 0)
        {
            return;
        }
        if (keyVal.count(key))
        {
            _increaseFreq(key);
            keyVal[key] = value;
            return;
        }
        if (keyVal.size() == cap)
        {
            // erase the least frequently used.
            int leastKey = freq[least].front();
            freq[least].pop_front();
            keyVal.erase(leastKey);
            count.erase(leastKey);
            keyIter.erase(leastKey);
        }

        keyVal[key] = value;
        count[key] = 0;
        keyIter[key] = freq[0].insert(freq[0].end(), key);
        least = 0;
    }

    void _increaseFreq(int key)
    {
        int curr = count[key];
        count[key]++;
        freq[curr].erase(keyIter[key]);
        freq[curr + 1].push_back(key);
        keyIter[key] = prev(freq[curr + 1].end());
        if (curr == least && freq[curr].empty())
        {
            least++;
        }
    }
};

int main()
{
    cout << "Running LFU_Cache.cpp..." << endl;

    LFUCache sol(2);

    // TODO:
    // Add local test calls here

    return 0;
}

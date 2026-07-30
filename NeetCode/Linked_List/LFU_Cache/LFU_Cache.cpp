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
    int least = 0;
    int cap;

public:
    LFUCache(int capacity)
    {
        cap = capacity;
    }

    int get(int key)
    {
    }

    void put(int key, int value)
    {
    }

    void _increaseFreq(int key)
    {
        int f = count[key];
        freq[f].erase(keyIter[key]);
        freq[f + 1].push_back(key);
        keyIter[key] = prev(freq[f + 1].end());
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

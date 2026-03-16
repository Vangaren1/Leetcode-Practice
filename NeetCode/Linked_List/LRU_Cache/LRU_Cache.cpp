// LRU_Cache.cpp
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
class LRUCache
{
private:
    int capacity;
    list<pair<int, int>> cache;
    unordered_map<int, list<pair<int, int>>::iterator> dict;

public:
    LRUCache(int capacity) : capacity(capacity) {}

    int get(int key)
    {
        auto found = dict.find(key);
        if (found == dict.end())
        {
            return -1;
        }

        auto iter = found->second;
        cache.splice(cache.begin(), cache, iter);
        return iter->second;
    }

    void put(int key, int value)
    {
        if (capacity == 0)
            return;

        auto found = dict.find(key);

        if (found != dict.end())
        {
            auto iter = found->second;
            iter->second = value;
            cache.splice(cache.begin(), cache, iter);
            return;
        }

        if ((int)cache.size() == capacity)
        {
            int lruKey = cache.back().first;
            dict.erase(lruKey);
            cache.pop_back();
        }

        cache.push_front({key, value});
        dict[key] = cache.begin();
    }
};
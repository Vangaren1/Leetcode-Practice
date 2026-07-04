// Design_Hashmap.cpp
//
// Compile locally with:
// clang++ Design_Hashmap.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class MyHashMap
{
private:
    vector<int> mymap = vector<int>(10000000, -1);

public:
    MyHashMap()
    {
    }

    void put(int key, int value)
    {
        mymap[key] = value;
    }

    int get(int key)
    {
        return mymap[key];
    }

    void remove(int key)
    {
        mymap[key] = -1;
    }
};

int main()
{
    cout << "Running Design_Hashmap.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

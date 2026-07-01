// Design_Hashset.cpp
//
// Compile locally with:
// clang++ Design_Hashset.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class MyHashSet
{
private:
    vector<bool> myhash = vector<bool>(100000, false);

public:
    MyHashSet()
    {
    }

    void add(int key)
    {
        myhash[key] = true;
    }

    void remove(int key)
    {
        myhash[key] = false;
    }

    bool contains(int key)
    {
        return myhash[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */

int main()
{
    cout << "Running Design_Hashset.cpp..." << endl;

    MyHashSet sol;

    // TODO:
    // Add local test calls here

    return 0;
}

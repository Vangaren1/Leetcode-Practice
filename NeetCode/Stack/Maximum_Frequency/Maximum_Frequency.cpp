// Maximum_Frequency.cpp
//
// Compile locally with:
// clang++ Maximum_Frequency.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class FreqStack
{
private:
    unordered_map<int, int> freq;
    unordered_map<int, vector<int>> groups;
    int maxFreq;

public:
    FreqStack()
    {
        maxFreq = 0;
    }

    void push(int val)
    {
        freq[val]++;
        groups[freq[val]].push_back(val);
        maxFreq = max(maxFreq, freq[val]);
    }

    int pop()
    {
        int val = groups[maxFreq].back();
        groups[maxFreq].pop_back();
        freq[val]--;
        if (groups[maxFreq].size() == 0)
        {
            maxFreq--;
        }
        return val;
    }
};

int main()
{
    cout << "Running Maximum_Frequency.cpp..." << endl;

    FreqStack sol;

    // TODO:
    // Add local test calls here

    return 0;
}

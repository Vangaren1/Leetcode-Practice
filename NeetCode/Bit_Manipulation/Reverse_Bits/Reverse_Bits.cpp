// Reverse_Bits.cpp
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
    int reverseBits(int n)
    {
        int r = 0;
        for (int i = 0; i < 32; i++)
        {
            r = r << 1;
            r |= (n & 1);
            n = n >> 1;
        }
        return r;
    }
};

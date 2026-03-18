// Fancy_Sequence.cpp
//
// Compile locally with:
// clang++ Fancy_Sequence.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class Fancy
{
private:
    long long addAcc;
    long long multi;
    vector<long long> values;
    const long long MOD = 1000000007;

    long long modPow(long long base, long long exp, long long mod)
    {
        long long result = 1;

        while (exp > 0)
        {
            if (exp % 2)
                result = (result * base) % mod;

            base = (base * base) % mod;
            exp /= 2;
        }

        return result;
    }

public:
    Fancy() : addAcc(0), multi(1)
    {
    }

    void append(int val)
    {
        long long normalized = ((val - addAcc + MOD) % MOD) * modPow(multi, MOD - 2, MOD) % MOD;
        values.push_back(normalized);
    }

    void addAll(int inc)
    {
        addAcc = (addAcc + inc) % MOD;
    }

    void multAll(int m)
    {
        addAcc = (addAcc * m) % MOD;
        multi = (multi * m) % MOD;
    }

    int getIndex(int idx)
    {
        if (idx >= values.size())
        {
            return -1;
        }
        return (values[idx] * multi + addAcc) % MOD;
    }
};

int main()
{
    cout << "Running Fancy_Sequence.cpp..." << endl;

    Fancy sol;

    // TODO:
    // Add local test calls here

    return 0;
}

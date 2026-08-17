// Add_Binary.cpp
//
// Compile locally with:
// clang++ Add_Binary.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class Solution
{
public:
    string addBinary(string a, string b)
    {
        int aptr(a.size() - 1), bptr(b.size() - 1), total(0), carry(0), abit(0), bbit(0);

        vector<char> result;

        while (aptr >= 0 || bptr >= 0 || carry > 0)
        {
            if (aptr >= 0)
            {
                abit = a[aptr] - '0';
            }
            else
            {
                abit = 0;
            }
            if (bptr >= 0)
            {
                bbit = b[bptr] - '0';
            }
            else
            {
                bbit = 0;
            }

            total = abit ^ bbit ^ carry;
            carry = (abit & bbit) | (carry & (abit ^ bbit));
            result.push_back('0' + total);
            aptr--;
            bptr--;
        }
        string resultStr = "";
        for (int i = result.size() - 1; i >= 0; i--)
        {
            resultStr += result[i];
        }
        return resultStr;
    }
};

int main()
{
    cout << "Running Add_Binary.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

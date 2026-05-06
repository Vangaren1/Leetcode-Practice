// Within_Two_Edits_Of_Dictionary.cpp
//
// Compile locally with:
// clang++ Within_Two_Edits_Of_Dictionary.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<string> twoEditWords(vector<string> &queries, vector<string> &dictionary)
    {
        vector<string> results;
        int n = queries[0].size();
        int diff = 0;
        for (string q : queries)
        {
            for (string word : dictionary)
            {
                diff = 0;
                for (int index = 0; index < n; index++)
                {
                    if (q[index] != word[index])
                    {
                        diff++;
                        if (diff > 2)
                        {
                            break;
                        }
                    }
                }
                if (diff <= 2)
                {
                    results.push_back(q);
                    break;
                }
            }
        }
        return results;
    }
};

int main()
{
    cout << "Running Within_Two_Edits_Of_Dictionary.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

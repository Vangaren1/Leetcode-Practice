// Longest_Repeating_Character_Replacement.cpp
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
    int characterReplacement(string s, int k)
    {
        vector<int> charCount(26, 0);
        int left{0}, right{0}, maxLen{0}, maxFreq{0};
        int n = s.size();

        while (right < n)
        {
            maxFreq = max(maxFreq, ++charCount[s[right] - 'A']);
            if (right - left + 1 - maxFreq > k)
            {
                charCount[s[left] - 'A']--;
                left++;
            }
            maxLen = max(maxLen, right - left + 1);
            right++;
        }
        return maxLen;
    }
};

/*


Works, but the priority queue is inefficient

class Solution
{
public:
    int characterReplacement(string s, int k)
    {
        unordered_map<char, int> charCount;
        priority_queue<pair<int, char>> freq;

        int maxLen{0}, currLen{0}, mostFreq{0}, left{0}, right{0};

        for (char ch : s)
        {
            charCount[ch]++;
            freq.push({charCount[ch], ch});

            currLen = right - left + 1;
            mostFreq = freq.top().first;
            while (currLen > (mostFreq + k))
            {

                charCount[s[left]]--;
                freq.push({charCount[s[left]], s[left]});
                left++;

                while (!freq.empty() && freq.top().first != charCount[freq.top().second])
                {
                    freq.pop();
                }

                currLen = right - left + 1;
                mostFreq = freq.top().first;
            }

            maxLen = max(maxLen, currLen);

            right++;
        }
        return maxLen;
    }
};

*/
// Two_Sum.cpp
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
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int left = 0;
        int right = numbers.size() - 1;
        int currSum = numbers[left] + numbers[right];
        while (currSum != target)
        {
            if (currSum < target)
            {
                left++;
            }
            else
            {
                right--;
            }
            currSum = numbers[left] + numbers[right];
        }
        return {left + 1, right + 1};
    }
};

// Meeting_Rooms.cpp
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
class Interval
{
public:
    int start, end;
    Interval(int start, int end)
    {
        this->start = start;
        this->end = end;
    }
};

class Solution
{
public:
    bool canAttendMeetings(vector<Interval> &intervals)
    {
        sort(intervals.begin(), intervals.end(),
             [](const Interval &a, const Interval &b)
             {
                 return a.start < b.start;
             });
        for (int index = 0; index < intervals.size() - 1; index++)
        {
            if (intervals[index].end > intervals[index + 1].start)
            {
                return false;
            }
        }
        return true;
    }
};

/*
leetcode is different because there they use vector<vector<int>> instead of interval

class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        if(intervals.size()==0){
            return true;
        }
        sort(intervals.begin(), intervals.end(),
     [](const vector<int>& a, const vector<int>& b) {
         return a[0] < b[0];
     });
        for (int index = 0; index < intervals.size() - 1; index++)
        {
            if(intervals[index][1]> intervals[index+1][0]){
                return false;
            }
        }
        return true;
    }
};
*/

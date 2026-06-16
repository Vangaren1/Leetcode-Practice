// Meeting_Rooms_II.cpp
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
    int minMeetingRooms(vector<vector<int>> &intervals)
    {
        {
            if (intervals.size() == 0)
            {
                return 0;
            }
            vector<vector<int>> startTimes(intervals);
            vector<vector<int>> endTimes(intervals);
            sort(startTimes.begin(), startTimes.end(), [](const vector<int> &a, const vector<int> &b)
                 { return a[0] < b[0]; });
            sort(endTimes.begin(), endTimes.end(), [](const vector<int> &a, const vector<int> &b)
                 { return a[1] < b[1]; });

            int sPtr(0), ePtr(0), count(0), maxCount(0);

            while (sPtr < intervals.size() && ePtr < intervals.size())
            {
                if (startTimes[sPtr][0] < endTimes[ePtr][1])
                {
                    sPtr++;
                    count++;
                }
                else
                {
                    ePtr++;
                    count--;
                }
                maxCount = max(maxCount, count);
            }
            return maxCount;
        }
    }
};

/*
class Solution
{
public:
    int minMeetingRooms(vector<Interval> &intervals)
    {
        if(intervals.size() == 0){
            return 0;
        }
        vector<Interval> startTimes(intervals);
        vector<Interval> endTimes(intervals);
        sort(startTimes.begin(), startTimes.end(), [](const Interval &a, const Interval &b){
            return a.start < b.start;
        });
        sort(endTimes.begin(), endTimes.end(), [](const Interval &a, const Interval &b){
            return a.end < b.end;
        });

        int sPtr(0), ePtr(0), count(0), maxCount(0);

        while( sPtr < intervals.size() && ePtr < intervals.size()){
            if(startTimes[sPtr].start < endTimes[ePtr].end){
                sPtr++;
                count++;
            }else{
                ePtr++;
                count--;
            }
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }
};

*/
// Median_Finder.cpp
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

class MedianFinder
{
private:
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int count;

public:
    MedianFinder()
    {
        count = 0;
    }

    void addNum(int num)
    {
        count++;
        if (maxHeap.empty())
        {
            maxHeap.push(num);
        }
        else
        {
            if (maxHeap.top() > num)
            {
                maxHeap.push(num);
            }
            else
            {
                minHeap.push(num);
            }
        }

        if (maxHeap.size() > minHeap.size() + 1)
        {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        }

        if (maxHeap.size() < minHeap.size())
        {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian()
    {
        if (count % 2 == 1)
        {
            return maxHeap.top();
        }
        return (maxHeap.top() / 2.0) + (minHeap.top() / 2.0);
    }
};

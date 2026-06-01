// Detect_Squares.cpp
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

class CountSquares
{
private:
    struct PairHash
    {
        size_t operator()(const pair<int, int> &p) const
        {
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };

    unordered_map<pair<int, int>, int, PairHash> ptCount;
    vector<pair<int, int>> points;

public:
    CountSquares()
    {
    }

    void add(vector<int> point)
    {
        pair<int, int> pt = {point[0], point[1]};
        ptCount[pt]++;
        points.push_back(pt);
    }

    int count(vector<int> point)
    {
        int result = 0;
        int py = point[1];
        int px = point[0];
        for (pair<int, int> xy : points)
        {
            int x = xy.first;
            int y = xy.second;
            if (abs(py - y) != abs(px - x) || x == px || y == py)
            {
                continue;
            }
            result = result + ptCount[{x, py}] * ptCount[{px, y}];
        }
        return result;
    }
};

// Number_Of_Connected_Components_In_Undirected_Graph.cpp
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

class QUFind
{
private:
    vector<int> arr;

public:
    QUFind(int n)
    {
        for (int i = 0; i < n; i++)
        {
            arr.push_back(i);
        }
    }

    bool connected(int a, int b)
    {
        return arr[a] == arr[b];
    }

    bool quUnion(int a, int b)
    {
        int currA = arr[a];
        int currB = arr[b];
        if (currA == currB)
        {
            return false;
        }
        for (int i = 0; i < arr.size(); i++)
        {
            if (arr[i] == currA)
            {
                arr[i] = currB;
            }
        }
        return true;
    }

    int getArr()
    {
        unordered_set<int> compSet;
        for (int tmp : arr)
        {
            compSet.insert(tmp);
        }
        return compSet.size();
    }
};

class Solution
{
public:
    int countComponents(int n, vector<vector<int>> &edges)
    {
        QUFind qu = QUFind(n);
        for (vector<int> edge : edges)
        {
            int a = edge[0];
            int b = edge[1];
            qu.quUnion(a, b);
        }
        return qu.getArr();
    }
};

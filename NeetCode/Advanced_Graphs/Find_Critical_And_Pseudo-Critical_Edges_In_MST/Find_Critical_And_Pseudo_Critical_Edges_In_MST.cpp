// Find_Critical_And_Pseudo_Critical_Edges_In_MST.cpp
//
// Compile locally with:
// clang++ Find_Critical_And_Pseudo_Critical_Edges_In_MST.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
private:
    class QuickUnion
    {
    public:
        vector<int> parent;
        vector<int> size;
        int components;
        QuickUnion(int n)
        {
            parent.resize(n);
            size.assign(n, 1);
            components = n;
            for (int i = 0; i < n; i++)
            {
                parent[i] = i;
            }
        }
        int find(int index)
        {
            while (parent[index] != index)
            {
                index = parent[index];
            }
            return index;
        }
        bool qunion(int a, int b)
        {
            int rootA = find(a);
            int rootB = find(b);
            if (rootA == rootB)
            {
                return false;
            }

            if (size[rootA] < size[rootB])
            {
                swap(rootA, rootB);
            }

            parent[rootB] = rootA;
            size[rootA] += size[rootB];
            components--;

            return true;
        }
    };

    vector<vector<int>> originalEdges;
    vector<vector<int>> sortedEdges;
    int vertexes;

public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>> &edges)
    {
        vertexes = n;
        originalEdges = edges;

        sort(edges.begin(), edges.end(),
             [](const auto &a, const auto &b)
             {
                 return a[2] < b[2];
             });
        sortedEdges = edges;
        pair<int, int> originalMST = getCost(0, false, false);
        vector<int> critical, psuedo;

        for (int index = 0; index < edges.size(); index++)
        {
            pair<int, int> test = getCost(index, true, false);
            if (test.first > originalMST.first || test.second > originalMST.second)
            {
                critical.push_back(index);
                continue;
            }
            test = getCost(index, false, true);
            if (test.first == originalMST.first && test.second == originalMST.second)
            {
                psuedo.push_back(index);
            }
        }
        return {critical, psuedo};
    }

    pair<int, int> getCost(int index, bool useSkip, bool forceInclude)
    {
        QuickUnion qu = QuickUnion(vertexes);
        int total = 0;
        auto &sedge = originalEdges[index];
        int skipA = sedge[0];
        int skipB = sedge[1];
        int weight = sedge[2];

        if (forceInclude)
        {
            qu.qunion(skipA, skipB);
            total += weight;
        }

        for (auto &edge : sortedEdges)
        {
            int pointA = edge[0];
            int pointB = edge[1];
            int w = edge[2];
            if (useSkip && pointA == skipA && pointB == skipB)
            {
                continue;
            }
            if (qu.find(pointA) == qu.find(pointB))
            {
                continue;
            }
            qu.qunion(pointA, pointB);
            total += w;
        }
        return {total, qu.components};
    }
};

int main()
{
    cout << "Running Find_Critical_And_Pseudo_Critical_Edges_In_MST.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}

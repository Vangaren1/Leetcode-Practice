// N_Queens.cpp
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
    vector<vector<string>> solveNQueens(int n)
    {
        vector<vector<char>> board(n, vector<char>(n, '.'));

        unordered_set<int> columns, posDiag, negDiag;

        vector<vector<string>> results;
        backtrack(0, n, board, columns, posDiag, negDiag, results);
        return results;
    }

    void backtrack(int row, int n, vector<vector<char>> &board, unordered_set<int> &columns, unordered_set<int> &posDiag, unordered_set<int> &negDiag, vector<vector<string>> &results)
    {
        if (row == n)
        {
            vector<string> c;
            for (const vector<char> &tmp : board)
            {
                c.push_back(string(tmp.begin(), tmp.end()));
            }
            results.push_back(c);
            return;
        }
        for (int col = 0; col < n; col++)
        {
            int pDiag = row + col;
            int nDiag = row - col;
            if (columns.find(col) != columns.end() || posDiag.find(pDiag) != posDiag.end() || negDiag.find(nDiag) != negDiag.end())
            {
                continue;
            }

            columns.insert(col);
            posDiag.insert(pDiag);
            negDiag.insert(nDiag);
            board[row][col] = 'Q';

            backtrack(row + 1, n, board, columns, posDiag, negDiag, results);

            columns.erase(col);
            posDiag.erase(pDiag);
            negDiag.erase(nDiag);
            board[row][col] = '.';
        }
    }
};

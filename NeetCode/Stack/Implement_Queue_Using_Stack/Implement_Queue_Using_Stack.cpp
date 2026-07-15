// Implement_Queue_Using_Stack.cpp
//
// Compile locally with:
// clang++ Implement_Queue_Using_Stack.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class MyQueue
{
private:
    stack<int> mystack;

public:
    MyQueue()
    {
    }

    void push(int x)
    {
        stack<int> tmp;
        while (!mystack.empty())
        {
            tmp.push(mystack.top());
            mystack.pop();
        }
        mystack.push(x);
        while (!tmp.empty())
        {
            mystack.push(tmp.top());
            tmp.pop();
        }
    }

    int pop()
    {
        int n = mystack.top();
        mystack.pop();
        return n;
    }

    int peek()
    {
        return mystack.top();
    }

    bool empty()
    {
        return mystack.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */

int main()
{
    cout << "Running Implement_Queue_Using_Stack.cpp..." << endl;

    MyQueue sol;

    // TODO:
    // Add local test calls here

    return 0;
}

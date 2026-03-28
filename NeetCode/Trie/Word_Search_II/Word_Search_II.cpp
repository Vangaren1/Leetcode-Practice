// Word_Search_II.cpp
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

class WordDictionary
{
private:
    class Node
    {
    public:
        array<Node *, 26> children{};
        bool terminal = false;
    };

    Node *root;

    bool src(string word, Node *ptr, int start)
    {
        for (int idx = start; idx < word.size(); idx++)
        {
            char ch = word[idx];

            if (ch == '.')
            {
                for (Node *tmp : ptr->children)
                {
                    if (tmp != nullptr && src(word, tmp, idx + 1))
                    {
                        return true;
                    }
                }
                return false;
            }

            if (ptr->children[ch - 'a'] == nullptr)
            {
                return false;
            }
            ptr = ptr->children[ch - 'a'];
        }
        return ptr->terminal;
    }

public:
    WordDictionary()
    {
        root = new Node();
    }

    void addWord(string word)
    {
        Node *ptr = root;
        for (char ch : word)
        {
            if (ptr->children[ch - 'a'] == nullptr)
            {
                ptr->children[ch - 'a'] = new Node();
            }
            ptr = ptr->children[ch - 'a'];
        }
        ptr->terminal = true;
    }

    bool search(string word)
    {
        Node *ptr = root;
        return src(word, ptr, 0);
    }
};

int main()
{
    WordDictionary wordDictionary;
    wordDictionary.addWord("day");
    wordDictionary.addWord("bay");
    wordDictionary.addWord("may");
    cout << wordDictionary.search("say") << endl;
}
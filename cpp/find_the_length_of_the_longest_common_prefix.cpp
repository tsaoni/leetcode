#include <iostream> 
#include <vector> 
#include <unordered_map> 

using namespace std; 

class Trie {
public: 
    Trie() {

    }
    ~Trie() {

    }

    void insert(int s) {
        if (root_ == NULL)
            root_ = new TrieNode(); 
        TrieNode *cur = root_; 
        vector<int> stk = {}; 
        while (s > 0) {
            stk.push_back(s % 10); 
            s /= 10; 
        }
        for (int i = stk.size() - 1; i >= 0; i--) {
            int c = stk[i]; 
            if (cur -> children.find(c) == cur -> children.end()) {
                cur -> children[c] = new TrieNode(); 
                cur -> children[c] -> value = c; 
            }
            cur = cur -> children[c]; 
        }
        cur -> is_terminal = true; 
    }

    int get_prefix_len(int s) {
        TrieNode *cur = root_; 
        vector<int> stk = {}; 
        while (s > 0) {
            stk.push_back(s % 10); 
            s /= 10; 
        }
        int l = 0; 
        for (int i = stk.size() - 1; i >= 0; i--) {
            int c = stk[i]; 
            if (cur -> children.find(c) == cur -> children.end()) {
                break; 
            }
            l++; 
            cur = cur -> children[c]; 
        }
        return l; 
    }


private: 
    struct TrieNode {
        unordered_map<char, TrieNode *> children;
        int value = -1;
        bool is_terminal = false;
    };

    TrieNode *root_ = NULL;
}; 

class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        Trie t = Trie(); 
        for (int x: arr1)
            t.insert(x); 
        int ret = 0; 
        for (int x: arr2)
            ret = max(ret, t.get_prefix_len(x)); 
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> arr1 = {1,10,100}; 
    // vector<int> arr2 = {1000}; 
    vector<int> arr1 = {1,2,3}; 
    vector<int> arr2 = {4,4,4}; 
    int ret = s.longestCommonPrefix(arr1, arr2); 
    cout << "ans: " << ret << endl; 
}
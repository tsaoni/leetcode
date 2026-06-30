#include <iostream> 
#include <vector> 

using namespace std; 

class TrieNode {
public:
    TrieNode* children[26]; 
    bool isEndOfWord;
    int max_length; 
    int t; 

    TrieNode() {
        isEndOfWord = false;
        max_length = 5001; 
        t = 0; 
        for (int i = 0; i < 26; i++) children[i] = nullptr;
    }
    ~TrieNode() {
        for (int i = 0; i < 26; i++) {
            if (children[i] != nullptr) {
                delete children[i]; 
            }
        }
    }
};

class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }
    ~Trie() { delete root; }
    
    void insert(string s, int ord) {
        TrieNode *cur = root; 
        int L = s.size(); 
        if (L == 0 && cur -> max_length > 0) {
            cur -> max_length = 0; 
            cur -> t = ord; 
            cur -> isEndOfWord = true; 
            return; 
        }
            
        for (int i = L - 1; i >= 0; i--) {
            char c = s[i]; 
            int cidx = c - 'a'; 
            if (cur -> children[cidx] == nullptr)
                cur -> children[cidx] = new TrieNode(); 
            if (L < cur -> max_length) {
                cur -> max_length = L; 
                cur -> t = ord; 
            }
            cur = cur -> children[cidx]; 
        }
        if (L < cur -> max_length) {
            cur -> max_length = L; 
            cur -> t = ord; 
        }
        cur -> isEndOfWord = true; 
    }

    int search(string s) {
        TrieNode *cur = root; 
        int ret = 0; 
        int L = s.size(); 
        for (int i = L - 1; i >= 0; i--) {
            char c = s[i]; 
            int cidx = c - 'a'; 
            if (cur -> children[cidx] == nullptr)
                return cur -> t; 
            cur = cur -> children[cidx]; 
        }
        return cur -> t; 
    }
}; 

class Solution {
public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        Trie *trie = new Trie(); 
        for (int i = 0; i < wordsContainer.size(); i++)
            trie -> insert(wordsContainer[i], i); 
        vector<int> ret; 
        for (string& s: wordsQuery)
            ret.push_back(trie -> search(s)); 
        delete trie; 
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<string> wordsContainer = {"abcd","bcd","xbcd"}; 
    // vector<string> wordsQuery = {"cd","bcd","xyz"}; 
    // vector<string> wordsContainer = {"abcdefgh","poiuygh","ghghgh"}; 
    // vector<string> wordsQuery = {"gh","acbfgh","acbfegh"}; 
    vector<string> wordsContainer = {"abcdef", "f"}; 
    vector<string> wordsQuery = {"xye"}; 
    vector<int> ret = s.stringIndices(wordsContainer, wordsQuery); 
    cout << "ans: " << endl; 
    for (auto x: ret)
        cout << x << " "; 
    cout << endl; 
}
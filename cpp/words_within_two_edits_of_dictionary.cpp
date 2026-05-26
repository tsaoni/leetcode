#include <vector> 
#include <iostream>

using namespace std; 

struct TrieNode {
    TrieNode* children[26]; 
    // bool isEndOfWord;       

    TrieNode() {
        // isEndOfWord = true;
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }
    }
};


class Tries {
    private:
        
    public:
        TrieNode* root;

        Tries() {
            root = new TrieNode();
        }

        void insert(string s) {
            TrieNode *cur = root; 
            for (auto c: s) {
                if (cur -> children[c - 'a'] == nullptr)
                    cur -> children[c - 'a'] = new TrieNode(); 
                cur = cur -> children[c - 'a']; 
            }

        }

        bool search(string s, TrieNode* node, int idx, int cnt) {
            if (idx == s.size())
                return true; 

            char c = s[idx]; 
            bool suc = false; 
            for (int i = 0; i < 26; i++) {
                if (node -> children[i] != nullptr) {
                    if (('a' + i) != c) {
                        if (cnt == 2)
                            return false; 
                        else 
                            suc = search(s, node -> children[i], idx + 1, cnt + 1); 
                    }
                    else 
                        suc = search(s, node -> children[i], idx + 1, cnt); 
                    if (suc)
                        return true; 
                }
            }
            return false; 
        }
}; 

class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        Tries t = Tries(); 
        vector<string> ret = {}; 
        for (string& s: dictionary)
            t.insert(s); 
        for (string& s: queries) {
            if (t.search(s, t.root, 0, 0))
                ret.push_back(s); 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<string> queries = {"word","note","ants","wood"}; 
    // vector<string> dictionary = {"wood","joke","moat"}; 
    vector<string> queries = {"yes"}; 
    vector<string> dictionary = {"not"}; 
    vector<string> ret = s.twoEditWords(queries, dictionary); 
    cout << "ans: " << endl; 
    for (auto& s: ret) 
        cout << s << " "; 
    cout << endl; 
}
#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    vector<int> compute_lps(string pattern) {
        int m = pattern.size(); 
        vector<int> lps(m, 0); 
        int cur = 0; 
        for (int i = 1; i < m; i++) {
            while (true) {
                if (pattern[i] == pattern[cur]) {
                    cur++; 
                    lps[i] = cur; 
                    break; 
                }
                else {
                    if (lps[cur] == cur) {
                        lps[i] = 0; 
                        break; 
                    }
                    cur = lps[cur]; 
                }
            }
        }
        return lps; 
    }

    bool rotateString(string s, string goal) {
        if (s.size() != goal.size())
            return false; 
        vector<int> lps = compute_lps(goal); 
        // for (auto x: lps)
        //     cout << x << " "; 
        // cout << endl; 
        string _s = s + s; 
        int cur = 0; 
        for (int i = 0; i < _s.size(); i++) {
            // cout << i << " " << cur << " " << _s[i] << endl; 
            while (true) {
                if (_s[i] == goal[cur]) {
                    cur++; 
                    break; 
                }
                else {
                    if (cur == lps[cur]) {
                        cur = 0; 
                        break; 
                    }
                    cur = lps[cur - 1]; 
                }
            }
            if (cur == goal.size())
                return true; 
        }
        return false; 
    }
};

int main() {
    Solution sol = Solution(); 
    // string s = "abcde", goal = "cdeab"; 
    string s = "abcde", goal = "abced"; 
    // string s = "defdefdefabcabc", goal = "defdefabcabcdef"; 
    bool ret = sol.rotateString(s, goal); 
    cout << "ans: " << ret << endl; 
}
#include <iostream> 
#include <queue> 
#include <vector>

using namespace std; 
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        queue<int> q; 
        q.push(0); 
        vector<bool> dp(s.size(), false); 
        dp[0] = true; 
        int N = s.size(); 
        int end = 0; 
        while (q.size() > 0) {
            // int end = q.back(); 
            int cur = q.front(); 
            q.pop(); 
            int _start = max(cur + minJump, end + 1); 
            int _end = min(N - 1, cur + maxJump); 
            // cout << _start << " " << _end << endl; 
            for (int i = _start; i <= _end; i++) {
                if (s[i] == '0') {
                    dp[i] = true; 
                    q.push(i); 
                    // cout << i << endl; 
                }
            }
            if (_end == N - 1)
                break; 
            end = _end; 
        }
        return dp.back(); 
    }
};

int main() {
    Solution sol = Solution(); 
    string s = "011010"; 
    int minJump = 2, maxJump = 3; 
    // string s = "01101110"; 
    // int minJump = 2, maxJump = 3; 
    int ret = sol.canReach(s, minJump, maxJump); 
    cout << "ans: " << ret << endl; 
}
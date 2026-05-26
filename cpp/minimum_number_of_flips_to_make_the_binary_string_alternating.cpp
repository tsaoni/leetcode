#include <iostream> 
#include <vector> 
#include <string>

using namespace std; 
class Solution {
public:
    int minFlips(string s) {
        int N = static_cast<int>(s.size()); 
        vector<vector<int>> pre(N + 1, vector<int>(2, 0)), suf(N + 1, vector<int>(2, 0));  
        for (int i = 1; i <= N; i++) {
            if (s[i - 1] == '0') { // pre
                pre[i][0] = pre[i - 1][1]; 
                pre[i][1] = pre[i - 1][0] + 1; 
            }
            else {
                pre[i][0] = pre[i - 1][1] + 1; 
                pre[i][1] = pre[i - 1][0]; 
            }
            if (s[N - i] == '0') { // suf
                suf[N - i][0] = suf[N - i + 1][1]; 
                suf[N - i][1] = suf[N - i + 1][0] + 1; 
            }
            else {
                suf[N - i][0] = suf[N - i + 1][1] + 1; 
                suf[N - i][1] = suf[N - i + 1][0]; 
            }
        }

        int ret = N; 
        if (N % 2 == 0) {
            for (int i = 0; i < N + 1; i++) {
                ret = min(ret, pre[i][0] + suf[i][1]); 
                ret = min(ret, pre[i][1] + suf[i][0]); 
            }
        }
        else {
            for (int i = 0; i < N + 1; i++) {
                ret = min(ret, pre[i][0] + suf[i][0]); 
                ret = min(ret, pre[i][1] + suf[i][1]); 
            }
        }
        return ret; 
    }
};

int main() {
    Solution sol = Solution(); 
    string s = "1110"; 
    int ret = sol.minFlips(s); 
    cout << "ans: " << ret << endl; 
    return 0; 
}
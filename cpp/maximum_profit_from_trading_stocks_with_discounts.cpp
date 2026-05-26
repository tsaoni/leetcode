#include <vector>
#include <iostream> 
#include <unordered_map>

using namespace std; 
class Solution {
public:
    vector<vector<int>> dfs(unordered_map<int, vector<int>>& T, 
        vector<int>& present, vector<int>& future, int cur, int budget) {
        vector<vector<int>> dp(budget + 1, vector<int>(2, 0)), _dp(budget + 1, vector<int>(2, 0)); 
        vector<vector<int>>& src = _dp, tgt = dp; 

        for(int i = 0; i < budget + 1; i++) {
            if (i >= present[cur])
                src[i][0] = (future[cur] - present[cur]); 
            if (i >= (present[cur] / 2))
                src[i][1] = (future[cur] - (present[cur] / 2)); 
        }
            
        for (auto c: T[cur]) {
            // vector<vector<int>> dpc(dp.size(), vector<int>(2, 0)); 
            // cout << c << endl; 
            vector<vector<int>> dpc = dfs(T, present, future, c, budget); 
            for(int i = 0; i < budget + 1; i++) {
                tgt[i][0] = max(tgt[i][0], dpc[i][0]); 
                tgt[i][1] = max(tgt[i][1], dpc[i][0]); 
                for (int j = present[cur]; j < i + 1; j++) 
                    tgt[i][0] = max(tgt[i][0], src[j][0] + dpc[i - j][1]); 
                for (int j = present[cur] / 2; j < i + 1; j++) 
                    tgt[i][1] = max(tgt[i][1], src[j][1] + dpc[i - j][1]); 
            }
            swap(src, tgt); 
        }
        cout << cur << endl; 
        for (auto& v: src)
            cout << v[0] << " "; 
        cout << endl; 
        for (auto& v: src)
            cout << v[1] << " "; 
        cout << endl; 
        return src; 
    }

    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        unordered_map<int, vector<int>> T; 
        // vector<vector<int>> dp(budget + 1, vector<int>(2, 0)); 
        for (vector<int>& v: hierarchy) {
            if (T.find(v[0] - 1) == T.end())
                T[v[0] - 1] = {}; 
            T[v[0] - 1].push_back(v[1] - 1); 
        }
        vector<vector<int>> dp = dfs(T, present, future, 0, budget); 
        int maxv = dp[0][0]; 
        for (auto& v: dp) {
            maxv = max(maxv, v[0]); 
        }
        return maxv; 
    }
};



int main() {
    Solution s = Solution(); 
    // int n = 2; 
    // vector<int> present = {1,2}; 
    // vector<int> future = {4,3}; 
    // vector<vector<int>> hierarchy = {{1,2}}; 
    // int n = 2; 
    // vector<int> present = {3,4}; 
    // vector<int> future = {5,8}; 
    // vector<vector<int>> hierarchy = {{1,2}}; 
    // int budget = 4; 
    // int n = 3; 
    // vector<int> present = {4,6,8}; 
    // vector<int> future = {7,9,11}; 
    // vector<vector<int>> hierarchy = {{1,2},{1,3}}; 
    // int budget = 10; 
    int n = 3; 
    vector<int> present = {49,10,27}; 
    vector<int> future = {18,44,38}; 
    vector<vector<int>> hierarchy = {{1,3},{1,2}}; 
    int budget = 141; 
    int ret = s.maxProfit(n, present, future, hierarchy, budget); 
    cout << "ans: " << ret << endl; 
}
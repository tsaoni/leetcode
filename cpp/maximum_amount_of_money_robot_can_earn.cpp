#include <iostream> 
#include <vector> 
#include <algorithm>

using namespace std; 
class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        int n = coins.size(), m = coins[0].size(); 
        int NINF = -(500 * 500 * 1000); 
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(3, NINF))); 
        dp[0][0][0] = coins[0][0]; 
        if (coins[0][0] < 0)
            dp[0][0][1] = 0; 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (coins[i][j] < 0) {
                    for (int t = 0; t < 3; t++) {
                        if (t > 0) {
                            if (i > 0)
                                dp[i][j][t] = max({dp[i][j][t], dp[i - 1][j][t] + coins[i][j], dp[i - 1][j][t - 1]}); 
                            if (j > 0)
                                dp[i][j][t] = max({dp[i][j][t], dp[i][j - 1][t] + coins[i][j], dp[i][j - 1][t - 1]}); 
                        }
                        else {
                            if (i > 0)
                                dp[i][j][t] = max({dp[i][j][t], dp[i - 1][j][t] + coins[i][j]}); 
            
                            if (j > 0)
                                dp[i][j][t] = max({dp[i][j][t], dp[i][j - 1][t] + coins[i][j]}); 
                
                        }
                    }
                }
                else {
                    for (int t = 0; t < 3; t++) {
                        if (i > 0)
                            dp[i][j][t] = max(dp[i][j][t], dp[i - 1][j][t] + coins[i][j]); 
                
                        if (j > 0)
                            dp[i][j][t] = max(dp[i][j][t], dp[i][j - 1][t] + coins[i][j]); 

                    }
                }
            }
        }
        return *max_element(dp[n - 1][m - 1].begin(), dp[n - 1][m - 1].end()); 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> coins = {{0,1,-1},{1,-2,3},{2,-3,4}}; 
    vector<vector<int>> coins = {{10,10,10},{10,10,10}}; 
    int ret = s.maximumAmount(coins); 
    cout << "ans: " << ret << endl; 
}
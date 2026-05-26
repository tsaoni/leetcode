#include <iostream> 
#include <vector> 
#include <cmath> 
#include <utility> 

using namespace std; 
class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        int modulo = pow(10, 9) + 7; 
        int n = grid.size(), m = grid[0].size(); 
        vector<vector<pair<long long, long long>>> dp(n, vector<pair<long long, long long>>(m, make_pair(-1, -1))); 
        if (grid[0][0] > 0)
            dp[0][0].second = grid[0][0]; 
        else if (grid[0][0] == 0) {
            dp[0][0].first = grid[0][0]; 
            dp[0][0].second = grid[0][0]; 
        }
        else 
            dp[0][0].first = -grid[0][0]; 
        for (int sm = 0; sm <= (n + m - 2); sm++) {
            for (int j = min(m - 1, sm); ((sm - j) < n) && (j >= 0); j--) {
                int i = sm - j; 
                if (i > 0) {
                    if (grid[i][j] < 0) {
                        dp[i][j].first = (dp[i - 1][j].second < 0) ? -1: static_cast<long long>(-grid[i][j] * dp[i - 1][j].second); 
                        dp[i][j].second = (dp[i - 1][j].first < 0) ? -1: static_cast<long long>(-grid[i][j] * dp[i - 1][j].first); 
                    }
                    else if (grid[i][j] == 0) {
                        dp[i][j].first = (dp[i - 1][j].second < 0) ? 0: static_cast<long long>(-grid[i][j] * dp[i - 1][j].second); 
                        dp[i][j].second = (dp[i - 1][j].first < 0) ? 0: static_cast<long long>(-grid[i][j] * dp[i - 1][j].first); 
                    }
                    else {
                        dp[i][j].first = (dp[i - 1][j].first < 0) ? -1: static_cast<long long>(grid[i][j] * dp[i - 1][j].first); 
                        dp[i][j].second = (dp[i - 1][j].second < 0) ? -1: static_cast<long long>(grid[i][j] * dp[i - 1][j].second); 
                    }
                }
                if (j > 0) {
                    if (grid[i][j] < 0) {
                        dp[i][j].first = (dp[i][j - 1].second < 0) ? dp[i][j].first: max(static_cast<long long>(dp[i][j].first), static_cast<long long>(-grid[i][j] * dp[i][j - 1].second)); 
                        dp[i][j].second = (dp[i][j - 1].first < 0) ? dp[i][j].second: max(static_cast<long long>(dp[i][j].second), static_cast<long long>(-grid[i][j] * dp[i][j - 1].first)); 
                    }
                    else if (grid[i][j] == 0) {
                        dp[i][j].first = (dp[i][j - 1].second < 0) ? max(0LL, dp[i][j].first): max(static_cast<long long>(dp[i][j].first), static_cast<long long>(-grid[i][j] * dp[i][j - 1].second)); 
                        dp[i][j].second = (dp[i][j - 1].first < 0) ? max(0LL, dp[i][j].second): max(static_cast<long long>(dp[i][j].second), static_cast<long long>(-grid[i][j] * dp[i][j - 1].first)); 
                    }
                    else {
                        dp[i][j].first = (dp[i][j - 1].first < 0) ? dp[i][j].first: max(static_cast<long long>(dp[i][j].first), static_cast<long long>(grid[i][j] * dp[i][j - 1].first)); 
                        dp[i][j].second = (dp[i][j - 1].second < 0) ? dp[i][j].second: max(static_cast<long long>(dp[i][j].second), static_cast<long long>(grid[i][j] * dp[i][j - 1].second)); 
                    }
                }
                // cout << i << " " << j << " out " << dp[i][j].first << " " << dp[i][j].second << endl; 
            }
        }
        long long ret = dp.back().back().second; 
        
        // cout << "out " << dp.back().back().first << endl; 
        return (ret < 0) ? -1: ret % modulo; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> grid = {{-1,-2,-3},{-2,-3,-3},{-3,-3,-2}}; 
    vector<vector<int>> grid = {{1,-2,1},{1,-2,1},{3,-4,1}}; 
    // vector<vector<int>> grid = {{1,3},{0,-4}}; 
    int ret = s.maxProductPath(grid); 
    cout << "ans: " << ret << endl; 
}
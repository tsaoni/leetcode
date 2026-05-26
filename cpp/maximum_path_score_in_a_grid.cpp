#include <iostream> 
#include <vector> 
#include <algorithm> 

using namespace std; 
class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int n = grid.size(), m = grid[0].size(); 
        vector<vector<int>> dp1(m, vector<int>(k + 1, -1)), dp2(m, vector<int>(k + 1, -1)); 
        // for (int i = 0; i <= m; i++)
        dp1[0][0] = 0; 
        // dp2[0][0] = 0; 
        for (int i = 0; i < n; i++) {
            // dp2[0][0] = 0; 
            for (int j = 0; j < m; j++) {
                // dp2[j][0] = 0; 
                int cost = (grid[i][j] > 0) ? 1: 0; 
                for (int _k = 0; _k <= k; _k++) {
                    if ((_k - cost) >= 0) {
                        if ((j > 0) && (dp2[j - 1][_k - cost] >= 0))
                            dp2[j][_k] = max(dp2[j][_k], dp2[j - 1][_k - cost] + grid[i][j]); 
                        if (dp1[j][_k - cost] >= 0)
                            dp2[j][_k] = max(dp2[j][_k], dp1[j][_k - cost] + grid[i][j]); 
                    }
                }
            }
            swap(dp1, dp2); 
            for (auto& v: dp2)
                fill(v.begin(), v.end(), -1); 
        }
        int ret = -1; 
        for (int i = 0; i <= k; i++)
            ret = max(ret, dp1[m - 1][i]); 
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> grid = {{0, 1},{2, 0}}; 
    // int k = 1; 
    vector<vector<int>> grid = {{0, 1},{1, 2}}; 
    int k = 1; 
    int ret = s.maxPathScore(grid, k); 
    cout << "ans: " << ret << endl; 
}
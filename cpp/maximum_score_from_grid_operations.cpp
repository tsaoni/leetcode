#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    long long maximumScore(vector<vector<int>>& grid) {
        int n = grid.size(); 
        vector<vector<long long>> pfx(n + 1, vector<long long>(n, 0)); 
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                pfx[j + 1][i] = grid[j][i] + pfx[j][i]; 
        
        vector<vector<long long>> sfx1(n + 1, vector<long long>(n + 1, 0)), sfx2(n + 1, vector<long long>(n + 1, 0)); 
        vector<vector<long long>>& sfx_p1 = sfx1, sfx_p2 = sfx2; 
        vector<vector<long long>> pmax1(n + 1, vector<long long>(n + 1, 0)), pmax2(n + 1, vector<long long>(n + 1, 0)); 
        vector<vector<long long>>& pmax_p1 = pmax1, pmax_p2 = pmax2; 
        vector<vector<vector<long long>>> dp(n, vector<vector<long long>>(n + 1, vector<long long>(n + 1, 0))); 
        for (int i = 0; i < n; i++) {
            for(int cur = 0; cur <= n; cur++) {
                for (int prev = 0; prev <= n; prev++) {
                    if (i == 0) {
                        dp[i][cur][prev] = 0; 
                    }
                    else {
                        if (cur <= prev)
                            dp[i][cur][prev] = sfx_p1[prev][0] + (pfx[prev][i] - pfx[cur][i]); 
                        else {
                            dp[i][cur][prev] = max(sfx_p1[prev][cur], pmax_p1[prev][cur] + (pfx[cur][i - 1] - pfx[prev][i - 1])); 
                        }   
                    }
                    
                }
                
            }
            for(int cur = 0; cur <= n; cur++) {
                sfx_p2[cur][n] = dp[i][cur][n]; 
                for (int k = n; k > 0; k--)
                    sfx_p2[cur][k - 1] = max(dp[i][cur][k - 1], sfx_p2[cur][k]); 

                pmax_p2[cur][0] = dp[i][cur][0] - pfx[0][i]; 
                for (int k = 1; k <= n; k++)
                    pmax_p2[cur][k] = max(pmax_p2[cur][k - 1], dp[i][cur][k] - max(0LL, pfx[k][i] - pfx[cur][i])); 
            }
            
            swap(pmax_p1, pmax_p2); 
            swap(sfx_p1, sfx_p2); 
        }

        long long ans = 0LL; 
        for (int cur = 0; cur <= n; cur++)
            for (int prev = 0; prev <= n; prev++)
                ans = max(ans, dp[n - 1][cur][prev]); 
        return ans; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<vector<int>> grid = {{0,0,0,0,0},{0,0,3,0,0},{0,1,0,0,0},{5,0,0,3,0},{0,0,0,0,2}}; 
    long long ret = s.maximumScore(grid); 
    cout << "ans: " << ret << endl; 
}
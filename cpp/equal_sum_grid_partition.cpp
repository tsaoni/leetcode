#include <iostream> 
#include <vector> 
#include <utility> 
#include <iostream> 
#include <cmath>

using namespace std; 
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size(); 
        long sm = 0; 
        int MAXN = pow(10, 5); 
        vector<int> freq(MAXN + 1, 0), freqt(MAXN + 1, 0); ; 
        vector<long> h(n, 0), v(m, 0); 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sm += grid[i][j]; 
                h[i] += grid[i][j]; 
                v[j] += grid[i][j]; 
                freq[grid[i][j]]++; 
            }
        }
        // if ((sm % 2) == 1)
        //     return false; 
        
        long acc = 0; 
        for (int i = 0; i < n; i++) {
            acc += h[i]; 
            if (acc == (sm - acc))
                return true; 
            for (int j = 0; j < m; j++) {
                freqt[grid[i][j]]++; 
                freq[grid[i][j]]--; 
            }
            long x = 2 * acc - sm; 
            if (((i == 0) && ((grid[i][0] == x) || (grid[i][m - 1] == x))) || (i > 0)) {
                if ((m > 1) || ((m == 1) && ((grid[0][0] == x) || (grid[i][0] == x)))) {
                    if (((x > 0) && (x <= MAXN)) && (freqt[x] > 0)) 
                        return true; 
                }
            }
        }

        acc = 0; 
        for (int j = m - 1; j >= 0; j--) {
            acc += v[j]; 
            if (acc == (sm - acc))
                return true; 
            for (int i = 0; i < n; i++) {
                freq[grid[i][j]]++; 
                freqt[grid[i][j]]--; 
            }
            long x = 2 * acc - sm; 
            if (((j == (m - 1)) && ((grid[0][j] == x) || (grid[n - 1][j] == x))) || (j < (m - 1))) {
                if ((n > 1) || ((n == 1) && ((grid[0][m - 1] == x) || (grid[0][j] == x)))) {
                    if (((x > 0) && (x <= MAXN)) && (freq[x] > 0)) 
                        return true; 
                }
            }
        }

        acc = 0; 
        for (int i = n - 1; i >= 0; i--) {
            acc += h[i]; 
            if (acc == (sm - acc))
                return true; 
            for (int j = m - 1; j >= 0; j--) {
                freqt[grid[i][j]]++; 
                freq[grid[i][j]]--; 
            }
            long x = 2 * acc - sm; 
            if (((i == (n - 1)) && ((grid[i][0] == x) || (grid[i][m - 1] == x))) || (i < (n - 1))) {
                if ((m > 1) || ((m == 1) && ((grid[n - 1][0] == x) || (grid[i][0] == x)))) {
                    if (((x > 0) && (x <= MAXN)) && (freqt[x] > 0)) 
                        return true; 
                }
            }
        }

        acc = 0; 
        for (int j = 0; j < m; j++) {
            acc += v[j]; 
            if (acc == (sm - acc))
                return true; 
            for (int i = n - 1; i >= 0; i--) {
                freq[grid[i][j]]++; 
                freqt[grid[i][j]]--; 
            }
            long x = 2 * acc - sm; 
            if (((j == 0) && ((grid[0][j] == x) || (grid[n - 1][j] == x))) || (j > 0)) {
                if ((n > 1) || ((n == 1) && ((grid[0][0] == x) || (grid[0][j] == x)))) {
                    if (((x > 0) && (x <= MAXN)) && (freq[x] > 0)) 
                        return true; 
                }
            }
        }
        return false; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> grid = {{1,4},{2,3}}; 
    // vector<vector<int>> grid = {{1,2},{3,4}}; 
    // vector<vector<int>> grid = {{1,2,4},{2,3,5}}; 
    vector<vector<int>> grid = {{65146,67299}}; 
    bool ret = s.canPartitionGrid(grid); 
    cout << "ans: " << ret << endl; 
}
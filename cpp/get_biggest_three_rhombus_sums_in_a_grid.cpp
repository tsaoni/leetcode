#include <iostream> 
#include <vector> 
#include <queue> 
#include <functional>
#include <unordered_set>

using namespace std; 
class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        unsigned int m = grid.size(), n = grid[0].size(); 
        vector<vector<vector<unsigned int>>> psum(m, vector<vector<unsigned int>>(n, vector<unsigned int>(2, 0))); 
        // vector<int> d = {1, 1, -1}; 
        priority_queue<int, vector<int>, greater<int>> minv;
        unordered_set<int> e;
        for (int l = 1; l <= min(m, n); l++) {
            for (int i = 0; i <= (m - l); i++) {
                for (int j = 0; j <= n - l; j++) {
                    if (l == 1)
                        psum[i][j][0] = grid[i][j]; 
                    else 
                        psum[i][j][0] = psum[i + 1][j + 1][0] + grid[i][j]; 
                }
                for (int j = l - 1; j < n; j++) {
                    if (l == 1)
                        psum[i][j][1] = grid[i][j]; 
                    else 
                        psum[i][j][1] = psum[i + 1][j - 1][1] + grid[i][j]; 
                    if (((i - l + 1) >= 0) && ((j - 2 * (l - 1)) >= 0)) {
                        int v; 
                        if (l == 1)
                            v = grid[i][j]; 
                        else {
                            v = psum[i - l + 1][j - l + 1][0] + psum[i][j][1] + psum[i - l + 1][j - l + 1][1] + psum[i][j - 2 * (l - 1)][0]; 
                            v -= (grid[i][j] + grid[i - l + 1][j - l + 1] + grid[i + l - 1][j - l + 1] + grid[i][j - 2 * (l - 1)]); 
                        }
                        
                        // cout << endl; 
                        // cout << i << " " << j - l + 1 << " " << v << endl; 
                        if (minv.size() < 3u) {
                            if (e.find(v) == e.end()) {
                                minv.push(v); 
                                e.insert(v);
                            }
                        }   
                        else {
                            if ((e.find(v) == e.end()) && (v > minv.top())) {
                                int _v = minv.top(); 
                                minv.pop(); 
                                minv.push(v);
                                e.insert(v); 
                                e.erase(_v); 
                            }
                        }
                    }
                }
            }
            // for (int k = 0; k < 2; k++) {
            //     cout << l << " start " << k << endl; 
            //     for (int i = 0; i < m; i++) {
            //         for (int j = 0; j < n; j++)
            //             cout << psum[i][j][k] << " "; 
            //         cout << endl; 
            //     }
            //     cout << endl; 
            // }
        }
        vector<int> v = {}; 
        while (!minv.empty()) {
            v.insert(v.begin(), minv.top()); 
            minv.pop(); 
        }
        return v; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> grid = {{3,4,5,1,3},{3,3,4,2,3},{20,30,200,40,10},{1,5,5,4,1},{4,3,2,2,5}}; 
    // vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}}; 
    vector<vector<int>> grid = {{7,7,7}}; 
    vector<int> v = s.getBiggestThree(grid); 
    cout << "ans:" << endl; 
    for (auto x: v) 
        cout << x << " "; 
    cout << endl; 
}
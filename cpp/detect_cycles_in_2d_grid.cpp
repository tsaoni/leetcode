#include <vector> 
#include <iostream>

using namespace std; 
class Solution {
public:
    bool dfs(vector<vector<int>>& visited, vector<vector<char>>& grid, int ci, int cj, int prev_d) {
        // cout << ci << " " << cj << endl; 
        if (visited[ci][cj])
            return true; 
        int n = grid.size(), m = grid[0].size(); 
        visited[ci][cj] = 1; 
        vector<int> d = {-1, 0, 1, 0, -1}; 
        for (int i = 0; i < 4; i++) {
            int di = d[i], dj = d[i + 1]; 
            int x = ci + di, y = cj + dj; 
            if ((x >= 0) && (x < n) && (y >= 0) && (y < m)) {
                if ((grid[ci][cj] == grid[x][y]) && (abs(i - prev_d) != 2)) {
                    bool have_cycle = dfs(visited, grid, x, y, i); 
                    if (have_cycle)
                        return true; 
                }
            }
        }
        return false; 
    }

    bool containsCycle(vector<vector<char>>& grid) {
        int n = grid.size(), m = grid[0].size(); 
        vector<vector<int>> visited(n, vector<int>(m, 0)); 
        bool have_cycle = false; 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j]) {
                    have_cycle = dfs(visited, grid, i, j, -4); 
                    // cout << i << " " << j << have_cycle << endl; 
                    if (have_cycle)
                        return true; 
                }
            }
        }
        return have_cycle; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<char>> grid = {{'a','a','a','a'},{'a','b','b','a'},{'a','b','b','a'},{'a','a','a','a'}}; 
    // vector<vector<char>> grid = {{'c','c','c','a'},{'c','d','c','c'},{'c','c','e','c'},{'f','c','c','c'}}; 
    // vector<vector<char>> grid = {{'a','b','b'},{'b','z','b'},{'b','b','a'}}; 
    vector<vector<char>> grid = {{'a','a','b'}}; 
    bool ret = s.containsCycle(grid); 
    cout << "ans: " << ret << endl; 
}
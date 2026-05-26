#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size(); 
        int N = n * m; 
        vector<long long> pfx(N + 1, 1), sfx(N + 1, 1); 
        vector<vector<int>> ret(n, vector<int>(m, 0)); 
        int modulo = 12345; 
        for (int i = 0; i < N; i++) {
            pfx[i + 1] = (pfx[i] * grid[i / m][i % m]) % modulo; 
            sfx[N - i - 1] = (sfx[N - i] * grid[(N - 1 - i) / m][(N - 1 - i) % m]) % modulo; 
            // cout << pfx[i + 1] << " " << grid[i / N][i % N] << " " << i << " " << sfx[N - i - 1] << endl; 
        }
        for (int i = 0; i < N; i++)
            ret[i / m][i % m] = (pfx[i] * sfx[i + 1]) % modulo; 

        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<vector<int>> grid = {{1,2},{3,4}}; 
    vector<vector<int>> ret = s.constructProductMatrix(grid); 
    cout << "ans: " << endl; 
    for (auto& row: ret) {
        for (auto x: row)
            cout << x << " "; 
        cout << endl; 
    }
}
#include <iostream> 
#include <vector> 
#include <unordered_map> 

using namespace std; 
class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        unsigned int m = grid.size(), n = grid[0].size(); 
        int INF = (m * n) + 1; 
        unordered_map<char, int> mp = {
            {'.', 0},
            {'X', 1},
            {'Y', -1}
        };
        vector<int> v1(n, INF), v2(n, INF); 
        vector<int> *ptr1 = &v1, *ptr2 = &v2; 
        int ret = 0; 
        for (unsigned i = 0; i < m; i++) {
            int sm = INF; 
            for (unsigned j = 0; j < n; j++) {
                if (sm == INF) {
                    sm = (mp[grid[i][j]] == 0) ? INF: mp[grid[i][j]]; 
                }
                else 
                    sm += mp[grid[i][j]]; 
                // cout << sm << endl; 
                if (i == 0) {
                    (*ptr2)[j] = sm; 
                    // if ((j == 0) || ((j > 0) && (*ptr2)[j - 1] == INF)) {
                    //     (*ptr2)[j] = (sm == 0) ? INF: sm; 
                    // }
                    // else {
                    //     (*ptr2)[j] = sm; 
                    // }
                }
                else {
                    if (((*ptr1)[j] == INF) && (sm == INF))
                        (*ptr2)[j] = INF; 
                    else if ((*ptr1)[j] == INF) {
                        (*ptr2)[j] = sm; 
                    }
                    else if (sm == INF) {
                        (*ptr2)[j] = (*ptr1)[j]; 
                    }
                    else {
                        (*ptr2)[j] = sm + (*ptr1)[j]; 
                    }
                }
                if ((*ptr2)[j] == 0)
                    ret++; 
            }
            // for (int j = 0; j < n; j++)
            //     cout << (*ptr2)[j] << " "; 
            // cout << endl; 
            swap(ptr1, ptr2); 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<vector<char>> grid = {{'X','Y','.'},{'Y','.','.'}}; 
    // vector<vector<char>> grid = {{'.','.'},{'Y','X'}}; 
    int ret = s.numberOfSubmatrices(grid); 
    cout << "ans: " << ret << endl; 
    return 0; 
}
#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        unsigned int m = grid.size(), n = grid[0].size(); 
        int ret = 0; 
        vector<int> _psum_2d(n + 1, 0), psum_2d(n + 1, 0); 
        vector<int>* _psum_2d_ptr = &_psum_2d, *psum_2d_ptr = &psum_2d; 
        for (unsigned int i = 0; i < m; i++) { 
            if (i == 0) {
                for (unsigned int j = 0; j < n; j++) {
                    int acc = (*psum_2d_ptr)[j] + grid[i][j]; 
                    (*psum_2d_ptr)[j + 1] = acc; 
                    if (acc <= k) {
                        ret++; 
                        // cout << acc << endl; 
                    }
                    else {
                        break; 
                    }
                        
                }
            }
            else {
                int _acc = 0, acc = 0; 
                for (unsigned int j = 0; j < n; j++) {
                    _acc += grid[i][j]; 
                    acc = _acc + (*_psum_2d_ptr)[j + 1]; 
                    (*psum_2d_ptr)[j + 1] = acc; 
                    if (acc <= k) {
                        ret++; 
                        // cout << acc << endl; 
                    }
                    else 
                        break; 
                }
            }
            swap(psum_2d_ptr, _psum_2d_ptr); 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> grid = {{7,6,3},{6,6,1}}; 
    // int k = 18; 
    vector<vector<int>> grid = {{1,10},{7,2},{9,1},{4,1}}; 
    int k = 8; 
    int ret = s.countSubmatrices(grid, k); 
    cout << "ans: " << ret << endl; 
}
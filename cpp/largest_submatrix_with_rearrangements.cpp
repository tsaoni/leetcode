#include <iostream>
#include <vector>  

using namespace std; 
class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        unsigned int m = matrix.size(), n = matrix[0].size(); 
        vector<vector<int>> h1 = {}, h2 = {}; 
        vector<vector<int>>* prevH = &h1; 
        vector<vector<int>>* H = &h2; 
        // *prevH = {}; 
        int ret = 0; 
        for (int i = 0; i < m; i++) {
            // *H = {}; 
            vector<int> row = {}; 
            for (int j = 0; j < n; j++)
                row.push_back(matrix[i][j]); 
            int _h = 0, c = 0; 
            for (vector<int>& v: *prevH) {
                int h = v[0], col = v[1]; 
                if (row[col] == 1) {
                    if (_h != (h + 1)) {
                        ret = max(ret, _h * c); 
                    }
                    (*H).push_back({h + 1, col}); 
                    row[col] = 0; 
                    _h = h + 1; 
                    c++; 
                }   
            }
            ret = max(ret, _h * c); 
            for (int j = 0; j < n; j++) {
                if (row[j] == 1)
                    (*H).push_back({1, j}); 
            }
            ret = max(ret, static_cast<int>((*H).size())); 
            swap(prevH, H); 
            if (H == &h1) 
                h1 = {}; 
            else 
                h2 = {}; 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<vector<int>> matrix = {{0,0,1},{1,1,1},{1,0,1}}; 
    int ret = s.largestSubmatrix(matrix); 
    cout << "ans: " << ret << endl; 
    return 0; 
}
#include <iostream> 
#include <vector> 
#include <algorithm>
#include <cmath>

using namespace std; 

class Solution {
public:
    static int MAXV; 
    // int MAXV = 2 * pow(10, 5); 
    static int merge(vector<vector<int>>& ori, vector<vector<int>>& a, int vh, int c) {
        vector<vector<int>> res = {}; 
        vector<vector<int>>& rf = res; 
        unsigned int p1 = 0, p2 = 0; 
        int ret = MAXV; 
        // for (auto v: ori)
        //     cout << v[0] << " " << v[1] << " " << v[2] << endl; 
        while ((p1 < ori.size()) && (p2 < a.size())) {
            // cout << vh << " " << c << " " << ori[p1][0] << " " << ori[p1][1] << " " << ori[p1][2] << endl; 
            if (ori[p1][2 - vh] == c) {
                
                p1++; 
            }
            else {
                if (ori[p1][0] < a[p2][0]) {
                    if ((res.size() > 0) && ((ori[p1][0] - res.back()[0]) > 0))
                        ret = min(ret, ori[p1][0] - res.back()[0]); 
                    res.push_back(ori[p1]); 
                    p1++; 
                }
                else {
                    if ((res.size() > 0) && ((a[p2][0] - res.back()[0]) > 0))
                        ret = min(ret, a[p2][0] - res.back()[0]); 
                    res.push_back(a[p2]); 
                    p2++; 
                }   
            }
        }
        while (p1 < ori.size()) {
            if (ori[p1][2 - vh] == c) {
                p1++; 
                continue; 
            }
            if ((res.size() > 0) && ((ori[p1][0] - res.back()[0]) > 0))
                ret = min(ret, ori[p1][0] - res.back()[0]); 
            res.push_back(ori[p1]); 
            p1++; 
        }
        while (p2 < a.size()) {
            if ((res.size() > 0) && ((a[p2][0] - res.back()[0]) > 0))
                ret = min(ret, a[p2][0] - res.back()[0]); 
            res.push_back(a[p2]); 
            p2++; 
        }
        swap(ori, rf); 
        // for (auto x: ori)
        //     cout << x[0] << " "; 
        // cout << endl; 
        return (ret == MAXV)? 0: ret; 
    }
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        vector<vector<int>> w = {}, _w = {};
        unsigned int m = grid.size(), n = grid[0].size(); 
        int _k = k; 
        vector<vector<int>> ret(m - k + 1, vector<int>(n - _k + 1, 0)); 
        for (int i = 0; i <= (m - _k); i++) {
            if (i == 0) {
                for (int _i = 0; _i < _k; _i++)
                    for (int _j = 0; _j < _k; _j++)
                        w.push_back({grid[_i][_j], _i, _j}); 
                sort(w.begin(), w.end()); 
                // for (auto v: w)
                //     cout << v[0] << " " << v[1] << " " << v[2] << endl; 
                int minv = MAXV; 
                for (int _i = 1; _i < (_k * _k); _i++) {
                    int tmp = abs(w[_i][0] - w[_i - 1][0]); 
                    if (tmp > 0)
                        minv = min(minv, abs(w[_i][0] - w[_i - 1][0])); 
                }
                ret[0][0] = (minv == MAXV)? 0: minv; 
                _w = w; 
            }
            else {
                vector<vector<int>> a = {}; 
                for (int _i = 0; _i < _k; _i++)
                    a.push_back({grid[i + _k - 1][_i], i + _k - 1, _i}); 
                sort(a.begin(), a.end()); 
                ret[i][0] = merge(_w, a, 1, i - 1); 
                w = _w; 
            }
            for (int j = 1; j <= (n - _k); j++) {
                vector<vector<int>> a = {}; 
                for (int _i = 0; _i < _k; _i++)
                    a.push_back({grid[i + _i][j + _k - 1], i + _i, j + _k - 1}); 
                sort(a.begin(), a.end()); 
                ret[i][j] = merge(w, a, 0, j - 1); 
            }
        }
        return ret; 
    }
};
int Solution::MAXV = 2 * pow(10, 5) + 1; 

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> grid = {{1,8},{3,-2}}; 
    // int k = 2; 
    // vector<vector<int>> grid = {{1,-2,3},{2,3,5}}; 
    // int k = 2; 
    vector<vector<int>> grid = {{6509,-48222,-54280,4190},{-94342,29589,-89201,77939}}; 
    int k = 2; 
    vector<vector<int>> ret = s.minAbsDiff(grid, k); 
    cout << "ans:" << endl; 
    for (auto v: ret) 
        for (auto x: v)
            cout << x << " "; 
        cout << endl; 
    return 0; 
}
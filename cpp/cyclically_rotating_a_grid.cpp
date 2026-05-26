#include <iostream> 
#include <vector>

using namespace std; 
class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int n = grid.size(), m = grid[0].size(); 
        int up = 0, dn = n - 1, lf = 0, ri = m - 1; 
        vector<vector<int>> ret(n, vector<int>(m, 0)); 
        vector<vector<bool>> mod(n, vector<bool>(m, false)); 
        while (up < dn && lf < ri) {
            int si = up, sj = lf; 
            // int val = grid[si][sj]; 
            int cnt = 0, tot_cnt = 2 * ((dn - up) + (ri - lf)); 
            int _k = k % tot_cnt; 
            while (cnt < tot_cnt) {
                int ci = si, cj = sj; 
                int val = grid[si][sj]; 
                while (true) {
                    int acck = 0; 
                    while (acck < _k) {
                        if (cj == lf && ci < dn) {
                            int _ci = ci; 
                            int stp = _k - acck; 
                            ci = min(ci + stp, dn); 
                            acck += (ci - _ci); 
                        }
                        else if (cj == ri && ci > up) {
                            int _ci = ci; 
                            int stp = _k - acck; 
                            ci = max(ci - stp, up); 
                            acck += (_ci - ci); 
                        }
                        else if (ci == up && cj > lf) {
                            int _cj = cj; 
                            int stp = _k - acck; 
                            cj = max(cj - stp, lf); 
                            acck += (_cj - cj); 
                        }
                        else if (ci == dn && cj < ri) {
                            int _cj = cj; 
                            int stp = _k - acck; 
                            cj = min(cj + stp, ri); 
                            acck += (cj - _cj); 
                        }
                        // cout << ci << " " << cj << " " << acck << " " << _k << endl; 
                    }
                    if (mod[ci][cj])
                        break; 
                    // cout << ci << " " << cj << endl; 
                    ret[ci][cj] = val; 
                    swap(grid[ci][cj], val); 
                    mod[ci][cj] = true; 
                    cnt++; 
                } 
                if (sj == lf && si < dn) {
                    int _si = si; 
                    int stp = 1; 
                    si = min(si + stp, dn); 
                }
                else if (sj == ri && si > up) {
                    int _si = si; 
                    int stp = 1; 
                    si = max(si - stp, up); 
                }
                else if (si == up && sj > lf) {
                    int _sj = sj; 
                    int stp = 1; 
                    sj = max(sj - stp, lf); 
                }
                else if (si == dn && sj < ri) {
                    int _sj = sj; 
                    int stp = 1; 
                    sj = min(sj + stp, ri); 
                }
            }
            up++; 
            dn--; 
            lf++; 
            ri--; 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> grid = {{40,10},{30,20}}; 
    // int k = 1; 
    vector<vector<int>> grid = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}}; 
    int k = 2; 
    vector<vector<int>> ret = s.rotateGrid(grid, k); 
    for (auto& v: ret) {
        for (auto x: v)
            cout << x << " "; 
        cout << endl; 
    }
}
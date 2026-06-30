#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int zigZagArrays_1(int n, int l, int r) {
        int m = r - l + 1; 
        int modulo = 1e9 + 7; 
        if (n == 1)
            return m; 
        vector<vector<int>> _dp(m, vector<int>(2, 1)), dp(m, vector<int>(2, 1)); 
        _dp[0][0] = dp[0][0] = _dp[m - 1][1] = dp[m - 1][1] = 0; 
        vector<vector<int>> *prev = &_dp, *nxt = &dp; 
        int acc; 
        for (int i = 1; i < n; i++) {
            acc = 0; 
            for (int j = m - 1; j > 0; j--) {
                acc = (acc + (*prev)[j][0]) % modulo; 
                (*nxt)[j - 1][1] = acc; 
            }
            acc = 0; 
            for (int j = 0; j < m - 1; j++) {
                acc = (acc + (*prev)[j][1]) % modulo; 
                (*nxt)[j + 1][0] = acc; 
            }
            swap(prev, nxt); 
        }
        int ret = 0; 
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < 2; j++) 
                ret = (ret + (*prev)[i][j]) % modulo; 
        }
        return ret; 
    }

    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1; 
        long long modulo = 1e9 + 7; 
        if (n == 1)
            return m; 
        vector<long long> _dp(2 * m, 1), dp(2 * m, 1); 
        // _dp[0] = dp[2 * m - 1] = 0; 
        vector<long long> *prev = &_dp, *nxt = &dp; 
        long long acc, _acc; 
        
        vector<vector<long long>> _M(2 * m, vector<long long>(2 * m, 0)), M(2 * m, vector<long long>(2 * m, 0)); 
        vector<vector<long long>> *prev_m = &_M, *nxt_m = &M; 
        for (int i = 0; i < m - 1; i++) {
            for (int j = i + 1 + m; j < 2 * m; j++) {
                // cout << i << " " << j << " " << m << endl; 
                _M[i][j] = 1; 
                _M[2 * m - 1 - i][2 * m - 1 - j] = 1; 
            }
        }
        // cout << "here" << endl; 

        int cnt = n - 1; 
        while (cnt > 0) {
            if (cnt & 1) {
                for (int i = 0; i < 2 * m; i++) {
                    acc = 0; 
                    for (int j = 0; j < 2 * m; j++) {
                        acc += (*prev)[j] * (*prev_m)[i][j]; 
                        acc %= modulo; 
                    }
                    (*nxt)[i] = acc; 
                }
                swap(prev, nxt); 
            }
            for (int i = 0; i < 2 * m; i++) {
                for (int j = 0; j < 2 * m; j++) {
                    acc = 0; 
                    for (int k = 0; k < 2 * m; k++) {
                        acc += (*prev_m)[i][k] * (*prev_m)[k][j]; 
                        acc %= modulo; 
                    }
                    (*nxt_m)[i][j] = acc; 
                }
            }
            swap(prev_m, nxt_m); 
            cnt >>= 1; 
        }
        int ret = 0; 
        for (int i = 0; i < 2 * m; i++) {
            ret = (ret + (*prev)[i]) % modulo; 
        }
        return ret; 
    }
};


int main() {
    Solution s = Solution(); 
    int n = 3, l = 4, r = 5; 
    // int n = 3, l = 1, r = 3; 
    int ret = s.zigZagArrays(n, l, r); 
    cout << "ans: " << ret << endl; 
}
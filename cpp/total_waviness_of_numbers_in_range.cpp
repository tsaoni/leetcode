#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    // int d = 0; 
    // vector<int> dfs(int pos, int prev, int curr, bool leadZero, bool isUpper, int ***dp_cnt, int ***dp_wv) {
    //     for (int )
    // }

    long long n_wavs(long long n) {
        int d = 0; 
        long long tmp = n;
        vector<int> stk = {}; 
        while (tmp > 0) {
            stk.push_back(tmp % 10); 
            d++; 
            tmp /= 10; 
        } 
        if (d <= 2)
            return 0; 
        // for (int x: stk)
        //     cout << x << " "; 
        // cout << endl; 
        // index, prev, curr, leadingZero, isUpper
        long long dp_cnt[16][10][10][2][2], dp_wv[16][10][10][2][2]; 
        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < 10; k++) {
                    dp_cnt[i][j][k][0][0] = dp_cnt[i][j][k][0][1] = dp_cnt[i][j][k][1][0] = dp_cnt[i][j][k][1][1] = 0; 
                    dp_wv[i][j][k][0][0] = dp_wv[i][j][k][0][1] = dp_wv[i][j][k][1][0] = dp_wv[i][j][k][1][1] = 0; 
                }
            }
        }
        for (int i = 1; i < stk.back(); i++) {
            dp_cnt[0][0][i][1][0] = 1; 
        }
        dp_cnt[0][0][stk.back()][1][1] = 1; 
        
        for (int i = 1; i < d; i++) {
            int _i = d - 1 - i; 
            int _cur = stk[_i + 1], _pos = stk[_i]; 
            dp_cnt[i][_cur][_pos][0][1] = 1; 
            if (i > 1) {
                int _prev = stk[_i + 2]; 
                dp_wv[i][_cur][_pos][0][1] = dp_wv[i - 1][_prev][_cur][0][1]; 
            }
            
            // int add_cnt[10][10] = {0}; 
            // cout << "dp wv prev " << n << " " << i << endl; 
            // for (int _i = 0; _i < 10; _i++) {
            //     for (int j = 0; j < 10; j++)
            //         cout << dp_wv[i][_i][j][0][0] << " "; 
            //     cout << endl; 
            // }
            // cout << endl; 
            for (int pos = 0; pos < 10; pos++) {
                for (int cur = 0; cur < 10; cur++) {
                    if (cur == 0 && pos > 0) { // leading zero
                        // if (pos < stk[_i])
                        dp_cnt[i][cur][pos][1][0] = 1; 
                        // if (pos == stk[_i])  // is upper 
                        //     dp_cnt[i][cur][pos][1][1] = 1; 
                    }
                    
                    for (int prev = 0; prev < 10; prev++) {
                        dp_cnt[i][cur][pos][0][0] += (dp_cnt[i - 1][prev][cur][1][0] + dp_cnt[i - 1][prev][cur][0][0]); 
                        dp_wv[i][cur][pos][0][0] += (dp_wv[i - 1][prev][cur][0][0]); 
                        if (pos < stk[_i]) {
                            dp_cnt[i][cur][pos][0][0] += (dp_cnt[i - 1][prev][cur][1][1] + dp_cnt[i - 1][prev][cur][0][1]); 
                            dp_wv[i][cur][pos][0][0] += (dp_wv[i - 1][prev][cur][0][1]); 
                        }
                            
                        
                        
                        if ((i > 1) && ((cur < prev && cur < pos) || (cur > prev && cur > pos))) {
                            // if (cur == 0 && pos == 2) {
                            //     cout << "before " << cur << " " << pos << " " << dp_wv[i][cur][pos][0][0] << endl; 
                            // }
                            dp_wv[i][cur][pos][0][0] += dp_cnt[i - 1][prev][cur][0][0]; 
                            // add_cnt[cur][pos]++; 
                            // if (cur == 0 && pos == 2) {
                            //     cout << "after " << cur << " " << pos << " " << dp_wv[i][cur][pos][0][0] << endl; 
                            // }
    
                            if (pos < stk[_i])
                                dp_wv[i][cur][pos][0][0] += dp_cnt[i - 1][prev][cur][0][1]; 
                            else if (pos == stk[_i])
                                dp_wv[i][cur][pos][0][1] += dp_cnt[i - 1][prev][cur][0][1]; 
                        }
                        // if (dp_wv[i][cur][pos][1][0] > 0)
                        //     cout << "a" << endl; 
                        // if (dp_wv[i][cur][pos][1][1] > 0)
                        //     cout << "b" << endl; 
                    }
                    
                }
            }

            // cout << "add cnt " << n << " " << i << endl; 
            // for (int _i = 0; _i < 10; _i++) {
            //     for (int j = 0; j < 10; j++)
            //         cout << add_cnt[_i][j] << " "; 
            //     cout << endl; 
            // }
            // cout << endl; 

            // cout << "dp cnt " << n << " " << i << endl; 
            // for (int _i = 0; _i < 10; _i++) {
            //     for (int j = 0; j < 10; j++)
            //         cout << dp_cnt[i][_i][j][0][0] << " "; 
            //     cout << endl; 
            // }
            // cout << endl; 

            // cout << "dp wv " << n << " " << i << endl; 
            // for (int _i = 0; _i < 10; _i++) {
            //     for (int j = 0; j < 10; j++)
            //         cout << dp_wv[i][_i][j][0][0] << " "; 
            //     cout << endl; 
            // }
            // cout << endl; 

        }

        long long ret = 0; 
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++)
                ret += (dp_wv[d - 1][i][j][0][0] + dp_wv[d - 1][i][j][0][1] + dp_wv[d - 1][i][j][1][0] + dp_wv[d - 1][i][j][1][1]); 
        }
        return ret; 
    }

    long long totalWaviness(long long num1, long long num2) {
        long long x2 = n_wavs(num2), x1 = n_wavs(num1 - 1); 
        // cout << x2 << " " << x1 << endl; 
        return x2 - x1; 
    }
};

int main() {
    Solution s = Solution(); 
    // int num1 = 120, num2 = 130; 
    // int num1 = 198, num2 = 202; 
    // int num1 = 5720, num2 = 10850; 
    // int num1 = 1, num2 = 101; 
    long long num1 = 2549294942, num2 = 5067104447; 
    long long ret = s.totalWaviness(num1, num2); 
    cout << "ans: " << ret << endl; 
}
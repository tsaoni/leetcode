#include <iostream> 
#include <vector> 
#include <algorithm> 

using namespace std; 
class Solution {
public:
    vector<int> si = {0, 1, 8}; 
    vector<int> asi = {2, 5, 6, 9}; 
    vector<int> valid = {0, 1, 2, 5, 6, 8, 9}; 

    int count_in_range(vector<int>& cands, int x) {
        int cnt = 0; 
        for (int _x = 0; _x <= x; _x++) {
            if (find(cands.begin(), cands.end(), _x) != cands.end())
                cnt++; 
        }
        return cnt; 
    }

    int check_in_list(vector<int>& cands, int x) {
        return (find(cands.begin(), cands.end(), x) != cands.end()) ? 1: 0; 
    }

    int rotatedDigits(int n) {
        int d = 0; 
        int tmp = n; 
        vector<int> digits = {}; 
        while (tmp > 0) {
            d++; 
            digits.insert(digits.begin(), tmp % 10); 
            tmp /= 10; 
        }
        // n_digits, is_upper, have_diff
        vector<vector<vector<int>>> dp(d, vector<vector<int>>(2, vector<int>(2, 0))); 
        for (int i = 0; i < d; i++) {
            if (i == 0) {
                dp[i][0][0] = count_in_range(si, digits[i] - 1); 
                dp[i][0][1] = count_in_range(asi, digits[i] - 1); 
                dp[i][1][0] = check_in_list(si, digits[i]); 
                dp[i][1][1] = check_in_list(asi, digits[i]); 
            }
            else {
                dp[i][0][0] = dp[i - 1][0][0] * count_in_range(si, 9) + dp[i - 1][1][0] * count_in_range(si, digits[i] - 1); 
                dp[i][0][1] = dp[i - 1][0][0] * count_in_range(asi, 9) + dp[i - 1][1][0] * count_in_range(asi, digits[i] - 1) \
                 + dp[i - 1][0][1] * count_in_range(valid, 9) + dp[i - 1][1][1] * count_in_range(valid, digits[i] - 1); 
                dp[i][1][0] = dp[i - 1][1][0] * check_in_list(si, digits[i]); 
                dp[i][1][1] = dp[i - 1][1][0] * check_in_list(asi, digits[i]) + dp[i - 1][1][1] * check_in_list(valid, digits[i]); 
            }
        }
        
        int ret = 0; 
        for (int i = 0; i < 2; i++)
            ret += dp[d - 1][i][1]; 
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    int n = 2; 
    int ret = s.rotatedDigits(n); 
    cout << "ans: " << ret << endl; 
}
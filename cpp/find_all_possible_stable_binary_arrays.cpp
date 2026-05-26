#include <iostream> 
#include <vector> 
#include <cmath>

using namespace std; 
class Solution {
public:

    static inline void print_vec3d(vector<vector<vector<int>>> a, int c) {
        cout << "Start " << c << endl; 
        for(auto& v: a) {
            cout << "a "; 
            for(auto n: v)
                cout << n[0] << " x " << n[1] << " "; 
            cout << endl; 
        }
        cout << endl; 
    }

    int numberOfStableArrays(int zero, int one, int limit) {
        unsigned int modulo = pow(10, 9) + 7;
        vector<vector<vector<unsigned int>>> dp(zero + 1, vector<vector<unsigned int>>(one + 1, vector<unsigned int>(2, 0))); 
        for (int i = 1; i <= min(zero, limit); i++)
            dp[i][0][0] = 1; 
        for (int i = 1; i <= min(one, limit); i++)
            dp[0][i][1] = 1; 
        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]; 
                if (i > limit) 
                    dp[i][j][0] += (modulo - (dp[i - limit - 1][j][1])); 
                dp[i][j][1] = dp[i][j - 1][0] + dp[i][j - 1][1]; 
                if (j > limit) 
                    dp[i][j][1] += (modulo - (dp[i][j - limit - 1][0])); 

                dp[i][j][0] %= modulo; 
                dp[i][j][1] %= modulo; 
            }
        }
        // print_vec3d(dp, 0); 
        return (dp[zero][one][0] + dp[zero][one][1]) % modulo; 

    }
};

int main() {
    Solution s = Solution(); 
    // int zero = 1, one = 1, limit = 2; 
    // int zero = 1, one = 2, limit = 1; 
    int zero = 3, one = 3, limit = 2; 
    // int zero = 1, one = 3, limit = 1; 
    int ret = s.numberOfStableArrays(zero, one, limit); 
    cout << "ans: " << ret << endl; 
}
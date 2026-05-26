#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm> 

using namespace std; 
class Solution {
public:
    static long long inv(long long v, long long modulo) {
        long long p = modulo - 2; 
        long long m = v; 
        long long ret = 1; 
        while (p > 0) {
            if (p & 1)
                ret = (ret * m) % modulo; 
            p >>= 1; 
            m = (m * m) % modulo; 
        }
        return ret; 
    }

    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        long long modulo = pow(10, 9) + 7; 
        long long n = nums.size(); 
        long long th = ceil(sqrt(n)); 

        std::sort(queries.begin(), queries.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[2] < b[2]; 
        });

        vector<long long> df(n, 1); 
        int _k = 0; 
        for (auto& q: queries) {
            long long l = q[0], r = q[1], k = q[2], v = q[3]; 
            if (k >= th) {
                for (int i = l; i <= r; i += k) {
                    long long tmp = (static_cast<long long>(nums[i]) * v) % modulo; 
                    nums[i] = tmp; 
                }
            }
            else {
                if ((_k > 0) && (k != _k)) {
                    for (int i = 0; i < n; i++) {
                        if (i >= _k)
                            df[i] = (df[i - _k] * df[i]) % modulo; 
                        nums[i] = (static_cast<long long>(nums[i]) * df[i]) % modulo; 
                    }
                    for (int i = 0; i < n; i++)
                        df[i] = 1; 
                }
                df[l] = (df[l] * v) % modulo; 
                int R = l + (floor((r - l) / k) + 1) * k; 
                if (R < n)
                    df[R] = (df[R] * inv(v, modulo)) % modulo; 
                _k = k; 
            }
        }

        // for (auto x: df)
        //     cout << x << " "; 
        // cout << endl; 

        int ret = 0; 
        for (int i = 0; i < n; i++) {
            if (i >= _k)
                df[i] = (df[i - _k] * df[i]) % modulo; 
            int tmp = (static_cast<long long>(nums[i]) * df[i]) % modulo; 
            ret ^= tmp; 
        }

        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<int> nums = {1,1,1}; 
    vector<vector<int>> queries = {{0,2,1,4}}; 
    int ret = s.xorAfterQueries(nums, queries); 
    cout << "ans: " << ret << endl; 
}
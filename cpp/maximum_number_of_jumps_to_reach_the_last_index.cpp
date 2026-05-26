#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int maximumJumps(vector<int>& nums, int target) {
        int n = nums.size(); 
        vector<int> dp(n, -1); 
        dp[0] = 0; 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] >= 0 && abs(nums[j] - nums[i]) <= target)
                    dp[i] = max(dp[i], dp[j] + 1); 
            }
        }
        return dp.back(); 
    }
};
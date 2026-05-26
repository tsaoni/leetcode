#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size(); 
        vector<int> ret(n, 1), prev(n, 1), suf(n, 1); 
        suf[n - 1] = nums[n - 1]; 
        ret[0] = nums[0]; 
        for (int i = n - 1; i > 0; i--) 
            suf[i - 1] = min(nums[i - 1], suf[i]); 
        int max_n = nums[0]; 
        for (int i = n - 1; i > 0; i--) {
            max_n = max(max_n, nums[i]); 
            if (max_n <= suf[i])
                max_n = nums[i]; 
            // ret[n - 1] = max(ret[n - 1], nums[n - 1]); 
            ret[i] = max_n; 
        }
        return ret; 
    }
};
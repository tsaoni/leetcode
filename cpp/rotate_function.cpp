#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int ret = 0; 
        int sm = 0; 
        int n = nums.size(); 
        for (int i = 0; i < nums.size(); i++) {
            sm += nums[i]; 
            ret += (i * nums[i]); 
        }
        int tmp = ret; 
        for (int i = n - 1; i > 0; i--) {
            tmp = tmp + sm - n * nums[i]; 
            ret = max(ret, tmp); 
            // cout << ret << endl; 
        }
        return ret; 
    }
};
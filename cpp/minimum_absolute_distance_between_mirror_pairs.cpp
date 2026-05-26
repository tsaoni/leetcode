#include <vector> 
#include <iostream> 
#include <unordered_map> 

using namespace std; 
class Solution {
public:
    int reverse(int n) {
        int ret = 0; 
        bool start = false; 
        while (n > 0) {
            if ((n % 10) > 0)
                start = true; 
            if (start) 
                ret = ret * 10 + (n % 10); 
            n /= 10;  
        }
        return ret; 
    }

    int minMirrorPairDistance(vector<int>& nums) {
        int ret = -1; 
        unordered_map<int, int> mp; 
        for (int i = 0; i < nums.size(); i++) {
            if (mp.find(nums[i]) != mp.end())
                ret = (ret < 0) ? i - mp[nums[i]]: min(ret, i - mp[nums[i]]); 
            mp[reverse(nums[i])] = i; 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {12,21,45,33,54}; 
    vector<int> nums = {120,21}; 
    int ret = s.minMirrorPairDistance(nums); 
    cout << "ans: " << ret << endl; 
}
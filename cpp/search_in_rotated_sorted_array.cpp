#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1; 
        while (l < r) {
            int mid = (l + r + 1) / 2; 
            if (nums[l] < nums[r]) {
                if (target < nums[mid])
                    r = mid - 1; 
                else 
                    l = mid; 
            }
            else {
                if (nums[mid] >= nums[l]) {
                    if (target < nums[mid] && target >= nums[l])
                        r = mid - 1; 
                    else 
                        l = mid; 
                }
                else {
                    if (target >= nums[mid] && target <= nums[r])
                        l = mid; 
                    else 
                        r = mid - 1; 
                }
            }
            // cout << l << " " << r << endl; 
        }
        // cout << l << endl; 
        return (nums[l] == target) ? l: -1; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {4,5,6,7,0,1,2}; 
    // int target = 0; 
    // vector<int> nums = {4,5,6,7,0,1,2}; 
    // int target = 3; 
    vector<int> nums = {1}; 
    int target = 0; 
    int ret = s.search(nums, target); 
    cout << "ans: " << ret << endl; 
}
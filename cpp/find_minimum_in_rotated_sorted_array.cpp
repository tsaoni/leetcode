#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l + r) / 2; 
            if (nums[l] < nums[mid] && nums[r] < nums[mid])
                l = mid; 
            else if (nums[l] > nums[mid] && nums[r] > nums[mid])
                r = mid; 
            else if (nums[l] < nums[r]) {
                break; 
            }
            else {
                l = r; 
                break; 
            }
        } 
        return nums[l]; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {3,4,5,1,2}; 
    // vector<int> nums = {4,5,6,7,0,1,2}; 
    vector<int> nums = {1,2,0}; 
    int ret = s.findMin(nums); 
    cout << "ans: " << ret << endl; 
}
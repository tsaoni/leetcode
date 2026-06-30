#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int N = nums.size(); 
        vector<long long> pfx(2 * N + 1, 0); 
        long long psum = 0, psum_acc = 0, ret = 0; 
        for (int i = 0; i < N; i++) {
            int inc = (nums[i] == target) ? 1: -1; 
            if (inc > 0)
                psum_acc += pfx[psum + N]; 
            psum += inc; 
            if (inc < 0)
                psum_acc -= pfx[psum + N]; 
            pfx[psum + N]++; 
            ret += (psum > 0) ? psum_acc + 1: psum_acc; 
            // cout << psum_acc << " " << ret << endl; 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {1,2,2,3}; 
    // int target = 2; 
    vector<int> nums = {1,1,1,1}; 
    int target = 1; 
    long long ret = s.countMajoritySubarrays(nums, target); 
    cout << "ans: " << ret << endl; 
}
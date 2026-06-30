#include <iostream> 
#include <vector> 
#include <cmath> 

using namespace std; 
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int N = nums.size(); 
        int MAX_N = pow(10, 9); 
        vector<int> pref(N, nums[0]), suf(N, nums.back()); 
        for (int i = 1; i < N; i++) {
            pref[i] = max(nums[i], pref[i - 1]); 
            suf[N - 1 - i] = min(nums[N - i], suf[N - i]); 
        }
        vector<int> ret(N, 1); 
        // for (auto x: pref)
        //     cout << x << " "; 
        // cout << endl; 
        // for (auto x: suf)
        //     cout << x << " "; 
        // cout << endl; 
        int maxn = pref.back(); 
        for (int i = N - 1; i >= 0; i--) {
            if (pref[i] > suf[i]) 
                ret[i] = maxn; 
            else {
                ret[i] = pref[i]; 
                maxn = pref[i]; 
            }
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {2,1,3}; 
    vector<int> nums = {2,3,1}; 
    // vector<int> nums = {9,30,16,6,36,9}; 
    vector<int> ret = s.maxValue(nums); 
    cout << "ans: " << endl; 
    for (auto x: ret)
        cout << x << " "; 
    cout << endl; 
}
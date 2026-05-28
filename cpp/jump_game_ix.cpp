#include <iostream> 
#include <vector> 
#include <cmath> 

using namespace std; 
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int N = nums.size(); 
        int MAX_N = pow(10, 9); 
        vector<int> pref(N, 1), suf(N, 1); 
        for (int i = 0; i < N; i++) {
            pref[i] = max(nums[i], (i > 0) ? pref[i - 1]: 1); 
            suf[N - i - 1] = min(nums[N - i - 1], (i > 0) ? suf[N - i]: MAX_N); 
        }
        vector<int> ret(N, 1); 
        int cur = 0; 
        for (auto x: pref)
            cout << x << " "; 
        cout << endl; 
        for (auto x: suf)
            cout << x << " "; 
        cout << endl; 
        for (int i = 0; i < N; i++) {
            while (cur < N && pref[i] > suf[cur])
                cur++; 
            if (cur > i)
                ret[i] = pref[cur - 1]; 
            else 
                ret[i] = pref[cur]; 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {2,1,3}; 
    // vector<int> nums = {2,3,1}; 
    vector<int> nums = {9,30,16,6,36,9}; 
    vector<int> ret = s.maxValue(nums); 
    cout << "ans: " << endl; 
    for (auto x: ret)
        cout << x << " "; 
    cout << endl; 
}
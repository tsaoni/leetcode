#include <vector> 
#include <iostream> 
#include <unordered_map>
#include <utility> 

using namespace std; 
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        unordered_map<int, pair<int, int>> mpl, mpr; 
        int N = nums.size(); 
        vector<int> l(N, -1), r(N, -1); 
        for (int i = 0; i < N; i++) {
            if (mpl.find(nums[i]) != mpl.end()) {
                l[i] = mpl[nums[i]].second; 
            }
            else 
                mpl[nums[i]].first = i; 
            mpl[nums[i]].second = i; 
            if (mpr.find(nums[N - i - 1]) != mpr.end()) {
                r[N - i - 1] = mpr[nums[N - i - 1]].second; 
            }
            else 
                mpr[nums[N - i - 1]].first = N - i - 1; 
            mpr[nums[N - i - 1]].second = N - i - 1; 
        }
        for (const auto& [k, v]: mpl) {
            if (mpl[k].first != mpl[k].second)
                l[mpl[k].first] = mpl[k].second; 
        }
        for (const auto& [k, v]: mpr) {
            if (mpr[k].first != mpr[k].second)
                r[mpr[k].first] = mpr[k].second; 
        }
        // for (auto x: l)
        //     cout << x << " "; 
        // cout << endl; 
        // for (auto x: r)
        //     cout << x << " "; 
        // cout << endl; 
        vector<int> ret(queries.size(), -1); 
        for (int i = 0; i < queries.size(); i++) {
            int pos = queries[i]; 
            // cout << l[pos] << " " << r[pos] << endl; 
            if (l[pos] >= 0)
                ret[i] = min(abs(l[pos] - pos), N - abs(l[pos] - pos)); 
            if (r[pos] >= 0)
                ret[i] = (ret[i] < 0) ? min(abs(r[pos] - pos), N - abs(r[pos] - pos)): min(ret[i], min(abs(r[pos] - pos), N - abs(r[pos] - pos))); 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<int> nums = {1,3,1,4,1,3,2}; 
    vector<int> queries = {0,3,5}; 
    vector<int> ret = s.solveQueries(nums, queries); 
    cout << "ans: " << endl; 
    for (auto x: ret) 
        cout << x << " "; 
    cout << endl; 
}
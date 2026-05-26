#include <iostream> 
#include <vector> 
#include <unordered_map> 

using namespace std; 
class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        unordered_map <int, vector<long long>> pos; 
        unordered_map <int, long long> val, vpos; 
        for (int i = 0; i < nums.size(); i++) {
            if (pos.find(nums[i]) == pos.end()) {
                pos[nums[i]] = {}; 
                vpos[nums[i]] = 0; 
            }
            pos[nums[i]].push_back(i); 
            val[nums[i]] += i - pos[nums[i]][0]; 
        }
        vector<long long> ret = {}; 
        for (int i = 0; i < nums.size(); i++) {
            ret.push_back(val[nums[i]]); 
            int vp = vpos[nums[i]], n = pos[nums[i]].size(); 
            int dist = (vp < pos[nums[i]].size() - 1) ? pos[nums[i]][vp + 1] - pos[nums[i]][vp]: 0; 
            val[nums[i]] += (dist * (2 * (vp + 1) - n)); 
            vpos[nums[i]]++; 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<int> nums = {1,3,1,1,2}; 
    vector<long long> ret = s.distance(nums); 
    cout << "ans: " << endl; 
    for (auto x: ret)
        cout << x << " "; 
    cout << endl; 
}
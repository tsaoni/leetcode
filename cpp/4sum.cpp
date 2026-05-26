#include <iostream> 
#include <algorithm> 
#include <vector> 
#include <numeric>

using namespace std; 

class Solution {
    public: 
    vector<vector<int>> fres; 
    
    static inline void print_vec2d(vector<vector<int>> a, int c) {
        cout << "Start " << c << endl; 
        for(auto& v: a) {
            cout << "a "; 
            for(auto n: v)
                cout << n << " "; 
            cout << endl; 
        }
        cout << endl; 
    }

    static inline void print_vec1d(vector<int> a, int c) {
        cout << "Start " << c << endl; 
        cout << "a "; 
        for(auto& v: a) {
            cout << v << " "; 
        }
        cout << endl; 
    }

    static inline int search(int left, int right, int th, vector<int>& nums) {
        int l = left, r = right; 
        while(l < r) {
            int mid = (l + r + 1) / 2; 
            if(nums[mid] < th) 
                l = mid; 
            else 
                r = mid - 1; 
        }
        if(nums[l] >= th)
            return l; 
        return (l == right) ? -1: (l + 1);
    }

    void find(vector<int>& nums, vector<int>& cur, int target, long sm, long acc_c) {
       
        if(cur.size() == 4) {
            vector<int> v = {}; 
            int acc = 0; 
            for(auto x: cur) {
                v.push_back(nums[x]); 
                acc += nums[x]; 
            }
            // print_vec1d(v, 1); 
            if(acc == target)
                fres.push_back(v); 
        }   
        else if (cur.size() == 2) {
            long t = static_cast<long>(target) - acc_c;  
            int start = cur.back() + 1, end = static_cast<int>(nums.size()) - 1; 
            // cout << start << " " << end << endl; 
            while (start < end) {
                int _start; 
                for (_start = start; _start < end; _start++) {
                    if ((_start == start) || (nums[_start] != nums[_start - 1])) {
                        if (static_cast<long>(nums[_start]) + static_cast<long>(nums[end]) == t) {
                            // cout << cur[0] << " " << cur[1] << " " << _start << " " << end << endl; 
                            fres.push_back({nums[cur[0]], nums[cur[1]], nums[_start], nums[end]}); 
                            break; 
                        }
                        else if (static_cast<long>(nums[_start]) + static_cast<long>(nums[end]) > t) {
                            // _start--; 
                            break; 
                        }
                    }
                }
                start = _start; 
                while ((end > 0) && (nums[end - 1] == nums[end]))
                    end--;
                end--;  
            }

        }   
        else {
            // print_vec1d(cur, 1); 
            int last_idx = (cur.size() == 0) ? -1: cur.back(); 
            int i = last_idx; 
            int n = static_cast<int>(nums.size()); 
            int n_cur = static_cast<int>(cur.size()); 
            int idx = n - (4 - n_cur); 
            long th = sm - nums[idx]; 
            long _th = target - th - acc_c; 
            // idx = search(i, idx, _th, nums); 
            while(i < idx) {
                i++; 
                // int _i = search(i, idx, _th, nums); 
                // if (_i < 0) break; 
                // cout << i << "r " << idx << "th " << _th << "i " << _i << endl; 
                if(((i - 1) == last_idx) || (i > 0 && nums[i] != nums[i - 1])) {
                // if((i > 0 && nums[i] != nums[i - 1])) {
                    // i = _i; 
                    if(i >= 0) {
                        if(static_cast<long>(nums[i]) + static_cast<long>(acc_c) < static_cast<long>(target) - static_cast<long>(th))
                            continue; 
                        cur.push_back(i); 
                        // cout << cur.size() << " " << i << " " << idx << " " << _th << endl; 
                        find(nums, cur, target, th, acc_c + static_cast<long>(nums[i])); 
                        cur.pop_back(); 
                        _th = nums[i] + 1; 
                        // cout << _th << endl; 
                    }
                }
                // i = _i; 
            }
        }
    }

    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end()); 
        // for(int i = 0; i < nums.size(); i++)
        //     cout << nums[i] << " "; 
        vector<int> cur = {}; 
        if(nums.size() >= 4) {
            long sm = std::accumulate(nums.end() - 4, nums.end(), 0L);
            // cout << sm << endl;
            find(nums, cur, target, sm, 0); 
        }
        
        return fres; 
    }
}; 

int main() {
    // vector<int> nums = {1,0,-1,0,-2,2}; 
    // int target = 0; 
    vector<int> nums = {1000000000,1000000000,1000000000,1000000000}; 
    int target = 0; 
    Solution s = Solution(); 
    vector<vector<int>> res = s.fourSum(nums, target); 
    Solution::print_vec2d(res, 2); 
    return 0; 
}
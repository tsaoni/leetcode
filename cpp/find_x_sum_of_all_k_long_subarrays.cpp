#include <iostream> 
#include <vector> 
#include <set> 
#include <utility>
#include <unordered_map>

using namespace std; 
class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        long long xsum = 0; 
        multiset<pair<int, int>> xs, s; 
        unordered_map<int, int> xmp, mp;
        vector <long long> ret = {}; 
        for (int i = 0; i < nums.size(); i++) {
            if (true) {
                if (xmp.find(nums[i]) != xmp.end()) {
                    // cout << "c 1 " << xsum << endl; 
                    auto p = make_pair(xmp[nums[i]], nums[i]); 
                    auto it = xs.find(p);
                    xs.erase(it); 
                    p = make_pair(xmp[nums[i]] + 1, nums[i]); 
                    xs.insert(p); 
                    xsum += nums[i]; 
                    xmp[nums[i]]++; 
                }
                else if (mp.find(nums[i]) != mp.end()) {
                    // cout << "c 2 " << xsum << endl; 
                    auto p = make_pair(mp[nums[i]], nums[i]); 
                    auto it = s.find(p);
                    s.erase(it); 
                    auto _p = *xs.begin(); 
                    // cout << _p.first << " " << _p.second << endl; 
                    p = make_pair(mp[nums[i]] + 1, nums[i]); 
                    // cout << p.first << " " << p.second << endl; 
                    mp.erase(nums[i]); 
                    if (p > _p) {
                        // cout << "xx" << endl; 
                        xs.erase(xs.begin()); 
                        xs.insert(p); 
                        xsum -= static_cast<long long>(_p.first) * static_cast<long long>(_p.second); 
                        xsum += static_cast<long long>(p.first) * static_cast<long long>(p.second); 
                        xmp.erase(_p.second); 
                        xmp[p.second] = p.first; 
                        s.insert(_p); 
                        mp[_p.second] = _p.first; 

                    }
                    else {
                        s.insert(p); 
                        // xsum += nums[i]; 
                        mp[p.second] = p.first; 
                    }
                }
                else {
                    // cout << "c 3 " << xsum << endl; 
                    if (xmp.size() < x) {
                        auto p = make_pair(1, nums[i]); 
                        xs.insert(p); 
                        xsum += nums[i]; 
                        xmp[nums[i]] = 1; 
                    }
                    else {
                        auto p = make_pair(1, nums[i]); 
                        auto _p = *xs.begin(); 
                        if (p > _p) {
                            xs.erase(xs.begin()); 
                            xs.insert(p); 
                            xsum -= static_cast<long long>(_p.first) * static_cast<long long>(_p.second); 
                            xsum += static_cast<long long>(p.first) * static_cast<long long>(p.second); 
                            xmp.erase(_p.second); 
                            xmp[p.second] = p.first; 
                            s.insert(_p); 
                            mp[_p.second] = _p.first; 
                        }
                        else {
                            s.insert(p); 
                            mp[p.second] = p.first; 
                        }
                    }
                }
            }
            if (i >= k) {
                if (xmp.find(nums[i - k]) != xmp.end()) {
                    // cout << "b 1 " << xsum << endl; 
                    auto p = make_pair(xmp[nums[i - k]], nums[i - k]); 
                    auto it = xs.find(p);
                    xs.erase(it); 
                    xsum -= nums[i - k]; 
                    xmp[nums[i - k]]--; 
                    if (xmp[nums[i - k]] == 0) {
                        xmp.erase(nums[i - k]); 
                        if (mp.size() > 0) {
                            auto p = *s.rbegin(); 
                            s.erase(prev(s.end())); 
                            mp.erase(p.second); 
                            xs.insert(p); 
                            xsum += static_cast<long long>(p.first) * static_cast<long long>(p.second); 
                            xmp[p.second] = p.first; 
                        }
                    }
                    else {
                        // cout << "x " << xsum << endl; 
                        if (mp.size() > 0) {
                            auto p = make_pair(xmp[nums[i - k]], nums[i - k]); 
                            auto _p = *s.rbegin(); 
                            if (_p > p) {
                                s.erase(prev(s.end())); 
                                mp.erase(_p.second); 
                                s.insert(p); 
                                mp[p.second] = p.first; 
                                xs.insert(_p); 
                                xsum -= static_cast<long long>(p.first) * static_cast<long long>(p.second); 
                                // cout << "x " << xsum << endl; 
                                xsum += static_cast<long long>(_p.first) * static_cast<long long>(_p.second); 
                                // cout << "x " << xsum << " " << _p.first << " " << _p.second << " " << nums[i - k] << endl; 
                                xmp.erase(p.second); 
                                xmp[_p.second] = _p.first; 
                            }
                            else {
                                xs.insert(p); 
                            }
                        }
                        else {
                            auto p = make_pair(xmp[nums[i - k]], nums[i - k]); 
                            xs.insert(p); 
                        }
                    }
                }
                else if (mp.find(nums[i - k]) != mp.end()) {
                    // cout << "b 2 " << xsum << endl; 
                    auto p = make_pair(mp[nums[i - k]], nums[i - k]); 
                    auto it = s.find(p);
                    s.erase(it); 
                    mp[nums[i - k]]--; 
                    if (mp[nums[i - k]] == 0) {
                        mp.erase(nums[i - k]); 
                    }
                    else {
                        auto p = make_pair(mp[nums[i - k]], nums[i - k]); 
                        s.insert(p); 
                    }
                }
                else 
                    cout << "error" << endl; 
            }
            if (i >= (k - 1)) 
                ret.push_back(xsum); 
            // cout << i << " " << xsum << endl; 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {1,1,2,2,3,4,2,3}; 
    // int k = 6; 
    // int x = 2; 
    // vector<int> nums = {3,8,7,8,7,5}; 
    // int k = 2; 
    // int x = 2; 
    vector<int> nums = {2,3,2,1,3,5,3,1}; 
    int k = 6; 
    int x = 1; 
    
    vector<long long> ret = s.findXSum(nums, k, x); 
    cout << "ans: " << endl; 
    for (long long x: ret) 
        cout << x << " "; 
    cout << endl; 
    return 0; 
}
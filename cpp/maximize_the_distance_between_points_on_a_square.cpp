#include <vector> 
#include <iostream> 
#include <algorithm> 

using namespace std; 
class Solution {
public:
    bool valid_min_dist_recur(int limit, vector<int>& val, int k, int idx, vector<int>& selected, int side) {
        if (idx == val.size())
            return false; 
        // cout << idx << endl; 
        if ((selected.size() == 0) || ((selected.size() > 0) && val[idx] - val[selected.back()] >= limit))
            selected.push_back(idx); 
        else 
            return false; 
        
        if (selected.size() == k) {
            // for (auto x: selected)
            //     cout << val[x] << " "; 
            // cout << endl; 
            if ((val[selected.back()] - val[selected[0]]) <= (4 * side - limit))
                return true; 
            else {
                selected.pop_back(); 
                return false; 
            }
        }
        else {
            for (int i = idx + 1; i < val.size(); i++) {
                if (valid_min_dist_recur(limit, val, k, i, selected, side))
                    return true; 
            }
            // cout << "xx" << endl; 
            selected.pop_back(); 
            return false; 
        }

    }

    bool valid_min_dist(long long limit, vector<long long>& val, int k, int idx, long long side) {
    
        // cout << idx << endl; 
        // vector<int> selected = {}; 
        int last = -1, cnt = 0; 
        int first = -1; 
        for (int i = idx; i < val.size(); i++) {
            if (cnt == k) break; 
            if ((cnt == 0) || ((cnt > 0) && val[i] - val[last] >= limit)) {
                if (cnt == 0) first = i; 
                last = i; 
                cnt++; 
            }
                
        }
        
        // for (auto x: selected)
        //     cout << x << " "; 
        // cout << endl; 
        if (cnt == k) {
            // for (auto x: selected)
            //     cout << val[x] << " "; 
            // cout << endl; 
            if ((val[last] - val[first]) <= (4 * side - limit))
                return true; 
        }
        return false; 
    }

    int maxDistance(int side, vector<vector<int>>& points, int k) {
        vector<long long> val = {}; 
        for (vector<int>& p: points) {
            long long v; 
            long long sd = side, p0 = p[0], p1 = p[1]; 
            if (p[0] == 0)
                v = p1; 
            else if (p[1] == side)
                v = sd + p0; 
            else if (p[0] == side)
                v = 3 * sd - p1; 
            else 
                v = 4 * sd - p0; 
            val.push_back(v); 
            // cout << p[0] << " " << p[1] << " " << v << endl; 
        }
        sort(val.begin(), val.end()); 
        long long l = 0, r = side; 
        while (l < r) {
            long long mid = (l + r + 1) / 2; 
            
            bool valid = false; 
            for (int idx = 0; idx <= (val.size() / k + 1); idx++) {
                // vector<int> selected = {}; 
                if (valid_min_dist(mid, val, k, idx, side)) {
                    valid = true; 
                    break; 
                }
                    
            }
            if (valid)
                l = mid; 
            else 
                r = mid - 1; 
            
        }
        // vector<int> selected = {}; 
        // for (auto x: val)
        //     cout << x << " "; 
        // cout << endl; 
        // cout << valid_min_dist(8, val, k, 0, selected, side) << endl; 
        return l; 
    }
};

int main() {
    Solution s = Solution(); 
    // int side = 2; 
    // vector<vector<int>> points = {{0,2},{2,0},{2,2},{0,0}}; 
    // int k = 4; 
    // int side = 2; 
    // vector<vector<int>> points = {{0,0},{1,2},{2,0},{2,2},{2,1}}; 
    // int k = 4; 
    
    int side = 13; 
    vector<vector<int>> points = {{5,0},{0,3},{9,13},{0,0},{0,13},{10,13}}; 
    int k = 4; 
    int ret = s.maxDistance(side, points, k); 
    cout << "ans: " << ret << endl; 
}
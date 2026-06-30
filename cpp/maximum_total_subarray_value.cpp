#include <iostream> 
#include <vector> 
#include <queue> 
#include <cmath> 

using namespace std; 
struct SegNode {
    int mn, mx, mn_idx, mx_idx;
};

class SegTree {
public:
    vector<int> T_mn = {}, T_mx = {}; 
    vector<int> T_mn_idx = {}, T_mx_idx = {}; 
    vector<int> nums; 
    int N; 
    int MX_VAL = 1e9; 
    SegTree(vector<int> arr) {
        N = arr.size(); 
        nums = arr; 
        for (int i = 0; i < 4 * N; i++) {
            T_mn.push_back(0); 
            T_mx.push_back(0); 
            T_mn_idx.push_back(0); 
            T_mx_idx.push_back(0); 
        }
        build(0, N - 1, 0); 
        // for (int i = 0; i < 4 * N; i++)
        //     cout << T_mx_idx[i] << " "; 
        // cout << endl; 
    }
    SegNode build(int l, int r, int cur) {
        if (l == r) {
            T_mn[cur] = nums[l]; 
            T_mx[cur] = nums[l]; 
            T_mn_idx[cur] = l; 
            T_mx_idx[cur] = l; 
            return {nums[l], nums[l], l, l}; 
        }
        int mid = (l + r) / 2; 
        SegNode _l = build(l, mid, 2 * cur + 1); 
        SegNode _r = build(mid + 1, r, 2 * cur + 2); 
        int mn = min(_l.mn, _r.mn), mx = max(_l.mx, _r.mx); 
        int mn_idx = (_l.mn <= _r.mn) ? _l.mn_idx: _r.mn_idx; 
        int mx_idx = (_l.mx >= _r.mx) ? _l.mx_idx: _r.mx_idx; 
        T_mn[cur] = mn; 
        T_mx[cur] = mx; 
        T_mn_idx[cur] = mn_idx; 
        T_mx_idx[cur] = mx_idx; 
        return {mn, mx, mn_idx, mx_idx}; 
    }

    SegNode query(int l, int r, int cur, int cl, int cr) {
        if (l == cl && r == cr) {
            return {T_mn[cur], T_mx[cur], T_mn_idx[cur], T_mx_idx[cur]}; 
        }
        int cmid = (cl + cr) / 2; 
        int mn = MX_VAL, mx = 0; 
        int mn_idx = N - 1, mx_idx = N - 1; 
        if (l <= cmid) {
            int _r = min(r, cmid); 
            SegNode v = query(l, _r, 2 * cur + 1, cl, cmid); 
            if (mn > v.mn)
                mn_idx = v.mn_idx; 
            else if (mn == v.mn)
                mn_idx = min(mn_idx, v.mn_idx); 
            // cout << mx << " " << mx_idx << endl; 
            if (mx < v.mx)
                mx_idx = v.mx_idx; 
            else if (mx == v.mx)
                mx_idx = min(mx_idx, v.mx_idx); 
            // cout << mx << " " << mx_idx << endl; 
            mn = min(mn, v.mn); 
            mx = max(mx, v.mx); 
            // mn_idx = (mn == v[0]) ? min(mn_idx, v[2]): mn_idx; 
            // mx_idx = (mx == v[1]) ? min(mx_idx, v[3]): mx_idx; 
            // cout << mx << " " << v[1] << " " << mx_idx << " " << v[0] << " " << v[3] << "x" << endl; 
        }
        if (r > cmid) {
            int _l = max(l, cmid + 1); 
            SegNode v = query(_l, r, 2 * cur + 2, cmid + 1, cr); 
            if (mn > v.mn)
                mn_idx = v.mn_idx; 
            else if (mn == v.mn)
                mn_idx = min(mn_idx, v.mn_idx); 
            // cout << mx << " " << mx_idx << endl; 
            if (mx < v.mx)
                mx_idx = v.mx_idx; 
            else if (mx == v.mx)
                mx_idx = min(mx_idx, v.mx_idx); 
            // cout << mx << " " << mx_idx << endl; 
            mn = min(mn, v.mn); 
            mx = max(mx, v.mx); 
            // mn_idx = (mn == v[0]) ? min(mn_idx, v[2]): mn_idx; 
            // mx_idx = (mx == v[1]) ? min(mx_idx, v[3]): mx_idx; 
            // cout << mx << " " << v[1] << " " << mx_idx << " " << v[0] << "y" << endl; 
        }
        return {mn, mx, mn_idx, mx_idx}; 
    }
};

struct State {
    int diff;
    int l;
    int r;
    int mn_idx; 
    int mx_idx; 

    State(int d, int left, int right, int mn_idx, int mx_idx) : diff(d), l(left), r(right), mn_idx(mn_idx), mx_idx(mx_idx) {}

    bool operator<(const State& other) const {
        return diff < other.diff;
    }
};

class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        SegTree st = SegTree(nums); 
        priority_queue<State> pq;
        int N = nums.size(); 
        for (int l = 0; l < N; l++) {
            SegNode val = st.query(l, N - 1, 0, 0, N - 1); 
            // cout << val[0] << " " << val[1] << " " << val[2] << " " << val[3] << endl; 
            pq.emplace(val.mx - val.mn, l, N - 1, val.mn_idx, val.mx_idx); 
        }

        long long ret = 0; 
        int cnt = 0; 
        int acc = 0; 
        while (cnt < k) {
            // acc++; 
            // if (acc < 10) break; 
            State v = pq.top(); 
            pq.pop(); 
            
            int idx = max(v.mn_idx, v.mx_idx); 
            int inc = min(k - cnt, v.r - idx + 1); 
            
            // cout << v.diff << " " << v.l << " " << v.r << " " << idx << endl; 
            // if (v.r < idx) break; 
            ret += static_cast<long long>(v.diff) * static_cast<long long>(inc); 
            cnt += inc; 
            // cout << cnt << endl; 
            
            if (v.l < idx) {
                // cout << "xx" << endl; 
                SegNode val = st.query(v.l, idx - 1, 0, 0, N - 1); 
                pq.emplace(val.mx - val.mn, v.l, idx - 1, val.mn_idx, val.mx_idx); 
                // cout << val[1] - val[0] << " " << v.l << " " << idx - 1 << " " << val[2] << " " << val[3] << endl; 
            }
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {1,3,2}; 
    // int k = 2; 
    // vector<int> nums = {4,2,5,1}; 
    // int k = 3; 
    vector<int> nums = {9,9,37}; 
    int k = 3; 
    // vector<int> nums = {11,8}; 
    // int k = 3; 
    int ret = s.maxTotalValue(nums, k); 
    cout << "ans: " << ret << endl; 
}
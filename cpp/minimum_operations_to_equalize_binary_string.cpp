#include <iostream>
#include <string>
#include <vector>
#include <numeric>

using namespace std; 

class Solution {
public:
    static int count_one(string s) {
        int cnt = 0; 
        for (auto c: s) {
            if (c == '1') 
                cnt++; 
        } 
        return cnt; 
    }

    static vector<int> get_range(vector<int>& v, int minv, int maxv) {
        int N = static_cast<int>(v.size()); 
        int l = 0, r = N - 1; 
        // cout << "unset: "; 
        // for (auto x: v)
        //     cout << x; 
        // cout << endl; 
        while (l < r) {
            // cout << "l: " << l << "r: " << r << endl; 
            int mid = (l + r) / 2; 
            if (v[mid] < minv) 
                l = mid + 1; 
            else 
                r = mid; 
        }
        // cout << "l: " << l << endl; 
        vector<int> ret = {}; 
        // cout << "N: " << N << endl; 
        if (v[l] < minv || N == 0) 
            return ret; 
        else {
            // cout << "r: "; 
            while (r < N && v[r] <= maxv) {
                ret.push_back(v[r]); 
                r++; 
                // cout << r << " "; 
                // v.erase(v.begin() + l); 
            }
            // cout << endl; 
            v.erase(v.begin() + l, v.begin() + r); 
            return ret; 
        }
    }

    int minOperations(string s, int k) {
        int N = static_cast<int>(s.size()); 
        vector<int> dist(N + 1, -1);
        vector<int> q = {}; 
        vector<int> unset_odd = {}, unset_even = {}; 
        for (int i = 0; i <= N; i++) {
            if (i % 2 == 0)
                unset_even.push_back(i); 
            else 
                unset_odd.push_back(i); 
        }
        int n1 = count_one(s); 
        if (n1 == N)
            return 0; 
        dist[n1] = 0; 
        // unset.erase(unset.begin() + n1); 
        vector<int>& unset = (n1 % 2 == 0) ? unset_even: unset_odd; 
        get_range(unset, n1, n1); 
        q.push_back(n1); 
        int step = 0; 
        while (q.size() > 0) {
            step++; 
            int d = q.front(); 
            int n1 = d, n0 = N - d; 
            int n0_flip_max = min(k, N - d); 
            int n0_flip_min = k - min(d, k); 
            int n1_flip_min = k - n0_flip_max; 
            int n1_flip_max = k - n0_flip_min; 
            int _n1_max = n1 - n1_flip_min + n0_flip_max; 
            int _n1_min = n1 - n1_flip_max + n0_flip_min; 
            vector<int>& unset = (_n1_min % 2 == 0) ? unset_even: unset_odd; 
            vector<int> v = get_range(unset, _n1_min, _n1_max); 
            // cout << _n1_min << " mm " << _n1_max << endl; 

            // for (int n0_flip = n0_flip_min; n0_flip <= n0_flip_max; n0_flip++) {
            for (auto _n1: v) {
                // int n1_flip = k - n0_flip; 
                // n0 = n0 - n0_flip + n1_flip;  
                // int _n1 = n1 - n1_flip + n0_flip; 
                // cout << d << " " << step << " " << _n1 << endl; 
                // cout << _n1 << " "; 
                if (dist[_n1] < 0) {
                    dist[_n1] = dist[d] + 1; 
                    q.push_back(_n1); 
                    if (_n1 == N) 
                        return dist[_n1]; 
                }
            }
            // cout << endl; 
            q.erase(q.begin()); 
        }
        return -1; 
    }
};

int main() {
    Solution sol = Solution(); 
    // string s = "010"; 
    // int k = 1; 
    string s = "01"; 
    int k = 2; 
    int ret = sol.minOperations(s, k); 
    cout << "ans: " << ret << endl; 
}
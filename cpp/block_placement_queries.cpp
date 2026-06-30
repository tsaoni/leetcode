#include <iostream> 
#include <vector> 
#include <set> 
#include <cmath> 
#include <iterator>

using namespace std; 

class BIT {
private:
    vector<int> arr;
    int M; 
public:
    BIT(int M): arr(vector<int>(M, 0)), M(M) { }
    ~BIT() { }
    
    int lowbit(int x) {
        return x & -x; 
    }

    void update(int pos, int x) {
        for (int p = pos; p < M; p += lowbit(p)) {
            arr[p] = max(x, arr[p]); 
        }
    }

    int query(int pos) {
        int ret = -1; 
        for (int p = pos; p > 0; p -= lowbit(p)) {
            // cout << p << " " << M << endl; 
            ret = max(ret, arr[p]); 
        }
        return ret; 
    }
    
}; 

class Solution {
public:

    vector<bool> getResults(vector<vector<int>>& queries) {
        int M = 0, Q = queries.size(); 
        for (vector<int>& v: queries) 
            M = max(v[1], M); 

        set<int> s; 
        int B = 5 * pow(10, 4) + 1; 
        s.insert(0); 
        s.insert(B); 
        BIT *bit = new BIT(M + 1); 
        for (vector<int>& v: queries) {
            if (v[0] == 1) {
                s.insert(v[1]); 
            }
        }
        
        int pre = 0, idx = 0; 
        // vector<int> pre(M + 1, 0); 
        for (const int x: s) {
            if (x > 0 && x < B) {
                bit -> update(x, x - pre); 
                // while (idx <= x) {
                //     pre[idx] = prev; 
                //     idx++; 
                // }
            }
            pre = x; 
        }

        vector<bool> stk = {}, ret = {}; 
        for (int i = Q - 1; i >= 0; i--) {
            vector<int>& v = queries[i]; 
            // auto it; 
            int pv, nv; 
            int x, sz, val, max_len; 

            switch (v[0]) {
                case 1: {
                    auto it = s.find(v[1]); 
                    pv = *prev(it), nv = *next(it); 
                    if (nv < B) {
                        bit -> update(nv, nv - pv); 
                        // cout << "xx " << v[1] << " " << nv << " " << pv << endl; 
                    }
                    s.erase(v[1]); 
                    break; 
                }
                case 2:
                    x = v[1], sz = v[2]; 
                    val = *prev(s.lower_bound(x)); 
                    // cout << x <<  "xx" << val << endl; 
                    max_len = bit -> query(val); 
                    // cout << max_len << " " << x << " " << sz << endl; 
                    // cout << x - val << endl; 
                    max_len = max(max_len, x - val); 
                    stk.push_back((max_len >= sz) ? true: false); 
                    break;

                default:
                    break;
            }
            
        }
        while (stk.size() > 0) {
            ret.push_back(stk.back()); 
            stk.pop_back(); 
        }
            
        return ret; 
        
    }
};

int main() {
    Solution s = Solution(); 
    vector<vector<int>> queries = {{1,2},{2,3,3},{2,3,1},{2,2,2}}; 
    // vector<vector<int>> queries = {{1,7},{2,7,6},{1,2},{2,7,5},{2,7,6}}; 
    vector<bool> ret = s.getResults(queries); 
    cout << "ans: " << endl; 
    for (auto x: ret)
        cout << x << " "; 
    cout << endl; 
}
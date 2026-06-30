#include <iostream> 
#include <vector> 
#include <unordered_map> 
#include <unordered_set>
#include <cmath> 

using namespace std; 

struct RetData {
    int n_odd, n_even, depth;
};

class Solution {
public:
    int find_depth(int cur, int depth, unordered_map<int, unordered_set<int>>& T, vector<bool>& visited) {
        visited[cur - 1] = true; 
        int d = depth; 
        for (int nxt: T[cur]) {
            // cout << nxt << endl; 
            if (!visited[nxt - 1]) {
                int _d = find_depth(nxt, depth + 1, T, visited); 
                d = max(d, _d); 
            }
        }
        return d; 
    }

    int fast_exp(int base, int exp) {
        unsigned long long modulo = 1e9 + 7; 
        unsigned long long res = 1, mul = base; 
        while (exp > 0) {
            if (exp & 1) {
                res = (res * mul) % modulo; 
            }
            mul = (mul * mul) % modulo; 
            exp >>= 1; 
        }
        return static_cast<int>(res); 
    }

    RetData dfs(int cur, int depth, unordered_map<int, unordered_set<int>>& T, vector<bool>& visited) {
        visited[cur - 1] = true; 
        auto ret_1_or_val = [](int x) {
            return (x == 0) ? 1: x;
        };
        int n_odd = 0, n_even = 0, n_ignore = 0, d = depth; 
        bool last_node = true; 
        for (int nxt: T[cur]) {
            // cout << nxt << endl; 
            if (!visited[nxt - 1]) {
                RetData x = dfs(nxt, depth + 1, T, visited); 
                if (x.depth > d) {
                    d = x.depth; 
                    n_ignore = ret_1_or_val(n_ignore) * (n_odd + n_even); // still will have errors..
                    n_odd = x.n_odd; 
                    n_even = x.n_even; 
                }
                else if (x.depth < d) {
                    n_ignore = ret_1_or_val(n_ignore) * (x.n_odd + x.n_even); 
                }
                else {
                    n_odd = ret_1_or_val(n_odd) * x.n_odd; 
                    n_even = ret_1_or_val(n_even) * x.n_even; 
                }
                last_node = false; 
            }
        }
        cout << cur << " " << n_odd << " " << n_even << " " << d << " " << last_node << endl; 
        if (last_node)
            return {1, 1, d}; 
        else
            return {n_odd * ret_1_or_val(n_ignore), n_even * ret_1_or_val(n_ignore), d}; 
    }

    int _assignEdgeWeights(vector<vector<int>>& edges) {
        unordered_map<int, unordered_set<int>> T; 
        int N = 0; 
        for (vector<int>& v: edges) {
            if (T.find(v[0]) == T.end())
                T[v[0]] = unordered_set<int>{}; 
            T[v[0]].insert(v[1]); 
            N = max(N, v[0]); 

            if (T.find(v[1]) == T.end())
                T[v[1]] = unordered_set<int>{}; 
            T[v[1]].insert(v[0]); 
            N = max(N, v[1]); 

        }
        vector<bool> visited(N, false); 
        RetData x = dfs(1, 0, T, visited); 
        return x.n_odd; 
    }

    int assignEdgeWeights(vector<vector<int>>& edges) {
        unordered_map<int, unordered_set<int>> T; 
        int N = 0; 
        for (vector<int>& v: edges) {
            if (T.find(v[0]) == T.end())
                T[v[0]] = unordered_set<int>{}; 
            T[v[0]].insert(v[1]); 
            N = max(N, v[0]); 

            if (T.find(v[1]) == T.end())
                T[v[1]] = unordered_set<int>{}; 
            T[v[1]].insert(v[0]); 
            N = max(N, v[1]); 

        }
        vector<bool> visited(N, false); 
        int depth = find_depth(1, 0, T, visited); 
        return (depth == 0) ? 0: fast_exp(2, depth - 1); 
    
    }

    // vector<int> stk = {}; 
    void build_table(int cur, int prev, int d, vector<int>& depths, vector<vector<int>>& pre, unordered_map<int, unordered_set<int>>& T) {
        depths[cur] = d; 
        if (prev >= 0) {
            pre[cur][0] = prev; 
            int log_N = pre[cur].size(); 
            for (int k = 1; k < log_N; k++) {
                if (pre[cur][k - 1] >= 0)
                    pre[cur][k] = pre[pre[cur][k - 1]][k - 1]; 
                else 
                    break; 
            }
        }

        // stk.push_back(cur); 
        for (int nxt: T[cur]) {
            if (depths[nxt] < 0) {
                build_table(nxt, cur, d + 1, depths, pre, T); 
            }
        }
        // stk.pop_back(); 
    }

    int lca(int v1, int v2, vector<int>& depths, vector<vector<int>>& pre) {
        int d1 = depths[v1], d2 = depths[v2]; 
        int n_edges = 0; 
        // cout << d1 << " " << d2 << endl; 
        while (d1 > d2) {
            int exp = floor(log2(d1 - d2)); 
            int offset = fast_exp(2, exp); 
            v1 = pre[v1][exp]; 
            d1 -= offset; 
            n_edges += offset; 
        }
        while (d2 > d1) {
            int exp = floor(log2(d2 - d1)); 
            int offset = fast_exp(2, exp); 
            v2 = pre[v2][exp]; 
            d2 -= offset; 
            n_edges += offset; 
        }
        // cout << d1 << endl; 
        while (v1 != v2) {
            // cout << v1 << " " << v2 << endl; 
            int exp = floor(log2(d1)); 
            for (int k = exp; k >= 0; k--) {
                if (pre[v1][k] != pre[v2][k] || k == 0) {
                    int offset = fast_exp(2, k); 
                    v1 = pre[v1][k]; 
                    v2 = pre[v2][k]; 
                    d1 -= offset; 
                    n_edges += (2 * offset); 
                    break; 
                }
            }
        }
        return (n_edges == 0) ? 0: fast_exp(2, n_edges - 1); 
    }

    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int N = 0; 
        unordered_map<int, unordered_set<int>> T; 
        for (vector<int>& v: edges) {
            N = max(N, v[0]); 
            N = max(N, v[1]); 
            if (T.find(v[0] - 1) == T.end())
                T[v[0] - 1] = unordered_set<int>{};
            T[v[0] - 1].insert(v[1] - 1);  
            if (T.find(v[1] - 1) == T.end())
                T[v[1] - 1] = unordered_set<int>{};
            T[v[1] - 1].insert(v[0] - 1);  
        }
        
        vector<int> depths(N, -1); 
        int log_N = ceil(log2(N));
        vector<vector<int>> pre(N, vector<int>(log_N, -1)); 
        build_table(0, -1, 0, depths, pre, T); 
        // for (int i = 0; i < N; i++) {
        //     for (int j = 0; j < log_N; j++)
        //         cout << pre[i][j] << " "; 
        //     cout << endl; 
        // }

        vector<int> ret = {}; 
        for (vector<int>& q: queries) {
            ret.push_back(lca(q[0] - 1, q[1] - 1, depths, pre)); 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> edges = {{1,2}}; 
    // vector<vector<int>> queries = {{1,1},{1,2}}; 
    vector<vector<int>> edges = {{1,2},{1,3},{3,4},{3,5}}; 
    vector<vector<int>> queries = {{1,4},{3,4},{2,5}}; 
    vector<int> ret = s.assignEdgeWeights(edges, queries); 
    cout << "ans: " << endl; 
    for (int x: ret)
        cout << x << " "; 
    cout << endl; 
}
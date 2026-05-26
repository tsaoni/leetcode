#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <cmath> 
#include <functional> 

using namespace std; 
class Solution {
public:

    static int find(vector<int>& parent, int idx) {
        if (parent[idx] == -1)
            return idx; 
        parent[idx] = find(parent, parent[idx]); 
        return parent[idx]; // (parent[idx] >= 0) ? find(parent, parent[idx]) : idx; 
    }

    int maxStability(int n, vector<vector<int>>& edges, int k) {
        vector<int> parent(n, -1); 
        // vector<vector<int>> child(n, vector<int>()); 
        sort(edges.begin(), edges.end()); 
        int min_init = 2 * pow(10, 5); 
        vector<vector<int>> q = {}; 

        int add = 0; 
        for (vector<int>& v: edges) {
            if (v[3] == 0) 
                q.push_back({v[2], v[0], v[1]}); 
            else {
                int p0 = find(parent, v[0]), p1 = find(parent, v[1]);  
                if (p0 != p1) { 
                    if (p1 > p0) 
                        swap(p0, p1); 
                    parent[p1] = p0; 
                    // child[p0].push_back(p1); 
                    // for (auto& x: child[p1]) {
                    //     parent[x] = p0; 
                    //     child[p0].push_back(x); 
                    // }
                    // child[p1] = {}; 
                }
                else 
                    return -1; 
                min_init = min(min_init, v[2]); 
                add++; 
            }   
            // for (auto x: parent) 
            //     cout << x << " "; 
            // cout << endl; 
        }

        sort(q.begin(), q.end(), greater<vector<int>>()); 
        vector<int> ev = {}; 
        for (vector<int>& v: q) {
            if (add == (n - 1)) 
                break; 
            int p0 = find(parent, v[1]), p1 = find(parent, v[2]); 
            if (p0 != p1) {
                if (p1 > p0) 
                    swap(p0, p1); 
                parent[p1] = p0; 
                // child[p0].push_back(p1); 
                // for (auto& x: child[p1]) {
                //     parent[x] = p0; 
                //     child[p0].push_back(x); 
                // }
                // child[p1] = {}; 
                ev.push_back(v[0]); 
                add++; 
            }
        }
        if (add != (n - 1))
            return -1; 

        if (ev.size() > 0) {
            min_init = min(min_init, ev.back() * 2); 
            int i = (ev.size() - 1 - k); 
            if (i >= 0)
                min_init = min(min_init, ev[i]); 
        }
        return min_init; 
    }
};

int main() {
    Solution s = Solution(); 
    int n = 3; 
    vector<vector<int>> edges = {{0,1,2,1},{1,2,3,0}}; 
    int k = 1; 

    // int n = 3; 
    // vector<vector<int>> edges = {{0,1,4,0},{1,2,3,0},{0,2,1,0}}; 
    // int k = 2; 

    // int n = 3;
    // vector<vector<int>> edges = {{0,1,1,1},{1,2,1,1},{2,0,1,1}}; 
    // int k = 0; 

    int ret = s.maxStability(n, edges, k); 
    cout << "ans: " << ret << endl; 
    return 0; 
}
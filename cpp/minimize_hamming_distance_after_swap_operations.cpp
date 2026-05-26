#include <iostream> 
#include <vector> 
#include <unordered_set> 
#include <unordered_map> 

using namespace std; 
class Solution {
public:
    int find(vector<int>& p, int x) {
        int root = x; 
        while (p[root] >= 0)
            root = p[root]; 
        while (x != root) {
            int tmp = p[x]; 
            p[x] = root; 
            x = tmp; 
        }
        return root; 
    }
    int minimumHammingDistance_1(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int N = source.size(); 
        vector<int> p(N, -1); 
        for (auto& v: allowedSwaps) {
            int p0 = find(p, v[0]), p1 = find(p, v[1]); 
            p[p0] = p1; 
        }
        unordered_map<int, unordered_set<int>> mp; 
        for (int i = 0; i < N; i++) {
            int _p = find(p, i); 
            if (mp.find(_p) == mp.end())
                mp[_p] = unordered_set<int>{}; 
            mp[_p].insert(i); 
        }
        int d = 0; 
        for (const auto& [root, s] : mp) {
            unordered_map<int, int> cntr_src, cntr_tgt; 
            for (int x: s) {
                if (cntr_src.find(source[x]) == cntr_src.end())
                    cntr_src[source[x]] = 0; 
                cntr_src[source[x]]++; 
                if (cntr_tgt.find(target[x]) == cntr_tgt.end())
                    cntr_tgt[target[x]] = 0; 
                cntr_tgt[target[x]]++; 
            }
            for (const auto& [val, cnt] : cntr_tgt) {
                if (cntr_src.find(val) == cntr_src.end())
                    d += cnt; 
                else 
                    d += (cnt - cntr_src[val]); 
            }
        }
        return d; 
    }

    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int N = source.size(); 
        vector<int> p(N, -1); 
        unordered_map<int, unordered_map<int, int>> cntr_src; 
        int d = 0; 
        for (auto& v: allowedSwaps) {
            int p0 = find(p, v[0]), p1 = find(p, v[1]); 
            if (p0 == p1) continue;  
            p[p0] = p1;
        }
        for (int i = 0; i < N; i++) {
            int p1 = find(p, i); 
            if (cntr_src.find(p1) == cntr_src.end())
                cntr_src[p1] = unordered_map<int, int>(); 
            if (cntr_src[p1].find(source[i]) == cntr_src[p1].end())
                cntr_src[p1][source[i]] = 1; 
            else
                cntr_src[p1][source[i]] ++; 
        }
        
        // for (const auto& [root, c] : cntr_src) {
        //     cout << root << endl; 
        //     for (const auto& [val, cnt] : c)
        //         cout << val << " " << cnt << endl; 
        // }
        for (int i = 0; i < N; i++) {
            int _p = find(p, i); 
            if (cntr_src[_p].find(target[i]) == cntr_src[_p].end())
                d++; 
            else if (cntr_src[_p][target[i]] == 0)
                d++; 
            else 
                cntr_src[_p][target[i]]--; 
        }
        return d; 

    }

};

int main() {
    Solution s = Solution(); 
    // vector<int> source = {1,2,3,4}; 
    // vector<int> target = {2,1,4,5}; 
    // vector<vector<int>> allowedSwaps = {{0,1},{2,3}}; 
    vector<int> source = {1,2,3,4}; 
    vector<int> target = {1,3,2,4}; 
    vector<vector<int>> allowedSwaps = {}; 
    int ret = s.minimumHammingDistance(source, target, allowedSwaps); 
    cout << "ans: " << ret << endl; 
}
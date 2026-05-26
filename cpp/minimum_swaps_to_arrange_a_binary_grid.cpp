#include <iostream> 
#include <numeric>
#include <vector>

using namespace std; 
class Solution {
public:
    static vector<int> countz(vector<vector<int>>& grid) {
        int nr = static_cast<int>(grid.size()), nc = static_cast<int>(grid[0].size()); 
        vector<int> v(nr, 0); 
        for (int j = 0; j < nr; j++) {
            for (int i = nc - 1; i >= 0; i--) {
                if (grid[j][i] != 0) 
                    break; 
                v[j]++; 
            } 
        }
        return v; 
    }
    int minSwaps(vector<vector<int>>& grid) {
        int N = static_cast<int>(grid.size()); 
        vector<int> cntz = countz(grid); 
        // vector<int> inds(N); 
        // iota(inds.begin(), inds.end(), 0);
        // for (auto c: cntz)
        //     cout << c << " "; 
        // cout << endl; 
        int ret = 0; 
        for (int i = 0; i < N; i++) {
            int th = N - i - 1; 
            int j = i; 
            while (j < N && cntz[j] < th)
                j++; 
            // cout << j << endl; 
            if (j == N) 
                return -1; 
            else {
                int t = cntz[j]; 
                cntz.erase(cntz.begin() + j); 
                cntz.insert(cntz.begin() + i, t); 
                ret += (j - i); 
                // t = inds[j]; 
                // inds.erase(j); 
                // inds.insert(cntz.begin() + i, t); 
            }
        }
        return ret; 
        // vector<vector<int>> rearranged;
        // rearranged.reserve(N); 

        // for (int idx: inds) {
        //     rearranged.push_back(move(grid[idx]));
        // }
        // return rearranged; 
    }
};

int main() {
    Solution s = Solution(); 
    std::vector<std::vector<int>> grid = {
        {0, 0, 1},
        {1, 1, 0},
        {1, 0, 0}
    };
    int ret = s.minSwaps(grid); 
    cout << "ans: " << ret << endl; 
}
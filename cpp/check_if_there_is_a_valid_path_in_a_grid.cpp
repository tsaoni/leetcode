#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        int ci = 0, cj = 0; 
        int n = grid.size(), m = grid[0].size(); 
        // int pi = -1, pj = -1; 
        // switch (grid[0][0]) {
        //     case 1:
        //         pi = 0, pj = -1; 
        //         break; 
        //     case 2:
        //         pi = -1, pj = 0; 
        //         break; 
        //     case 3:
        //         pi = 0, pj = -1; 
        //         break; 
        //     case 6:
        //         pi = -1, pj = 0; 
        //         break; 
        // }
        // int i = 0; 
        vector<vector<bool>> visited(n, vector<bool>(m, false)); 
        vector<vector<int>> q = {{0, 0}}; 
        while (q.size() > 0) {
            // i++; 
            // cout << pi << " " << pj << endl; 
            // cout << ci << " " << cj << endl; 
            // cout << endl; 
            int ci = q[0][0], cj = q[0][1]; 
            visited[ci][cj] = true; 
            q.erase(q.begin());
            if ((ci == n - 1) && (cj == m - 1)) {
                // if ((grid[ci][cj] == 1) || (grid[ci][cj] == 2) || (grid[ci][cj] == 3) || (grid[ci][cj] == 6))
                return true; 
                // else 
                //     return false; 
            }
                
            switch (grid[ci][cj]) {
                case 1:
                    if (true) {
                        if ((cj + 1 == m)) {

                        }
                        else if (!visited[ci][cj + 1]) {
                            if ((grid[ci][cj + 1] == 1) || (grid[ci][cj + 1] == 3) || (grid[ci][cj + 1] == 5)) {
                                q.push_back({ci, cj + 1}); 
                            }
                        }
                    }
                    if (true) {
                        if ((cj - 1 < 0)) {

                        }
                        else if (!visited[ci][cj - 1]) {
                            if ((grid[ci][cj - 1] == 1) || (grid[ci][cj - 1] == 4) || (grid[ci][cj - 1] == 6)) {
                                q.push_back({ci, cj - 1}); 
                            }
                        }
                    }
                    break;
                case 2:
                    if (true) {
                        if ((ci + 1 == n)) {

                        }
                        else if (!visited[ci + 1][cj]) {
                            if ((grid[ci + 1][cj] == 2) || (grid[ci + 1][cj] == 5) || (grid[ci + 1][cj] == 6)) {
                                q.push_back({ci + 1, cj}); 
                            }
                        }
                        
                    } 
                    if (true) {
                        if ((ci - 1 < 0)) {

                        }
                        else if (!visited[ci - 1][cj]) {
                            if ((grid[ci - 1][cj] == 2) || (grid[ci - 1][cj] == 3) || (grid[ci - 1][cj] == 4)) {
                                q.push_back({ci - 1, cj}); 
                            }
                        }
                    }
                    break;
                case 3:
                    if (true) {
                        if ((ci + 1 == n)) {

                        }
                        else if (!visited[ci + 1][cj]) {
                            if ((grid[ci + 1][cj] == 2) || (grid[ci + 1][cj] == 5) || (grid[ci + 1][cj] == 6)) {
                                q.push_back({ci + 1, cj}); 
                            }
                        }
                    }
                    if (true) {
                        if ((cj - 1 < 0)) {

                        }
                        else if (!visited[ci][cj - 1]) {
                            if ((grid[ci][cj - 1] == 1) || (grid[ci][cj - 1] == 4) || (grid[ci][cj - 1] == 6)) {
                                q.push_back({ci, cj - 1}); 
                            }
                        }
                    }
                    break;
                case 4:
                    if (true) {
                        if ((ci + 1 == n)) {

                        }
                        else if (!visited[ci + 1][cj]) {
                            if ((grid[ci + 1][cj] == 2) || (grid[ci + 1][cj] == 5) || (grid[ci + 1][cj] == 6)) {
                                q.push_back({ci + 1, cj}); 
                            }
                        }
                    }
                    if (true) {
                        if ((cj + 1 == m)) {

                        }
                        else if (!visited[ci][cj + 1]) {
                            if ((grid[ci][cj + 1] == 1) || (grid[ci][cj + 1] == 3) || (grid[ci][cj + 1] == 5)) {
                                q.push_back({ci, cj + 1}); 
                            }
                        }
                    }
                    break;
                case 5:
                    if (true) {
                        if ((cj - 1 < 0)) {

                        }
                        else if (!visited[ci][cj - 1]) {
                            if ((grid[ci][cj - 1] == 1) || (grid[ci][cj - 1] == 4) || (grid[ci][cj - 1] == 6)) {
                                q.push_back({ci, cj - 1}); 
                            }
                        }
                    }
                    if (true) {
                        if ((ci - 1 < 0)) {

                        }
                        else if (!visited[ci - 1][cj]) {
                            if ((grid[ci - 1][cj] == 2) || (grid[ci - 1][cj] == 3) || (grid[ci - 1][cj] == 4)) {
                                q.push_back({ci - 1, cj}); 
                            }
                        }
                    }
                    
                    break;
                case 6:
                    if (true) {
                        if ((cj + 1 == m)) {

                        }
                        else if (!visited[ci][cj + 1]) {
                            if ((grid[ci][cj + 1] == 1) || (grid[ci][cj + 1] == 3) || (grid[ci][cj + 1] == 5)) {
                                q.push_back({ci, cj + 1}); 
                            }
                        }
                    }
                    if (true) {
                        if ((ci - 1 < 0)) {

                        }
                        else if (!visited[ci - 1][cj]) {
                            if ((grid[ci - 1][cj] == 2) || (grid[ci - 1][cj] == 3) || (grid[ci - 1][cj] == 4)) {
                                q.push_back({ci - 1, cj}); 
                            }
                        }
                    }
                    
                    break;
                default:
                    break; 
            }
            // pi = ci, pj = cj; 
        }
        return false; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<vector<int>> grid = {{2,4,3},{6,5,2}}; 
    // vector<vector<int>> grid = {{1,2,1},{1,2,1}}; 
    vector<vector<int>> grid = {{4,1},{6,1}}; 
    bool ret = s.hasValidPath(grid); 
    cout << "ans: " << ret << endl; 
}
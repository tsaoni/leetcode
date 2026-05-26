#include <vector>
#include <iostream>
#include <utility>
#include <cmath>
#include <unordered_map>
#include <algorithm> 

using namespace std; 

class Solution {
public:
    int search(vector<int> v, int val, int ori) {
        int l = 0, r = v.size() - 1;
        while (l < r) {
            if (ori == 0) {
                int mid = (l + r + 1) / 2; 
                if (val > v[mid]) 
                    l = mid; 
                else 
                    r = mid - 1; 
            }
            else {
                int mid = (l + r) / 2; 
                if (val < v[mid]) 
                    r = mid; 
                else 
                    l = mid + 1; 
            }
        } 
        if (ori == 0)
            return (v[l] >= val) ? -1: l; 
        else
            return (v[l] <= val) ? -1: l; 
    }

    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int ret = 0; 
        vector<int> ori = {1, 0, -1, 0}; 
        pair<int, int> cur = make_pair(0, 0), dir = make_pair(1, 0); 
        
        unordered_map<int, vector<int>> mpx, mpy; 
        sort(obstacles.begin(), obstacles.end()); 
        for (auto& v: obstacles) {
            // cout << v[0] << " " << v[1] << endl; 
            if (mpx.find(v[0]) == mpx.end())
                mpx[v[0]] = {}; 
            mpx[v[0]].push_back(v[1]); 
            // cout << mpx[v[0]][0] << mpx[v[0]].back() << endl; 
            
            if (mpy.find(v[1]) == mpy.end())
                mpy[v[1]] = {}; 
            mpy[v[1]].push_back(v[0]); 
        }
        // if (find(mpx[0].begin(), mpx[0].end(), -3) == mpx[0].end())
        //     cout << "err" << endl; 
            

        for (auto x: commands) {
            if (x == -1) {
                dir.first = (dir.first + 3) % 4; 
                dir.second = (dir.second + 3) % 4; 
            }
            else if (x == -2) {
                dir.first = (dir.first + 1) % 4; 
                dir.second = (dir.second + 1) % 4; 
            }
            else {
                // cout << "dir " << dir.first << " " << dir.second << endl; 
                if ((mpy.find(cur.second) != mpy.end()) && ori[dir.first] != 0) {
                    
                    if (ori[dir.first] > 0) {
                        int idx = search(mpy[cur.second], cur.first, 1); 
                        int src = cur.first, dest = cur.first + ori[dir.first] * x; 
                        if (idx >= 0) 
                            cur.first = min(mpy[cur.second][idx] - 1, dest); 
                        else 
                            cur.first = dest; 
                    }
                    else {
                        int idx = search(mpy[cur.second], cur.first, 0); 
                        int src = cur.first, dest = cur.first + ori[dir.first] * x; 
                        if (idx >= 0) 
                            cur.first = max(mpy[cur.second][idx] + 1, dest); 
                        else 
                            cur.first = dest; 
                    }
                }
                else
                    cur.first += (ori[dir.first] * x); 
                
                if ((mpx.find(cur.first) != mpx.end()) && ori[dir.second] != 0) {
                    if (ori[dir.second] > 0) {
                        int idx = search(mpx[cur.first], cur.second, 1); 
                        // cout << "xxx "<< idx << endl; 
                        int src = cur.second, dest = cur.second + ori[dir.second] * x; 
                        if (idx >= 0) 
                            cur.second = min(mpx[cur.first][idx] - 1, dest); 
                        else 
                            cur.second = dest; 
                    }
                    else {
                        int idx = search(mpx[cur.first], cur.second, 0); 
                        // cout << "xxx "<< idx << endl; 
                        int src = cur.second, dest = cur.second + ori[dir.second] * x; 
                        if (idx >= 0) 
                            cur.second = max(mpx[cur.first][idx] + 1, dest); 
                        else 
                            cur.second = dest; 
                    }
                }
                else
                    cur.second += (ori[dir.second] * x); 
                ret = max(ret, (static_cast<int>(pow(cur.first, 2) + pow(cur.second, 2)))); 
                
            }
            // cout << cur.first << " " << cur.second << endl; 
        }
        return ret; 
    }
};

class Robot {
private: 
    int width, height; 
    int sp; 
    int idx, d; 
    bool start; 
    vector<vector<int>> start_pos;  
    vector<vector<int>> dir; 
    vector<string> dirs; 

public:
    Robot(int width, int height) {
        this -> width = width; 
        this -> height = height; 
        this -> sp = height - 1; 
        this -> idx = 3; 
        this -> d = 0; 
        // this -> start = true; 
        this -> start_pos = {{0, 0}, {width - 1, 0}, {width - 1, height - 1}, {0, height - 1}}; 
        this -> dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}}; 
        this -> dirs = {"East", "North", "West", "South"}; 
    }
    
    void step(int num) {
        int _idx = num / (width + height - 2); 
        int _sp = num % (width + height - 2); 
        sp += _sp; 
        if (sp > (width + height - 2)) {
            idx += 2; 
            sp -= (width + height - 2); 
        }
        else if ((idx == 0) || (idx == 2)) {
            if (sp > (width - 1)) {
                sp -= (width - 1); 
                idx++; 
            }
        }
        else {
            if (sp > (height - 1)) {
                sp -= (height - 1); 
                idx++; 
            }
        }
        idx += (2 * _idx); 
        idx %= 4; 
        // sp = _sp; 
        d = idx; 
        // start = false; 
    }
    
    vector<int> getPos() {
        // cout << sp << " " << idx << endl; 
        return {start_pos[idx][0] + dir[idx][0] * sp, start_pos[idx][1] + dir[idx][1] * sp}; 
    }
    
    string getDir() {
        return dirs[d]; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> commands = {4,-1,3}; 
    // vector<vector<int>> obstacles = {};  
    // vector<int> commands = {4,-1,4,-2,4}; 
    // vector<vector<int>> obstacles = {{2,4}}; 
    // vector<int> commands = {6,-1,-1,6}; 
    // vector<vector<int>> obstacles = {{0,0}}; 
    // vector<int> commands = {-2,-1,8,9,6}; 
    // vector<vector<int>> obstacles = {{-1,3},{0,1},{-1,5},{-2,-4},{5,4},{-2,-3},{5,-1},{1,-1},{5,5},{5,2}}; 
    vector<int> commands = {7,-2,-2,7,5}; 
    vector<vector<int>> obstacles = {{-3,2},{-2,1},{0,1},{-2,4},{-1,0},{-2,-3},{0,-3},{4,4},{-3,3},{2,2}}; 
    int ret = s.robotSim(commands, obstacles); 
    cout << "ans: " << ret << endl; 
}
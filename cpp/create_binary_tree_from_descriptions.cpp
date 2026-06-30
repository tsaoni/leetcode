#include <iostream> 
#include <vector> 
#include <unordered_map> 

// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class Solution {
public:
    TreeNode *dfs(int cur, unordered_map<int, vector<vector<int>>>& mp) {
        TreeNode *cur_node = new TreeNode(cur); 
        for (vector<int>& v: mp[cur]) {
            if (v[1] == 0)
                cur_node -> right = dfs(v[0], mp); 
            else 
                cur_node -> left = dfs(v[0], mp); 
        }
        return cur_node; 
    }
    
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, vector<vector<int>>> mp; 
        unordered_map<int, int> p; 
        for (vector<int>& v: descriptions) {
            int parent = v[0], child = v[1], isLeft = v[2]; 
            if (mp.find(parent) == mp.end()) {
                mp[parent] = {}; 
            }
            mp[parent].push_back({child, isLeft}); 
            if (p.find(parent) == p.end())
                p[parent] = -1; 
            p[child] = parent; 
        }
        int root = -1; 
        for (auto& x: p) {
            if (x.second < 0) {
                root = x.first; 
                break; 
            }
        }
        return dfs(root, mp); 

    }
};
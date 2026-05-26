#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size(); 
        int start = 0, end = n - 1; 
        while (start < end) {
            for (int i = start; i < end; i++) {
                int tmp = matrix[start][i]; 
                matrix[start][i] = matrix[n - 1 - i][start]; 
                matrix[n - 1 - i][start] = matrix[n - 1 - start][n - 1 - i]; 
                matrix[n - 1 - start][n - 1 - i] = matrix[i][n - 1 - start]; 
                matrix[i][n - 1 - start] = tmp; 
            }
            start++; 
            end--; 
        }
    }
};
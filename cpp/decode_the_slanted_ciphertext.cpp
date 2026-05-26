#include <iostream> 
#include <string> 

using namespace std; 
class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        int col = encodedText.size() / rows; 
        int it = col - rows + 1; 
        string ret = ""; 
        for (int start = 0; start < (it + 1); start++) {
            for (int i = 0; i < rows; i++) {
                int j = i + start; 
                if (j == col)
                    break; 
                ret += encodedText[i * col + j]; 
            }
        }
        int i = ret.size() - 1; 
        while ((i >= 0) && (ret[i] == ' ')) {
            ret.pop_back(); 
            i--; 
        }
            
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    string encodedText = "ch   ie   pr"; 
    int rows = 3; 
    // string encodedText = "iveo    eed   l te   olc"; 
    // int rows = 4; 
    string ret = s.decodeCiphertext(encodedText, rows); 
    cout << "ans: " << ret << endl; 
}
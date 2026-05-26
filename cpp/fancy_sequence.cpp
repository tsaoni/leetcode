#include <iostream> 
#include <vector> 
#include <cmath> 

using namespace std; 
class Fancy {
private: 
    vector<int> v = {}; 
    vector<vector<long>> params = {}; 
    long al = 1, bl = 0; 
    long modulo = pow(10, 9) + 7; 
public:
    Fancy() {

    }
    
    void append(int val) {
        v.push_back(val); 
        params.push_back({al, bl}); 
        return; 
    }
    
    void addAll(int inc) {
        bl = (bl + inc) % modulo; 
        return; 
    }
    
    void multAll(int m) {
        al = (m * al) % modulo; 
        bl = (m * bl) % modulo; 
        return; 
    }
    
    long inverse(int x) {
        long exp = modulo - 2L; 
        long p, mul = 1, x; 
        while (exp > 0) {
            if (exp % 2L == 1) 
                p = (p * mul) % modulo; 
            mul = (mul * mul) % modulo; 
            exp >>= 1; 
        }
        return p; 
    }

    int getIndex(int idx) {
        if (idx >= static_cast<int>(v.size()))
            return -1; 
        else {
            int ai = params[idx][0], bi = params[idx][1]; 
            int ao = (al * inverse(ai)) % modulo; 
            int bo = (modulo + bl - (((al * inverse(ai)) % modulo) * bi) % modulo) % modulo; 
            return ((ao * v[idx]) % modulo + bo) % modulo; 
        }
    }
};


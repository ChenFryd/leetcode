#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int size = s.length(), counter = 0;
        for (int i = size-1; i >= 0; i--)
        {
            if (s[i] == ' ' && counter>0) break;
            if (s[i] != ' ') counter++;
        }
        return counter;
    }
};

int main(){
    Solution sol;
    cout<<sol.lengthOfLastWord("hello world")<<endl;
}
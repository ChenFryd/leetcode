#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
    private:
        vector<vector<bool>> dp;
        bool solve(int i,int j,string &s){
            if (i==j)
                return dp[i][j] = true;
            if (j-i == 1){
                if (s[i] == s[j])
                    return this->dp[i][j] = true;
                else
                    return this->dp[i][j] = false;
            }
            if (s[i] == s[j] && dp[i+1][j-1])
                return this->dp[i][j] = true;
            else
                return this->dp[i][j] = false;
        }
    public:
        string longestPalindrome(string s) {
            
            int n = s.size();
            dp.resize(n, vector<bool>(n, false));
            int startIndex = 0, maxlen=0;
            for(int interval=0;interval<n;interval++){
                for (int i=0; i<n-interval; i++){
                    int j = i + interval;
                    solve(i,j,s);
                    if (dp[i][j]){
                        if (j-i+1 > maxlen){
                            startIndex = i;
                            maxlen = j-i+1;
                        }
                    }
                }
            }
            return s.substr(startIndex,maxlen);
        }
};

int main(){
    Solution s;
    string str = "babad";
    string ans = s.longestPalindrome(str);
    cout<<ans<<endl;
}
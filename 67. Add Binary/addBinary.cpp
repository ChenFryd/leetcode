#include <string>
#include <iostream>

class Solution {
public:
    std::string addBinary(std::string a, std::string b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        std::string res = "";

        while (i >= 0 || j >= 0 || carry) {
            carry += i >= 0 ? a[i] - '0' : 0;
            carry += j >= 0 ? b[j] - '0' : 0;
            i--; j--;
            res = char(carry % 2 + '0') + res;
            carry /= 2;
        }





        return res;
    }
};


int main() {
    Solution sol;
    std::string a = "11";
    std::string b = "1";
    std::string res = sol.addBinary(a, b);
    std::cout << res << std::endl;

    return 0;
}

class stringToInteger{
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.myAtoi(""));
        System.out.println(sol.myAtoi("123"));
        System.out.println(sol.myAtoi("  123"));
        System.out.println(sol.myAtoi("  -123"));
        System.out.println(sol.myAtoi("-91283472332"));
        System.out.println(sol.myAtoi("21474836460"));
    }
}

class Solution {
    public int myAtoi(String s){
        int i=0;
        int n=s.length();
        double num=0;
        while (i<n && s.charAt(i)==' ') i++;
        boolean positivity = true;
        if (i<n && s.charAt(i) == '-')
            positivity = false;
        if (i<n && (s.charAt(i) == '+' || s.charAt(i) == '-'))
            i++;
        while (i<n && s.charAt(i)-'0'<10 && s.charAt(i)-'0'>=0)
            num = num*10 + s.charAt(i++)-'0';
        if (positivity == false)
            num *= -1;
        if (num >Integer.MAX_VALUE)
            return Integer.MAX_VALUE;
        if (num < Integer.MIN_VALUE)
            return Integer.MIN_VALUE;
        return (int) num;
    }
}
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows >= len(s):
            return s
        i=0
        col=0
        strTable=[[] for _ in range(numRows)]
        while (i<len(s)):
            strTable[col].append(s[i])
            col = col+1 if (i//(numRows-1))%2==0 else col-1
            i+=1
        return "".join(["".join(row) for row in strTable])

            
sol = Solution()
print(sol.convert("PAYPALISHIRING",3))
print(sol.convert("PAYPALISHIRING",4))
print(sol.convert("A",1))
print(sol.convert("AB",1))
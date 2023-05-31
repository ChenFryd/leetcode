class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows >= len(s):
            return s
        i=0
        row=0
        strTable=['' for i in range(numRows)]
        for i, c in enumerate(s):
            strTable[row]+=c
            row = row+1 if (i//(numRows-1))%2==0 else row-1
        return "".join(strTable)

            
sol = Solution()
print(sol.convert("PAYPALISHIRING",3))
print(sol.convert("PAYPALISHIRING",4))
print(sol.convert("A",1))
print(sol.convert("AB",1))
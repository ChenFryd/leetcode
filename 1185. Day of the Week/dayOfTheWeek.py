class Solution:
    def hasLeapDay(self,year):
            return 1 if year % 4 == 0 and year % 100 != 0 or year %400 ==0 else 0
    
    def daysSinceStart(self,day,month,year):
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        numDays = 0
        for y in range(year-1,1970,-1):
                numDays += 365 + self.hasLeapDay(y)
        numDays += sum(daysInMonth[:month-1])
        numDays += day
        if month > 2:
              numDays += self.hasLeapDay(y)
        return numDays
        


    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
                dayNames = ["Friday","Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
                knownStart = self.daysSinceStart(1,1,1971)
                d = self.daysSinceStart(day,month,year)
                return dayNames[abs(d-knownStart) % 7]
    
sol = Solution()
print(sol.dayOfTheWeek(12,9,2023))

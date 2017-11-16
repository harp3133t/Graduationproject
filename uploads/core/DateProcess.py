from datetime import date

class CalDate:

    def __init__(self):
        self.year=2017
        self.month=10
        self.days=29





    def deltaDate(self,year1,month1,days1,year2,month2,days2):
        d0=date(year1,month1,days1)
        d1=date(year2,month2,days2)
        result=d1-d0
        return abs(result)



##s=CalDate()
##n=s.deltaDate(2017,8,23,2017,9,24)
##print n.days
##print type(n.days)

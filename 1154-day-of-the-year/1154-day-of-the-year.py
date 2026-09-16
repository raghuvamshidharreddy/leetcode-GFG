class Solution:
    def dayOfYear(self, date: str) -> int:
        from datetime import datetime
        date_object = datetime.strptime(date, "%Y-%m-%d").date()
        print(date_object)
        year=date_object.year
        start_date=datetime(year,1,1).date()
        print(start_date)
        days=(date_object-start_date).days
        return days+1
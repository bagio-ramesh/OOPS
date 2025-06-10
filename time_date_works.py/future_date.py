from datetime import datetime,timedelta

cur_date = datetime.today()

td = timedelta(days = 20)

future_date = cur_date+td

print(future_date)  
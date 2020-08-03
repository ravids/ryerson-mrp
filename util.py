from calendar import monthrange
import pandas as pd

def lastdayofmonth(year_start, year_end):
    last_day_of_month_list = []
    for year in range(year_start, year_end):
        for month in range(1, 13):
            last_day = monthrange(year, month)
            last_day_of_month_list.append(str(year) + '-' + str(month) + '-' + str(last_day[1])) 
            #print(monthrange(year, month))
            #print (lastdayofmonth(datetime.date(year, month, 1)))
    return pd.DataFrame(last_day_of_month_list, columns = ['Date']) 
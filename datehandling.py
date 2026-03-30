import datetime

def passDate():
    current_date = datetime.datetime.now()
    current_MonthYear = current_date.strftime("%B %Y") 
    return current_MonthYear


def addCurrentMonthExpense(expenses, current_MonthYear):
    existing = expenses["Expenses"].get(current_MonthYear, [])
    start_id = max([item["ID"] for item in existing], default=0)
    expense_id = start_id + 1
    return expense_id

def addNextMonthExpense(expenses, current_MonthYear, next_MonthYear):
    if next_MonthYear not in expenses["Expenses"]:
        expenses["Expenses"][next_MonthYear] = []

    if not expenses["Expenses"][next_MonthYear]:
        expense_id = 1    
    else:
        last_id = expenses["Expenses"][next_MonthYear][-1]["ID"]
        expense_id = last_id + 1
    return expense_id



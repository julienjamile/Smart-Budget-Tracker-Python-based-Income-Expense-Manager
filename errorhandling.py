
import datetime
from tkinter import messagebox
import json

#Error-Logic Handling
def calculate_remaining_balance(data, currentDate):
    remBalance = 0
    try:
        expenses = data["Expenses"].get(currentDate, [])
        for entry in expenses:
            remBalance += entry.get("Amount", 0)
        return data.get("Monthly Income", 0) - remBalance
    except Exception as e:
        messagebox.showerror("Calculation Error", f"ERROR: {e}")
        return None

def budgetFlags(expenses, current_MonthYear):    
    category_limits = {}
    try:
        for limit in expenses["Expenses"][current_MonthYear]:
            category = limit["Category"]
            amount = limit["Amount"]
            if category in category_limits:
                category_limits[category] += amount
            else:
                category_limits[category] = amount
        return category_limits
    except Exception as e: 
        messagebox.showerror("Calculation Error", f"ERROR: {e}")
        return None

def calculate_total_spent(data, currentDate):
    try:
        total = 0
        for i in range(len(data["Expenses"][currentDate])):
            total += data["Expenses"][currentDate][i]["Amount"]
        return total
    except Exception as e:
        messagebox.showerror("Calculation Error", f"ERROR: {e}")
        return None
    
#Error-File Handling

def passArchive():
    try:
        with open('archivedexpenses.json') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        messagebox.showerror("File Error", f"ERROR: archivedexpenses.json cannot be loaded: {e}")
        return {}

def archiveData(data):
    try:
        with open('archivedexpenses.json', 'w') as f:
            json.dump(data, f, indent=4)
    except TypeError as e:
        messagebox.showerror("Save Error", f"ERROR: Saving archive data failed: {e}")
        return {}

def passData(): 
    try:
        with open('expense data.json') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        messagebox.showerror("File Error", f"ERROR: expense expense data.json cannot be loaded: {e}")
        return None

def fillEmptyFile(currentDate, income):
    try:
        with open('expense data.json', 'w') as f:
            data = {
                "Monthly Income": income,
                "Expenses": {
                    currentDate: []
                }
            }
            json.dump(data, f, indent=4)
    except Exception as e:
        messagebox.showerror("File Error",f"Error creating expense data file: {e}")

def passMonthIncome():
    try:
        with open('expense data.json') as f:
            data = json.load(f)
        return data['Monthly Income']
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        messagebox.showerror("Data Error", f"Error retrieving monthly income: {e}")
        return None

def passRemBalance(currentDate):
    try:
        with open('expense data.json') as f:
            data = json.load(f)
        remBalance = calculate_remaining_balance(data, currentDate)
        return remBalance
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        messagebox.showerror("Data Error", f"Error retrieving remaining balance: {e}")
        return None
    
def passBudget(currentDate):
    try:
        total = 0
        with open('expense data.json') as f:
            data = json.load(f)
        total = calculate_total_spent(data, currentDate)
        return total 
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        messagebox.showerror("Data Error", f"Error retrieving total expenses: {e}")
        return None
    
def saveData(data):
    try: 
        with open('expense data.json', 'w') as f:
            json.dump(data, f, indent=4)
    except TypeError as e:
        messagebox.showerror("Save Error", f"ERROR: Saving expense data failed: {e}")

#Error-Date Handling 
def archivePrepDate(currentdate, dates):
    format = "%B %Y"
    current_dt = datetime.datetime.strptime(currentdate, format)
    target_dt = datetime.datetime.strptime(dates, format)
    return target_dt < current_dt

def formatError(userdate):
    diff_formats = [
        "%d %B, %Y",
        "%B %d, %Y",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%Y-%m-%d",
        "%Y-%m-%d",
        "%m-%d-%Y",
        "%B-%d-%Y",
    ]
    for fmt in diff_formats:
        try:
            transformed_date = datetime.datetime.strptime(userdate, fmt)
            return transformed_date.strftime("%m/%d/%Y")
        except ValueError:
           continue
    if not userdate:
        messagebox.showerror("Missing Date", f"Please enter date.")
        return False
    messagebox.showerror("Date Error", f"ERROR: Unable to read the date '{userdate}' in any supported format.")
    return False

def cmprdates(input_date, currentdate):
    input_dt = datetime.datetime.strptime(input_date, "%m/%d/%Y")
    current_dt = datetime.datetime.strptime(currentdate, "%B %Y")
    input_month = input_dt.replace(day=1)
    current_month = current_dt.replace(day=1)

    if input_month == current_month:
        return True
    elif input_month > current_month:
        messagebox.showinfo("Scheduled for Future Month", "Your expense was scheduled for a future month.")
        return False
    else:
        messagebox.showerror("Invalid Date", "You cannot schedule an expense for a past month.")
        return False
    
def datetoKey(date):
    # Try parsing the date using different formats
    date_formats = [
        "%d %B, %Y",
        "%B %d, %Y",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%Y-%m-%d",
        "%Y-%m-%d",
        "%m-%d-%Y",
        "%B-%d-%Y",  
    ]
    
    for fmt in date_formats:
        try:
            nextdate = datetime.datetime.strptime(date, fmt)
            return nextdate.strftime("%B %Y")
        except ValueError:
            continue
    messagebox.showerror("Date Format Error", f"Date format of '{date}' is not valid.")

#Others
def input_description(desc_entry):
    description = desc_entry.get()

    if not description:
        messagebox.showwarning("Missing Description", "Please fill out the description field.")
        return None
    return description

def input_payee(payee_entry):
    payee = payee_entry.get()

    if not payee:
        messagebox.showwarning("Missing Payee", "Please fill out the payee field.")
        return None
    return payee
        
def input_category(category_combobox):
    category = category_combobox.get()

    if not category:
        messagebox.showwarning("Missing Category", "Please select a category.")
        return None
    return category

def input_method(method_combobox):
    method = method_combobox.get()

    if not method:
        messagebox.showwarning("Missing Method", "Please select a payment method.")
        return None
    return method

def input_amount(amount_entry):
    raw = amount_entry.get().strip()
    if not raw:
        messagebox.showerror("Missing Input", "Amount field is required.")
        return None
    try:
        amount = float(raw)
        if amount < 0:
            messagebox.showerror("Invalid Amount", "Amount cannot be negative.")
            return None
        return amount
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for amount.")
        return None

    


        
    
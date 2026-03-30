import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import datahandling as file 
import datehandling as datehandle
import errorhandling as error
import logic as logic
import datetime 

root = tk.Tk()
root.title("Smart Budget Tracker")
root.geometry("900x600")
root.configure(bg='#f0f2f5')


background_color = "#f0f2f5"
primary_color = "#2d4059"
accent_color = "#5cdb95"
light_accent = "#edf5e1"
base_font = ('Segoe UI', 13)
header_font = ('Segoe UI', 18, 'bold')

current_MonthYear = datehandle.passDate() 

if file.isFileEmpty() == True:
    monthly_income = 0.0
    remaining_balance = 0.0
    total_expenses = 0.0
    expenses = {}
    category_limits = {}   
else:
    monthly_income = error.passMonthIncome()
    expenses = error.passData()

    months_to_archive = []
    for month_key in expenses["Expenses"]:
        if error.archivePrepDate(current_MonthYear, month_key):
            error.archiveData({month_key: expenses["Expenses"][month_key]})
            months_to_archive.append(month_key)
    
    for month in months_to_archive:
        if month in expenses["Expenses"]:
            del expenses["Expenses"][month]
    error.saveData(expenses)

    if current_MonthYear not in expenses["Expenses"]:
        expenses["Expenses"][current_MonthYear] = []
        error.saveData(expenses)

    remaining_balance = error.passRemBalance(current_MonthYear)
    total_expenses = error.passBudget(current_MonthYear)
    category_limits = error.budgetFlags(expenses, current_MonthYear)


style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.TFrame", background=background_color)
style.configure("Custom.TLabel", background=background_color, font=base_font)
style.configure("Custom.TButton", background=primary_color, foreground="white", font=base_font, padding=6)
style.map("Custom.TButton", background=[("active", accent_color)])
style.configure("Treeview", background=light_accent, foreground="black", rowheight=25,
                    fieldbackground=light_accent, font=('Segoe UI', 10))
style.configure("Treeview.Heading", background=primary_color, foreground="white", font=('Segoe UI', 11, 'bold'))

    
main_frame = ttk.Frame(root, padding=20, style="Custom.TFrame")
main_frame.pack(fill='both', expand=True)


income_frame = ttk.Frame(main_frame, style="Custom.TFrame")
income_frame.grid(row=0, column=0, sticky='ew', pady=10)
ttk.Label(income_frame, text="💰 Monthly Income:", style="Custom.TLabel").grid(row=0, column=0, sticky='w')
income_entry = ttk.Entry(income_frame, font=base_font)
income_entry.grid(row=0, column=1, padx=5)

income_button = ttk.Button(income_frame, text="Set Income", style="Custom.TButton")
income_button.grid(row=0, column=2, padx=5)
totalExpenses_button = ttk.Button(income_frame, text="Total Spent", style="Custom.TButton")
totalExpenses_button.grid(row=0, column=3, padx=5)

archive_button = ttk.Button(income_frame, text="Past Expenses", style="Custom.TButton")
archive_button.grid(row=0, column=4, padx=5)


balance_label = ttk.Label(main_frame, text=f"Remaining Balance: PHP {remaining_balance:.2f}", font=header_font, style="Custom.TLabel")
balance_label.grid(row=1, column=0, columnspan=3, pady=10)


def input_income():
    global monthly_income, remaining_balance, total_expenses
    try:
        income = float(income_entry.get())
        monthly_income = income
        remaining_balance = income
        balance_label.config(text=f"Remaining Balance: PHP {income:.2f}")
        income_entry.delete(0, tk.END)
        file.saveMonthIncome(income)

        income_button.config(text="Change Income", command=change_income)
    except ValueError:
        messagebox.showerror("Invalid Input:", "Please enter a valid numeric value for income.")
def change_income():
    global monthly_income, remaining_balance, total_expenses
    try:
        income = float(income_entry.get())
        monthly_income = income
        if total_expenses == 0.0:
            remaining_balance = income
        elif total_expenses <= income:
            remaining_balance = income - total_expenses
        else:
            messagebox.showerror("Balance Exceeded Monthly Income!", "Please delete an expense.")
            remaining_balance = income - total_expenses

        balance_label.config(text=f"Remaining Balance: PHP {remaining_balance:.2f}")
        income_entry.delete(0, tk.END)
        file.saveMonthIncome(income)
    except ValueError:
        messagebox.showerror("Invalid Input:", "Please enter a valid numeric value for income.")

def showTotalSpent():
    messagebox.showinfo("Total Expenses", f"Your total spent for this month is {total_expenses}")
def noMonthlyIncome():
    messagebox.showwarning("Total Expenses", f"Input Monthly Income first")

def pastExpenses():
    archiveDataDisplay = tk.Toplevel(root)
    archiveDataDisplay.title("Past Expenses")
    archiveDataDisplay.geometry("600x400")
    archiveDataDisplay.configure(bg='#f0f2f5')

    mini_frame = ttk.Frame(archiveDataDisplay, padding=20, style="Custom.TFrame")
    mini_frame.pack(fill='both', expand=True)

    mini_frame.columnconfigure(0, weight=1)
    mini_frame.rowconfigure(4, weight=1) 

    archiveData = error.passArchive()
    prevMoth = list(archiveData.keys())

    ttk.Label(mini_frame, text="Select Month:", style="Custom.TLabel").grid(row=0, column=0, sticky='w')
    prevMonth_combobox = ttk.Combobox(mini_frame, values=prevMoth, font=base_font, state="readonly")
    prevMonth_combobox.grid(row=0, column=1, padx=5, pady=5)

    columns = ("ID", "Date", "Description", "Amount", "Category", "Payee", "Method")
    tree = ttk.Treeview(mini_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=70, anchor='center')
    tree.grid(row=4, column=0, columnspan=3, pady=10, sticky='nsew')

    def on_month_selected(event):
        selectedMonth = prevMonth_combobox.get()
        tree.delete(*tree.get_children()) 
        for i, data in enumerate(archiveData[selectedMonth]):
            tree.insert('', 'end', values=(
                data["ID"],
                data["Date"],
                data["Description"],
                data["Amount"],
                data["Category"],
                data["Payee"],
                data["Method"]
            ))

    prevMonth_combobox.bind("<<ComboboxSelected>>", on_month_selected)



   



if monthly_income == 0 and remaining_balance == 0:
    income_button.config(text="Set Income", command=input_income)
    totalExpenses_button.config(state="normal", command=noMonthlyIncome)
else:
    income_button.config(text="Change Income", command=change_income)
    totalExpenses_button.config(state="normal", command=showTotalSpent)
archive_button.config(command=pastExpenses)



input_frame = ttk.Frame(main_frame, style="Custom.TFrame")
input_frame.grid(row=2, column=0, columnspan=3, sticky='ew', pady=10)

date_entry = ttk.Entry(input_frame, font=base_font)
desc_entry = ttk.Entry(input_frame, font=base_font)
amount_entry = ttk.Entry(input_frame, font=base_font)
category_combobox = ttk.Combobox(input_frame, values=["Food", "Transport", "Bills", "Entertainment", "Savings", "Others"], font=base_font)
payee_entry = ttk.Entry(input_frame, font=base_font)
method_combobox = ttk.Combobox(input_frame, values=["Cash", "Credit", "Online", "Others"], font=base_font)

ttk.Label(input_frame, text="📅 Date:", style="Custom.TLabel").grid(row=0, column=0, sticky='w')
date_entry.grid(row=0, column=1, padx=5, pady=3)
ttk.Label(input_frame, text="📝 Description:", style="Custom.TLabel").grid(row=1, column=0, sticky='w')
desc_entry.grid(row=1, column=1, padx=5, pady=3)
ttk.Label(input_frame, text="💸 Amount:", style="Custom.TLabel").grid(row=2, column=0, sticky='w')
amount_entry.grid(row=2, column=1, padx=5, pady=3)
ttk.Label(input_frame, text="📂 Category:", style="Custom.TLabel").grid(row=0, column=2, sticky='w')
category_combobox.grid(row=0, column=3, padx=5, pady=3)
ttk.Label(input_frame, text="👤 Payee:", style="Custom.TLabel").grid(row=1, column=2, sticky='w')
payee_entry.grid(row=1, column=3, padx=5, pady=3)
ttk.Label(input_frame, text="💳 Method:", style="Custom.TLabel").grid(row=2, column=2, sticky='w')
method_combobox.grid(row=2, column=3, padx=5, pady=3)

    
columns = ("ID", "Date", "Description", "Amount", "Category", "Payee", "Method")
tree = ttk.Treeview(main_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130, anchor='center')
tree.grid(row=4, column=0, columnspan=3, pady=10, sticky='nsew')
i = 0

if file.isFileEmpty():
    error.fillEmptyFile(current_MonthYear, monthly_income)
    expenses = error.passData() 
else:
    months_to_archive = []

    for month_key in expenses["Expenses"]:
        if month_key == current_MonthYear:
            for i, data in enumerate(expenses["Expenses"][month_key]):
                tree.insert('', 'end', values=(
                    i + 1,
                    data["Date"],
                    data["Description"],
                    data["Amount"],
                    data["Category"],
                    data["Payee"],
                    data["Method"]
                ))
        elif error.archivePrepDate(current_MonthYear, month_key):
            error.archiveData({month_key:expenses["Expenses"][month_key]})
            months_to_archive.append(month_key)
            

    for month in months_to_archive:
        if month in expenses["Expenses"]:
            del expenses["Expenses"][month]
            error.saveData(expenses)

def input_expense():
    global expenses
    global remaining_balance

    amount = error.input_amount(amount_entry)
    if amount is None:
        return

    if amount > remaining_balance:
        messagebox.showerror("Not Enough Balance", "Not enough remaining balance to add this expense!")
        return
    
    date = error.formatError(date_entry.get())
    if date is False:
        return

    category = error.input_category(category_combobox)
    if category is None:
        return

    method = error.input_method(method_combobox)
    if method is None:
        return

    description = error.input_description(desc_entry)
    if description is None:
        return

    payee = error.input_payee(payee_entry)
    if payee is None:
        return

    category_limits.setdefault(category, 0)
    category_limits[category] += amount

    if category_limits[category] > monthly_income * 0.5:
        messagebox.showwarning("Overspending", f"Overspending in category '{category}'.")

    dateInputted = error.cmprdates(date, current_MonthYear)

    if dateInputted is None or (dateInputted is False and datetime.datetime.strptime(date, "%m/%d/%Y") < datetime.datetime.strptime(current_MonthYear, "%B %Y")):
        return  

    expense_data = {
        "Date": date,
        "Description": description,
        "Amount": amount,
        "Category": category,
        "Payee": payee,
        "Method": method
    }

    if dateInputted == True:
        expense_id = logic.addCurrentMonthExpense(expenses, current_MonthYear)
        remaining_balance -= amount
        balance_label.config(text=f"Remaining Balance: PHP {remaining_balance:.2f}")

        expense_data["ID"] = expense_id
        
        tree.insert('', 'end', values=(
            expense_id,
            date,
            description,
            f"{amount:.2f}",
            category,
            payee,
            method
        ))

        expenses["Expenses"][current_MonthYear].append(expense_data)
        error.saveData(expenses)

    else:
        next_MonthYear = error.datetoKey(date)
        expense_data["ID"] = logic.addNextMonthExpense(expenses, current_MonthYear, next_MonthYear)
        expenses["Expenses"][next_MonthYear].append(expense_data)
        error.saveData(expenses)

    date_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_combobox.delete(0, tk.END)
    payee_entry.delete(0, tk.END)
    method_combobox.delete(0, tk.END)
        

def delete_selected():
        global expenses
        global remaining_balance
        
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a row to delete.")
            return
        
        if current_MonthYear not in expenses["Expenses"]:
            messagebox.showerror("Error", f"No expenses found for {current_MonthYear}.")
            return

        for item in selected:
            values = tree.item(item, 'values')
            amount = float(values[3])
            category = values[4]
            item_id = int(values[0])

            for i, exp in enumerate(expenses["Expenses"][current_MonthYear]):
                if exp["ID"] == item_id:
                    expenses["Expenses"][current_MonthYear].pop(i)
                    break

            remaining_balance += amount
            balance_label.config(text=f"Remaining Balance: PHP {remaining_balance:.2f}")

            if category in category_limits:
                category_limits[category] -= amount
                if category_limits[category] <= 0:
                    del category_limits[category]
            tree.delete(item)

        tree.delete(*tree.get_children())  
        for i, data in enumerate(expenses["Expenses"][current_MonthYear], start=1):
            data["ID"] = i  
            tree.insert('', 'end', values=(
                i,
                data["Date"],
                data["Description"],
                f"{data['Amount']:.2f}",
                data["Category"],
                data["Payee"],
                data["Method"]
            ))

        error.saveData(expenses)

ttk.Button(main_frame, text="➕ Add Expense", style="Custom.TButton", command=input_expense).grid(row=3, column=0, columnspan=3, pady=10)
ttk.Button(main_frame, text="🗑️ Delete Selected", style="Custom.TButton", command=delete_selected).grid(row=5, column=0, columnspan=3, pady=10)
  
main_frame.grid_rowconfigure(4, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

root.mainloop()


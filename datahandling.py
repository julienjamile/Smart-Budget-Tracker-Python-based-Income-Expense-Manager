import json 
import logic as logic
import errorhandling as error

def isFileEmpty():
    with open('expense data.json') as f:
        content = f.read().strip()
    if not content:
        return True
    else:
        return False

def saveMonthIncome(income):
    with open('expense data.json') as f:
        data = json.load(f)
    data["Monthly Income"] = income  
    with open('expense data.json', 'w') as f:
        json.dump(data, f, indent=4) 




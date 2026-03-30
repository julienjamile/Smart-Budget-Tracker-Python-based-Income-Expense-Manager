# Smart-Budget-Tracker-Python-based-Income-Expense-Manager
A Python-based income and expense manager built with Tkinter. Features real-time tracking, budget categorization, and local JavaScript Object Notation (JSON) storage. Developed as a Bachelor of Science in Computer Science student as a final project for the Course, Intermediate Programming at Pamantasan ng Lungsod ng Maynila (PLM)

# Smart Budget Tracker: Python-Based Income & Expense Manager

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## Project Description
[cite_start]Effective financial control is important in today's rapidly changing environment, yet many people find it challenging to keep track of their money using manual techniques like calculators or spreadsheets, which are frequently prone to mistakes, inefficiencies, and inconsistencies[cite: 51, 89, 90]. 

[cite_start]The Smart Budget Tracker is an automated, user-friendly tool built in Python to address these issues[cite: 53, 92]. [cite_start]It provides users with clear visual financial insights, category budget management, and real-time spending tracking[cite: 54]. [cite_start]This system is designed to empower individuals—from salaried workers to freelancers and students—to take control of their finances, cut back on wasteful spending, and work toward financial stability[cite: 56, 97].

## Features
* [cite_start]**Income-Based Budget Tracking:** Uses the user's monthly income and reported expenses to create an effective budget[cite: 115, 163].
* [cite_start]**Expense Categories & Flagging:** Classifies expenses into distinct groups and flags overspending when a specific category exceeds the set budget[cite: 116, 180].
* [cite_start]**Detailed Transaction Logging:** Records Payee details, exact Dates of Payment, Payment Methods (Cash, Credit, Online), and Expense Descriptions for full clarity[cite: 117, 118, 119, 121].
* [cite_start]**Real-Time Balances & Summaries:** Displays the real-time remaining balance after each input and generates categorized expense summaries[cite: 181, 183].
* [cite_start]**Data Archiving:** Allows users to view financial records and data from previous months[cite: 253, 254].

## System Architecture / How It Works
[cite_start]The system follows a standard Input-Process-Output (IPO) framework[cite: 166]:
* [cite_start]**Input:** Users input their monthly income, daily logged expenses (with exact amounts), select predefined categories, add descriptions, and designate payment dates[cite: 170, 171, 172, 173, 174].
* [cite_start]**Process:** The system analyzes the income, categorizes the inputs, calculates the remaining balance per log, processes the payment date to update the monthly balance, and triggers alerts for overspending[cite: 175, 176, 177, 178, 180].
* [cite_start]**Output:** The interface displays the real-time remaining balance, a summary of expenses grouped by category, and a table reflecting spending patterns[cite: 181, 183, 184].

## Tech Stack
* [cite_start]**Language:** Python [cite: 278]
* [cite_start]**GUI Framework:** Tkinter Widgets [cite: 280]
* [cite_start]**Data Storage:** Local JSON file handling [cite: 281]
* [cite_start]**Utilities:** Datetime module for scheduling and logging [cite: 282]

## File Structure
* `main.py` — Main application entry point; handles the Tkinter GUI, button commands, expense input/deletion logic, and balance display.
* `datahandling.py` — Handles file read/write operations for the JSON data file, checking file states, and saving income data.
* `datehandling.py` — Retrieves and formats the current month and year used as the active session key.
* `errorhandling.py` — Contains all validation logic, error-handling functions, date formatting/comparison, balance calculations, and field input checks.
* `logic.py` — Contains pure logic functions for assigning expense IDs for current-month and scheduled future entries.
* `IP_Project_Group5_REVISED_.pdf` — Complete academic project documentation and research paper.

## How to Run / Installation
1. Ensure you have Python 3.x installed on your machine.
2. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)

# 💰 Smart Budget Tracker
### Python-Based Income & Expense Manager

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey?style=for-the-badge)
![JSON](https://img.shields.io/badge/Storage-JSON-orange?style=for-the-badge&logo=json&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-2ea44f?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> A desktop application that helps individuals track their monthly income and expenses in real time — built with Python and Tkinter as a final academic project at Pamantasan ng Lungsod ng Maynila.

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [System Architecture](#-system-architecture--how-it-works)
- [Tech Stack](#-tech-stack)
- [File Structure](#-file-structure)
- [Getting Started](#-getting-started)
- [Screenshots](#-screenshots)
- [Limitations](#-limitations)
- [Team Members & Roles](#-team-members--roles)
- [Acknowledgements](#-acknowledgements)

---

## 📖 About the Project

Effective financial control is important in today's rapidly changing environment, yet many people find it challenging to keep track of their money using manual techniques like calculators or spreadsheets — methods that are frequently prone to mistakes, inefficiencies, and inconsistencies.

The **Smart Budget Tracker** is an automated, user-friendly desktop tool built in Python to address these issues. It provides users with real-time spending tracking, category-based budget management, and clear financial summaries. Designed to empower everyone — from salaried workers to freelancers and students — to take control of their finances, reduce wasteful spending, and work toward financial stability.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💵 **Income-Based Budget Tracking** | Uses the user's monthly income and reported expenses to build and manage an effective budget |
| 📂 **Expense Categories & Overspending Flags** | Classifies expenses into distinct groups (Food, Transport, Bills, etc.) and alerts the user when a category exceeds budget |
| 🧾 **Detailed Transaction Logging** | Records payee details, exact payment dates, payment methods (Cash, Credit, Online), and expense descriptions |
| 📊 **Real-Time Balances & Summaries** | Displays remaining balance after each entry and generates a categorized expense summary |
| 🗂️ **Monthly Data Archiving** | Allows users to browse and review financial records from previous months |
| 📅 **Future Expense Scheduling** | Expenses entered with a future date are automatically assigned to the correct upcoming month |

---

## 🔧 System Architecture / How It Works

The system follows an **Input → Process → Output (IPO)** framework:

```
┌─────────────────────────────────────────────────────────────────┐
│  INPUT               PROCESS                OUTPUT              │
│  ─────               ───────                ──────              │
│  Monthly Income  →   Analyze income     →   Real-time balance   │
│  Expense amount  →   Categorize inputs  →   Categorized summary │
│  Category        →   Calculate balance  →   Spending table      │
│  Description     →   Process dates      →   Overspending alert  │
│  Payment date    →   Flag overspending  →                       │
└─────────────────────────────────────────────────────────────────┘
```

**Input:** Users enter their monthly income, log daily expenses with exact amounts, select from predefined expense categories, add descriptions, specify a payee, choose a payment method, and designate payment dates.

**Process:** The system analyzes the income, categorizes each input, calculates the real-time remaining balance per log entry, processes payment dates to assign expenses to the correct month, and triggers alerts when any category exceeds 50% of monthly income.

**Output:** The interface displays the up-to-date remaining balance, a categorized summary of all logged expenses, and a data table reflecting spending patterns — all updated live as transactions are added or removed.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| **Tkinter** | Desktop GUI framework (widgets, layout, events) |
| **JSON** | Local persistent data storage |
| **Datetime** | Date scheduling, formatting, and month-based filtering |
| **Visual Studio Code** | Development environment |

**Hardware used during development:**
- Processor: Intel Core i5-4210M @ 2.60GHz
- RAM: 12.0 GB minimum / 16.0 GB recommended
- System: 64-bit Windows OS

---

## 📁 File Structure

```
smart-budget-tracker/
│
├── main.py                          # Main entry point — Tkinter GUI, button commands,
│                                    # expense input/deletion logic, balance display
│
├── datahandling.py                  # File read/write operations for the JSON data file;
│                                    # checks file state and saves monthly income
│
├── datehandling.py                  # Retrieves and formats the current month and year
│                                    # used as the active session key
│
├── errorhandling.py                 # All validation logic, error handling, date
│                                    # formatting/comparison, balance calculations,
│                                    # archive management, and field input checks
│
├── logic.py                         # Pure logic functions for assigning expense IDs
│                                    # for current-month and scheduled future entries
│
├── expense data.json                # Auto-generated at runtime — stores active
│                                    # monthly income and expense records
│
├── archivedexpenses.json            # Auto-generated at runtime — stores past
│                                    # monthly expense records
│
└── IP_Project_Group5_REVISED_.pdf   # Full academic project documentation
```

> **Note:** The two `.json` files (`expense data.json` and `archivedexpenses.json`) are generated automatically when the application is first run. Do not manually edit them.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine
- `tkinter` is included in the Python standard library — no additional installs required
- Git installed (for cloning)

### Installation & Running

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/smart-budget-tracker.git
```

**2. Navigate into the project folder**
```bash
cd smart-budget-tracker
```

**3. Run the application**
```bash
python main.py
```

That's it — no additional dependencies or package installations needed. The JSON data files will be created automatically on first run.

---

## 📸 Screenshots

> *Add screenshots of the application to your repository and update the paths below.*

**Main Dashboard — Expense Tracker View**

<img width="828" height="448" alt="image" src="https://github.com/user-attachments/assets/38378a00-ff2b-43dd-82a4-5a2717a98ac6" />

**Past Expenses — Monthly Archive View**

<img width="830" height="431" alt="image" src="https://github.com/user-attachments/assets/2ed502ff-a076-4737-ad40-75bacdf04ee2" />

---

## ⚠️ Limitations

The following limitations were identified and documented during development:

- **No user accounts** — There is no login/logout system due to the team's limited experience with database integration at the time of development.
- **No full budgeting support** — The system tracks expenses against income but does not support advanced budgeting features (e.g., budget goals per category set by the user).
- **Limited security** — The application does not implement advanced data security or encryption protocols.
- **No external software integration** — The system cannot sync with or import data from other financial apps or platforms.
- **Manual data entry required** — All expense entries must be input manually; there is no automated data collection.

---

## 👥 Team Members & Roles

This project was developed collaboratively by six students, each assigned a specific technical domain. Listed alphabetically by last name:

| Member | Role | Responsibilities |
|---|---|---|
| **Avila, Julien Jamile P.** | File Handling & JSON (Project Lead) | Served as the overall project lead, coordinating the team's progress and merging all individual modules into a single, cohesive and functioning system. Handled reading and writing of processed expense data to and from JSON files. Simulated save/load functionality independently without requiring the GUI, and provided data support for the logic and error handling modules. |
| **Dela Cruz, Lorejane M.** | Logic & Processing | Developed the core processing logic including expense categorization and balance calculation. Worked initially in a console environment using dummy inputs, with GUI integration completed in a later stage. |
| **Guevarra, Gabrielle Ruth V.** | Exception Handling & Reporting UI | Responsible for wrapping all logic, file handling, and UI interactions with proper exception handling and error reporting. Prepared reusable templates and wrappers, adding coverage progressively as other modules were finalized. |
| **Jandoc, Russel Paolo C.** | Event Handling & Button Commands | In charge of binding all GUI button events to their corresponding backend functions. This role was dependent on the layout module being completed first, as it required existing GUI elements to hook event handlers onto. |
| **Martin, Scheanz Y.** | Date Calculations | Handled all date tagging, date comparison, and month-based filtering logic for expense scheduling and archiving. Used mock data formats initially, pending finalization of the data structure from the Logic and File Handling modules. |
| **Sebastian, Jan Zyanne B.** | Layout & Tkinter Widgets *(Lead)* | Led the design and implementation of the entire GUI structure, including all labels, entry fields, buttons, comboboxes, and Treeview table widgets using Tkinter. This module could begin independently and served as the structural foundation all other roles depended on. |

---

## 🙏 Acknowledgements

Developed as a final course requirement for the **Bachelor of Science in Computer Science** program at:

**Pamantasan ng Lungsod ng Maynila (PLM)**
College of Information Systems and Technology Management
Department of Computer Science

Supervised and evaluated by **Prof. Marilou B. Mangrobang**.

Special thanks to our panelists for their guidance and critical feedback.

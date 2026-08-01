````md
# Personal Expense Tracker

A command-line **Personal Expense Tracker** built with **Python** that helps users manage their daily expenses using **JSON** for data storage.

---

## Features

- Add new expenses
- View all expenses
- View expenses by date
- View expenses by category
- Calculate total expenses
- View expense summary
- Delete expenses
- Save and load data using JSON

---

## Technologies Used

- Python
- JSON
- File Handling

---

## Project Structure

```text
python-expense-tracker/
│── main.py
│── expenses.json
│── README.md
│── .gitignore
└── LICENSE
````

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vedwaghmare45-dev/python-expense-tracker.git
```

### 2. Navigate to the project folder

```bash
cd python-expense-tracker
```

### 3. Run the application

```bash
python main.py
```

---

## What I Learned

Building this project helped me understand and practice:

* Breaking a large problem into smaller, reusable functions.
* Working with lists of dictionaries to store structured data.
* Reading from and writing to JSON files using the `json` module.
* Python file handling for persistent data storage.
* Exception handling to validate user input.
* Searching and filtering data by date and category.
* Calculating totals and generating category-wise summaries.
* Deleting records from a list using `enumerate()`.
* Organizing a menu-driven terminal application.
* Debugging and improving program logic.

---

## Sample Output

```text
Personal Expense Tracker

1. Add New Expense
2. View All Expenses
3. View Expenses by Date
4. View Expenses by Category
5. Calculate Total Expenses
6. View Expense Summary
7. Delete an Expense
8. Save Expenses
9. Exit

Enter your choice: 1

Enter the date (DD-MM-YYYY): 01-08-2026
Enter the amount: 250
Choose your category:
Food
Enter the description: Lunch

Expense added successfully!

----------------------------------------

Enter your choice: 2

Date         Amount   Category      Description
01-08-2026   250.0    Food          Lunch

----------------------------------------

Enter your choice: 5

Total Expenses: 250.0

----------------------------------------

Enter your choice: 8

Expenses saved successfully.

----------------------------------------

Enter your choice: 9

Thank you for using Personal Expense Tracker!
```

---

## Future Improvements

* Add a graphical user interface (GUI) using Tkinter.
* Store data in an SQLite database instead of JSON.
* Generate expense charts using Matplotlib.
* Export expense records to CSV.
* Add monthly and yearly expense reports.

---

## Author

**Ved Waghmare**

```
```



---

## Author

Ved Waghmare

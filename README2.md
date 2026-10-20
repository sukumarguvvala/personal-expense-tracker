# Personal Expense Tracker

An application to record and categorize daily expenses, store transactions using SQL, and view totals and summaries through a simple HTML and CSS interface.

## Features

- Add daily expenses with a category
- Store all transactions in a SQL database
- Calculate total expenses using SQL queries
- View expense records and summaries in a clean HTML/CSS interface

## Tech Stack

| Layer    | Technology |
|----------|------------|
| Backend  | Python |
| Database | SQL (SQLite) |
| Frontend | HTML, CSS |

## Project Structure

```
personal-expense-tracker/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- No separate database server needed (SQLite is built into Python)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/personal-expense-tracker.git
   cd personal-expense-tracker
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app (the database file and `expenses` table are created automatically)
   ```bash
   python app.py
   ```

4. Open `http://127.0.0.1:5000` in your browser.

### Database table
```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    expense_date TEXT NOT NULL
);
```

## Example SQL Queries Used

```sql
-- Total of all expenses
SELECT SUM(amount) FROM expenses;

-- Total spent per category
SELECT category, SUM(amount) AS total
FROM expenses
GROUP BY category;
```

## Screenshots

Add screenshots in a `screenshots/` folder and link them here.

![Dashboard](screenshots/dashboard.png)
![Add expense](screenshots/add-expense.png)

## What I Learned

- Designing a simple database schema for transactions
- Writing SQL queries for totals and category summaries
- Connecting Python to a SQL database
- Building a clean interface with HTML and CSS

## Future Improvements

- Monthly and weekly reports
- Charts for spending by category
- Edit and delete expenses
- Export to CSV

## Author

**Divya Sukumar Guvvala**
[LinkedIn](#) | [GitHub](#) | sukumarguvvala1@gmail.com

import sqlite3
from datetime import date

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

DATABASE = "expenses.db"
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the expenses table if it does not exist."""
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            expense_date TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_connection()

    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY expense_date DESC, id DESC"
    ).fetchall()

    total = conn.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses").fetchone()[0]

    summary = conn.execute(
        """
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        """
    ).fetchall()

    conn.close()
    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        summary=summary,
        categories=CATEGORIES,
        today=date.today().isoformat(),
    )


@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "Other")
    expense_date = request.form.get("expense_date") or date.today().isoformat()

    try:
        amount = float(request.form.get("amount", ""))
    except ValueError:
        flash("Please enter a valid amount.", "error")
        return redirect(url_for("index"))

    if not title or amount <= 0:
        flash("Title is required and amount must be greater than 0.", "error")
        return redirect(url_for("index"))

    conn = get_connection()
    conn.execute(
        "INSERT INTO expenses (title, category, amount, expense_date) VALUES (?, ?, ?, ?)",
        (title, category, amount, expense_date),
    )
    conn.commit()
    conn.close()
    flash("Expense added.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
    df.to_csv(FILE_NAME, index=False)


def add_expense():
    date = input("Enter date (YYYY-MM-DD) OR press Enter for today: ")
    if date == "":
        date = datetime.today().strftime("%Y-%m-%d")

    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/Education/Other): ")
    description = input("Enter description: ")

    df = pd.read_csv(FILE_NAME)

    new_expense = {
        "Date": date,
        "Amount": amount,
        "Category": category,
        "Description": description
    }

    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    print("\n✅ Expense Added Successfully!\n")


def view_expenses():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\n⚠️ No expenses found!\n")
    else:
        print("\n📌 All Expenses:\n")
        print(df.to_string(index=False))
        print()


def total_expense():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\n⚠️ No expenses found!\n")
    else:
        total = df["Amount"].sum()
        print(f"\n💰 Total Expense: ₹{total:.2f}\n")


def category_summary():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\n⚠️ No expenses found!\n")
    else:
        summary = df.groupby("Category")["Amount"].sum()
        print("\n📌 Category Wise Summary:\n")
        print(summary)
        print()


def show_charts():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\n⚠️ No expenses found to show charts!\n")
        return

    category_sum = df.groupby("Category")["Amount"].sum()

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(category_sum, labels=category_sum.index, autopct="%1.1f%%")
    plt.title("Expense Distribution (Category Wise)")
    plt.show()

    # Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(category_sum.index, category_sum.values)
    plt.title("Category Wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.show()

    # Line Chart (Date Wise)
    df["Date"] = pd.to_datetime(df["Date"])
    date_sum = df.groupby("Date")["Amount"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(date_sum.index, date_sum.values, marker="o")
    plt.title("Expense Trend (Date Wise)")
    plt.xlabel("Date")
    plt.ylabel("Amount (₹)")
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("========= EXPENSE TRACKER =========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Show Charts")
        print("6. Exit")
        print("===================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            show_charts()
        elif choice == "6":
            print("\n👋 Exiting... Thank you!\n")
            break
        else:
            print("\n❌ Invalid choice! Try again.\n")


main()

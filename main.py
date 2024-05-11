





# Calendar and ReminderApp





import calendar
from datetime import datetime

class ReminderApp:
    def __init__(self):
        self.reminders = {}

    def display_calendar(self, year, month):
        cal = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]
        print(f"\n{month_name} {year}")
        print(" Mo Tu We Th Fr Sa Su")

        for week in cal:
            for day in week:
                if day == 0:
                    print("   ", end=" ")
                elif day in self.reminders:
                    print(f" {day:2}*", end=" ")
                else:
                    print(f" {day:2} ", end=" ")
            print()

    def add_reminder(self, date, reminder):
        self.reminders[date] = reminder
        print(f"Reminder added for {date}")

    def remove_reminder(self, date):
        if date in self.reminders:
            del self.reminders[date]
            print(f"Reminder removed for {date}")
        else:
            print(f"No reminder found for {date}")

    def view_reminders(self):
        if self.reminders:
            print("\nReminders:")
            for date, reminder in self.reminders.items():
                print(f"{date}: {reminder}")
        else:
            print("\nNo reminders set.")

    def edit_reminder(self, date, new_reminder):
        if date in self.reminders:
            self.reminders[date] = new_reminder
            print(f"Reminder for {date} edited")
        else:
            print(f"No reminder found for {date}")

if __name__ == "__main__":
    app = ReminderApp()
    today = datetime.today()
    current_year = today.year
    current_month = today.month

    while True:
        app.display_calendar(current_year, current_month)
        print("\nOptions:")
        print("1. Add reminder")
        print("2. Remove reminder")
        print("3. View reminders")
        print("4. Edit reminder")
        print("5. Next month")
        print("6. Previous month")
        print("7. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            date = int(input("Enter date: "))
            reminder = input("Enter reminder: ")
            app.add_reminder(date, reminder)
        elif choice == "2":
            date = int(input("Enter date: "))
            app.remove_reminder(date)
        elif choice == "3":
            app.view_reminders()
        elif choice == "4":
            date = int(input("Enter date: "))
            new_reminder = input("Enter new reminder: ")
            app.edit_reminder(date, new_reminder)
        elif choice == "5":
            current_month += 1
            if current_month > 12:
                current_month = 1
                current_year += 1
        elif choice == "6":
            current_month -= 1
            if current_month < 1:
                current_month = 12
                current_year -= 1
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

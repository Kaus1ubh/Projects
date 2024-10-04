import json
import os
from datetime import datetime

data_file = "habits.json"

def load_habits():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {}

def save_habits(habits):
    with open(data_file, "w") as file:
        json.dump(habits, file, indent=4)

def add_habit(habit):
    habits = load_habits()
    if habit in habits:
        print("Habit already exists!")
    else:
        habits[habit] = {"streak": 0, "last_completed": None}
        save_habits(habits)
        print(f"Habit '{habit}' added!")

def complete_habit(habit):
    habits = load_habits()
    if habit not in habits:
        print("Habit not found!")
        return
    today = datetime.today().strftime("%Y-%m-%d")
    if habits[habit]["last_completed"] == today:
        print("Habit already completed today!")
    else:
        if habits[habit]["last_completed"]:
            last_date = datetime.strptime(habits[habit]["last_completed"], "%Y-%m-%d")
            if (datetime.today() - last_date).days == 1:
                habits[habit]["streak"] += 1
            else:
                habits[habit]["streak"] = 1
        else:
            habits[habit]["streak"] = 1
        habits[habit]["last_completed"] = today
        save_habits(habits)
        print(f"Habit '{habit}' marked as completed! Streak: {habits[habit]['streak']}")

def view_habits():
    habits = load_habits()
    if not habits:
        print("No habits found!")
    else:
        for habit, data in habits.items():
            print(f"{habit}: Streak {data['streak']}, Last completed: {data['last_completed']}")

def main():
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Complete Habit")
        print("3. View Habits")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            habit = input("Enter habit name: ")
            add_habit(habit)
        elif choice == "2":
            habit = input("Enter habit name: ")
            complete_habit(habit)
        elif choice == "3":
            view_habits()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()

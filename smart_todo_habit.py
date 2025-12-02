
tasks = []
habits = {}
streaks = {}

def add_task():
    tasks.append([input("Task: "), False])

def view_tasks():
    if not tasks: print("No tasks."); return
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t[0]} - { 'Done' if t[1] else 'Pending' }")

def complete_task():
    view_tasks()
    if not tasks: return
    n = int(input("Task number: ")) - 1
    if 0 <= n < len(tasks): tasks[n][1] = True

def add_habit():
    h = input("Habit: ")
    habits[h] = False
    streaks[h] = streaks.get(h, 0)

def view_habits():
    if not habits: print("No habits."); return
    for h in habits:
        print(f"{h} - { 'Done' if habits[h] else 'Pending' } | Streak: {streaks[h]}")

def complete_habit():
    view_habits()
    if not habits: return
    h = input("Habit name: ")
    if h in habits and not habits[h]:
        habits[h] = True
        streaks[h] += 1

def wellness():
    if not tasks and not habits:
        print("No data yet."); return
    
    total = len(tasks) + len(habits)
    done = sum(t[1] for t in tasks) + sum(habits.values())
    score = done / total

    if score == 1:
        print(" Perfect day!")
    elif score >= 0.6:
        print(" Good job!")
    else:
        print(" Keep going!")

def new_day():
    for h in habits: habits[h] = False
    print("New day started.")

def menu():
    print("""
1 Add Task
2 View Tasks
3 Complete Task
4 Add Habit
5 View Habits
6 Complete Habit
7 Wellness Insight
8 New Day
9 Exit
""")

while True:
    menu()
    c = input("Choose: ")
    if c == "1": add_task()
    elif c == "2": view_tasks()
    elif c == "3": complete_task()
    elif c == "4": add_habit()
    elif c == "5": view_habits()
    elif c == "6": complete_habit()
    elif c == "7": wellness()
    elif c == "8": new_day()
    elif c == "9": break
    else: print("Invalid")

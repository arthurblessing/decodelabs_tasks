my_tasks = []
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Quit")
    choice = input("Choose: ")
    if choice == "1":
        task = input("Enter task: ")
        my_tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if my_tasks:
            for index, task in enumerate(my_tasks, 1):
                print(f"{index}. {task}")
        else:
            print("No tasks yet.")
    elif choice == "3":
        break

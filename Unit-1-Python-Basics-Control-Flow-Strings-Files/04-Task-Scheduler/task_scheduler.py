# Program: Interactive Task Scheduler Using Boolean Logic

# Initialize an empty task queue
task_queue = []

while True:
    print("\n========== TASK SCHEDULER ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Execute Tasks")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task_name = input("Enter task name: ").strip()

        if not task_name:
            print("Task name cannot be empty!")

        else:
            priority = input("Is this a high-priority task? (yes/no): ").strip().lower()
            condition = input("Is the task ready to execute? (yes/no): ").strip().lower()

            if priority not in ("yes", "no") or condition not in ("yes", "no"):
                print("Invalid input! Please enter yes or no.")

            else:
                task = {
                    "name": task_name,
                    "priority": priority == "yes",
                    "ready": condition == "yes",
                    "completed": False
                }

                task_queue.append(task)
                print("Task added successfully!")

    elif choice == "2":
        if not task_queue:
            print("Task queue is empty!")

        else:
            print("\n========== TASK LIST ==========")

            for index, task in enumerate(task_queue, start=1):
                if task["completed"]:
                    status = "Completed"
                elif task["ready"] and task["priority"]:
                    status = "Ready - High Priority"
                elif task["ready"]:
                    status = "Ready - Normal Priority"
                else:
                    status = "Waiting"

                print(f"{index}. {task['name']} | Status: {status}")

    elif choice == "3":
        if not task_queue:
            print("No tasks available for execution!")

        else:
            executed = False

            print("\n========== EXECUTING TASKS ==========")

            for task in task_queue:
                if task["completed"]:
                    continue

                # Boolean logic and short-circuit evaluation
                if task["ready"] and not task["completed"]:
                    if task["priority"] or task["ready"]:
                        print(f"Executing task: {task['name']}")
                        task["completed"] = True
                        executed = True

                    elif not task["ready"]:
                        print(f"Task is not ready: {task['name']}")

                elif not task["ready"] and not task["completed"]:
                    print(f"Task waiting for conditions: {task['name']}")

            if not executed:
                print("No pending tasks met the execution conditions.")

    elif choice == "4":
        if not task_queue:
            print("Task queue is empty!")

        else:
            try:
                task_number = int(input("Enter task number to remove: "))

                if 1 <= task_number <= len(task_queue):
                    removed_task = task_queue.pop(task_number - 1)
                    print(f"Task '{removed_task['name']}' removed successfully!")

                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "5":
        print("Exiting Task Scheduler. Goodbye!")
        break

    else:
        print("Invalid choice! Please select from 1 to 5.")


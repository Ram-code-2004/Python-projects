def task():
    tasks = []
    print("Welcome to the Task Management System")

    total_tasks = int(input("How many tasks do you want to add? "))
    for i in range(total_tasks):
        task_name = input(f"Enter the name of task {i + 1}: ")
        tasks.append(task_name)

    print(f"today's tasks are\n{ tasks}")

    while True:
        operations =int(input("Enter 1 to add a task, 2 to update a task, 3 to delete, or 4 to view: ,or 5 to exit: "))
        if operations == 1:
            new_task = input("Enter the name of the task to add: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added successfully.")
        elif operations == 2:
            update_value = input("Enter the name of the task to update: ")
            if update_value in tasks:
                new_value = input("Enter the new name for the task: ")
                index = tasks.index(update_value)
                tasks[index] = new_value
                print(f"Task '{update_value}' updated to '{new_value}'.")    
        elif operations == 3:
            delete_value = input("Enter the name of the task to delete: ")
            if delete_value in tasks:
               ind = tasks.index(delete_value)
               del tasks[ind]
               print(f"Task '{delete_value}' deleted successfully.")
            else:
                print(f"Task '{delete_value}' not found.")
        elif operations == 4:
            print("Current tasks:")
            for task in tasks:
                print(task)
        elif operations == 5:
            print("Exiting the Task Management System. Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")
task()
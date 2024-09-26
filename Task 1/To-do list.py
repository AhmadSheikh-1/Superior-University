todo_list = []

def add_task():
    task = input("Enter a task to add:")
    todo_list.append(task)
    print(f"has been added.",(task))

def remove_task():
    task = input("Enter the task to remove: ")
    
    if task in todo_list:
        todo_list.remove(task)
        print(f"has been removed.", (task))
    else:
        print(f"not found in the list.", (task))

def view_tasks():
    if not todo_list:
        print("Your To-Do List is empty.")
   
    else:
       print("Your To-do List:")
for task in todo_list:
    print("- " + task)

def main():
    while True:
        print("\n1. Add Task\n 2. Remove Task\n 3. View Tasks\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")
            
main()

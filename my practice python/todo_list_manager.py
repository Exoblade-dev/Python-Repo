# Load existing items
# 1. create new items
# 2. list items 
# 3. mark item as complete  
# 4. save items   


import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except:
        return {"tasks":[]}

def save_tasks():
    pass

def view_tasks():
    pass

def create_tasks():
    pass

def mark_task_completed():
    pass

def main():
    tasks = load_tasks()
    print(load_tasks())
    
    while True:
        print("ToDo List Manager")
        print("1.View Tasks")
        print("2.Add Task")
        print("3.Complete Task")
        print("4.Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            create_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice, Please try again")

main()

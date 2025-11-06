import os
import time as t
from datetime import datetime

def main():
    lists_path = "ToDoLists"
    os.makedirs(lists_path, exist_ok=True)
    Current_List = []
    list_loaded = False

    dir_files = os.listdir(lists_path)
    if not dir_files:
        choice = input("No to-do lists found.\nType 1 to CREATE a new one or 2 to QUIT: ").strip()
        while choice != "1":
            print(f"Please type 1 to CREATE (you typed '{choice}')")
            t.sleep(1.5)
            choice = input("Please enter your choice again: ").strip()
        create_or_add_to_existing_list(Current_List, None, lists_path)

    while True:
        dir_files = os.listdir(lists_path)
        print("\nYou have saved lists.")
        print("1) CREATE a new list")
        print("2) LOAD an existing list")
        print("3) LIST all lists")
        print("4) QUIT")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            create_or_add_to_existing_list(Current_List, None, lists_path)
        elif choice == "2":
            load_list(Current_List, lists_path)
        elif choice == "3":
            print("\n** Existing lists:**")
            for name in dir_files:
                print(name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        t.sleep(1.5)

def load_list(Current_List, lists_path):
    dir_files = os.listdir(lists_path)
    file_name = input("Please enter the full file name (with .txt): ").strip()
    while file_name not in dir_files:
        print(f"This is not a file in the directory.\nChoose from: {dir_files}")
        file_name = input("Please enter the full file name (with .txt): ").strip()
    file_path = os.path.join(lists_path, file_name)
    with open(file_path, 'r') as f:
        items = f.read().splitlines()
    # parse each line into task list [task, date, done_bool] or fallback
    new_list = []
    for line in items:
        parts = line.split("||")
        if len(parts) == 3:
            # stored as task||date||done_flag
            task, due_date, done_str = parts
            done = (done_str == "True")
            new_list.append([task, due_date, done])
        else:
            new_list.append([line, "", False])
    Current_List.clear()
    Current_List.extend(new_list)
    print(f"\nLoaded {file_name}. Current tasks:")
    display_list(Current_List)
    create_or_add_to_existing_list(Current_List, file_name, lists_path)

def create_or_add_to_existing_list(Current_List, file_name, lists_path):
    if file_name is None:
        List_Name = input("Please enter a list name (without .txt): ").strip()
        file_name = List_Name + ".txt"
        print(f"Created new list '{file_name}'")
    while True:
        print("\nChoose one of the following options:")
        print("1) ADD a task")
        print("2) DELETE a task")
        print("3) SHOW tasks")
        print("4) EXIT to main menu (and save)")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_task(Current_List)
        elif choice == "2":
            delete_task(Current_List)
        elif choice == "3":
            display_list(Current_List)
        elif choice == "4":
            save_list(file_name, Current_List, lists_path)
            break
        else:
            print("ERROR: Invalid Input! Please try again.")
        t.sleep(1)

def display_list(Current_List):
    if not Current_List:
        print("The list is currently empty.")
    else:
        print("\nYour current tasks:")
        for i, item in enumerate(Current_List, start=1):
            task, due_date, done = item
            status = "Done" if done else "Not done"
            print(f"{i}. Task: {task} | Due: {due_date} | Status: {status}")

def date_validation():
    user_date = input("Provide date (DD/MM/YYYY): ").strip()
    while True:
        try:
            datetime.strptime(user_date, "%d/%m/%Y")
            return user_date
        except ValueError:
            user_date = input("Incorrect date format. Please use DD/MM/YYYY: ").strip()

def add_task(Current_List):
    task = input("Please enter the task you would like to add: ").strip()
    due_date = date_validation()
    Current_List.append([task, due_date, False])
    print(f'"{task}" has been successfully added to the list!')

def delete_task(Current_List):
    if not Current_List:
        print("The list is empty. Nothing to delete.")
        return
    display_list(Current_List)
    try:
        index = int(input("Please enter the task number you would like to delete: ").strip())
        if 1 <= index <= len(Current_List):
            removed = Current_List.pop(index-1)
            print(f'Item "{removed[0]}" has been successfully removed from the list!')
        else:
            print("Item number is not in the list!")
    except ValueError:
        print("Invalid number entered!")

def save_list(file_name, Current_List, lists_path):
    file_path = os.path.join(lists_path, file_name)
    with open(file_path, 'w') as f:
        for task, due_date, done in Current_List:
            f.write(f"{task}||{due_date}||{done}\n")
    print("Saving the list", end="")
    for _ in range(3):
        t.sleep(1)
        print(".", end="", flush=True)
    print("\nList has been saved!\n")

if __name__ == '__main__':
    main()

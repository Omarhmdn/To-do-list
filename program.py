import os
import time as t
def main():
    lists_path = "ToDoLists"
    os.makedirs(lists_path, exist_ok=True)
    Current_List = []
    dir = os.listdir(lists_path)
    list_loaded = False

    if not dir:
        choice = input("No to-do lists found.\nType CREATE to make one or QUIT to exit: ").upper().strip()
        while choice != "CREATE":
            print(f"Please type CREATE (you typed '{choice}')")
            t.sleep(1.5)
            choice = input("Please enter your choice again: ").upper()
        create_or_add_to_existing_list(list_loaded, Current_List, None, lists_path)

    while True:
        choice = input("You have saved lists.\nType CREATE to make one, LOAD to open, LIST to view all or QUIT to exit: ").upper().strip()
        if choice == "CREATE":
            create_or_add_to_existing_list(list_loaded, Current_List, None, lists_path)
        elif choice == "LOAD":
            load_list(Current_List, list_loaded, dir, lists_path)
        elif choice == "LIST":
            print("\n**Existing lists:**")
            for name in dir:
                print(name)
        elif choice == "QUIT":
            exit("Goodbye!")
        else:
            print("Invalid choice! Please try again.")
        t.sleep(1.5)
        dir = os.listdir(lists_path)

def load_list(Current_List, list_loaded, dir, lists_path):
    list_loaded = True
    file_name = input("Please enter the full file name (with .txt): ").strip()

    while file_name not in dir:
        print(f'This is not a file in the directory.\nChoose from the following lists: {dir}')
        file_name = input("Please enter the full file name (with .txt): ").strip()

    with open(os.path.join(lists_path, file_name), 'r') as f:
        items = f.read().splitlines()
        Current_List = [items]

    print(f"\nLoaded {file_name}. Current tasks:")
    display_list(Current_List)
    create_or_add_to_existing_list(list_loaded, Current_List, file_name, lists_path)

def create_or_add_to_existing_list(list_loaded, Current_List, file_name, lists_path):
    running = True
    if not list_loaded:
        List_Name = input("Please enter a list name (without .txt): ").strip()
        file_name = List_Name + ".txt"
        List_Storage = {List_Name: Current_List}
    else:
        List_Storage = {"LoadedList": Current_List}

    while running:
        choice = input("\nChoose one of the following options:\nType ADD to add a task, DELETE to delete a task, SHOW to view tasks, EXIT to exit: ").upper().strip()

        while choice not in ("ADD", "DELETE", "SHOW", "EXIT"):
            print("ERROR: Invalid Input! Please try again.")
            t.sleep(1)
            choice = input("\nChoose one of the following options\nType ADD, DELETE, SHOW, EXIT: ").upper().strip()

        if choice == "ADD":
            Current_List = add_task(Current_List)
        elif choice == "DELETE":
            delete_task(Current_List)
        elif choice == "SHOW":
            display_list(Current_List)
        else:
            running = False
            save_list(file_name, Current_List, lists_path)

import datetime as dt
from calendar import monthrange

def date_validation():
    current_year = dt.datetime.today().year
    while True:
        due_date = input("Please enter the due date for the task in the format dd/mm/yyyy:").strip().split("/")
        due_date = list(map(int, due_date))
        if due_date[2] >= current_year:
            if 1 <= due_date[1] <= 12:
                days = monthrange(due_date[2], due_date[1])
                if due_date[0] <= days[1]:
                    break
                else:
                    continue
            else:
                continue
        else:
            continue
    due_date = '/'.join(list(map(str, due_date)))
    return due_date

def add_task(Current_List):
    task = input("Please enter the task you would like to add: ").strip().lower()
    due_date = date_validation()
    Current_List.append([task, due_date, False])
    print(f'"{task}" has been successfully added to the list!')
    return Current_List
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

def display_list(Current_List):
    if not Current_List:
        print("The list is currently empty.")
    else:
        print("\nYour current tasks:")
        for i, task in enumerate(Current_List, start=1):
            print(f"{i}. {task}")
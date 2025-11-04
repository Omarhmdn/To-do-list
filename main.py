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




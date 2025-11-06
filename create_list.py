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
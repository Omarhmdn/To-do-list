def display_list(Current_List):
    if not Current_List:
        print("The list is currently empty.")
    else:
        print("\nYour current tasks:")
        for i, task in enumerate(Current_List, start=1):
            print(f"{i}. {task}")
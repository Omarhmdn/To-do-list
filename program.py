def add_task(Current_List):
    task = input("Please enter the task you would like to add: ").strip().lower()
    due_date = input("Please enter the due date of the task in the form dd/mm/yyyy: ").strip()
    Current_List.append([task, due_date, False])
    print(f'"{task}" has been successfully added to the list!')
    return Current_List
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
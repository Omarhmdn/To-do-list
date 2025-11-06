def save_list(file_name, Current_List, lists_path):
    if not file_name:
        file_name = input("Please choose a filename (Make sure to add .txt at the end): ").strip()
    file_path = os.path.join(lists_path, file_name)

    with open(file_path, 'w') as f:
        for item in Current_List:
            f.write(item + "\n")

    print("Saving the list", end="")
    for _ in range(3):
        t.sleep(1)
        print(".")
    print("\nList has been saved!\n")
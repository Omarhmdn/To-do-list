def load_list(Current_List, list_loaded, dir, lists_path):
    list_loaded = True
    file_name = input("Please enter the full file name (with .txt): ").strip()

    while file_name not in dir:
        print(f'This is not a file in the directory.\nChoose from the following lists: {dir}')
        file_name = input("Please enter the full file name (with .txt): ").strip()

    with open(os.path.join(lists_path, file_name), 'r') as f:
        items = f.read().splitlines()
        Current_List = set(items)

    print(f"\nLoaded {file_name}. Current tasks:")
    display_list(Current_List)
    create_or_add_to_existing_list(list_loaded, Current_List, file_name, lists_path)

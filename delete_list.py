def delete_list():
    f = input("File name: ")
    try:
        t = open(f).read().splitlines()
        for i, x in enumerate(t): print(i+1, x)
        n = int(input("Task number to delete: ")) - 1
        t.pop(n)
        open(f, "w").write("\n".join(t))
        print("Task deleted!")
    except: print("Error")

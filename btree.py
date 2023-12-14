from BTrees._IIBTree import IIBTree
import time
def menu():
    print("--------- B Tree ---------")
    print("1: Insert")
    print("2: Search")
    print("3: Stop")
    choice = int(input("Enter function: "))
    return choice

btree = IIBTree()

run = True

while run == True:
    choice = menu()
    if choice == 1:
        key = int(input("Enter a number to insert: "))
        btree.insert(key, key)
        print(f"{key} inserted in tree")
    elif choice == 2:
        key = int(input("Enter what you want to search: "))
        start_time = time.time()
        if key in btree:
            print(f"{key} found in tree")
        else:
            print(f"{key} not found in tree")
        end_time = time.time()
        print(f"Time taken for searching {end_time-start_time}")
    elif choice == 3:
        run == False
    else:
        print("Invalid Input")
import tempfile
import time
from bplustree import BPlusTree

def print_menu():
    print("\n******** B+ Tree ********")
    print("1. Insert")
    print("2. Search")
    print("3. Exit")
    return input("Enter your choice: ")

temp_file = tempfile.NamedTemporaryFile().name

class SimpleSerializer:
    def serialize(self, obj, size):
        return obj.ljust(size, b'\0')
    
bplus_tree = BPlusTree(order=4, filename=temp_file, serializer=SimpleSerializer())

run = True

while run == True:
    option = print_menu()
    if option == '1':
        value = int(input("Enter element you want to insert: "))
        value_bytes = str(value).encode("utf-8")
        bplus_tree[value_bytes] = value_bytes
        print(f"{value} inserted in b+ tree.")
    elif option == '2':
        key = int(input("Enter what you want to search: "))
        key_bytes = str(key).encode('utf-8')
        start = time.time()
        if value_bytes in bplus_tree:
            print(f"{value} found in tree")
        else:
            print(f"{value} not found in tree")
        end = time.time()
        print(f"\tSearch took {end - start} seconds")
    elif option == '3':
        run = False
    else:
        print("Invalid Option! Try again.")

bplus_tree.close()
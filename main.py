import time
import sys
import clipboard
import json
from save import save_data
from load import load_items

SAVED_DATA = "clipboard.json"

if __name__=="__main__":
    argument = sys.argv 

    if len(argument) == 2:
        command = argument[1]
        data = load_items(SAVED_DATA)

        if command == "save":
            print()

            key = input("Enter a key: ")
            print()

            data[key] = clipboard.paste()

            save_data(SAVED_DATA, data)

            print("Saving Data...⌛")
            print()
            time.sleep(2)
            print("Data Saved ✅")
            print()



        elif command == "copy" or command == "load":
            print()
            key = input("Enter the Key of the data you want to load: ")
            print()

            if key in data:
                clipboard.copy(data[key])
                print("Copying data...⌛")
                print()
                time.sleep(1)
                print("Data Copied sucessfully!✅")
                print()
            else:
                print()
                print("Key Does not Exist❗")   
                print()     

        elif command == "list":
            print()
            if not data:
                print("Your Multicipboard is empty! 🙅🏻")
            print()
            for key, value in data.items():
                print()
                print(key.upper())
                print(value)
                print()
            

        else:
            print()
            print("Unknown Command❗")
            print()
    else:
        print()
        print("Error! Please pass exactly one command❗('save' / 'copy' or 'load' / 'list')")
        print()


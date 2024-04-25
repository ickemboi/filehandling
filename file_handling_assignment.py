# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with a mix of strings and numbers: 3.14\n")
except IOError as e:
    print("Error occurred while creating the file:", e)

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("This is line 4 (appended)\n")
        file.write("98765 (appended)\n")
        file.write("Appended line with a mix of strings and numbers: 2.718 (appended)\n")
except IOError as e:
    print("Error occurred while appending to the file:", e)
except PermissionError:
    print("Permission denied to append to the file.")
finally:
    print("File manipulation completed.")


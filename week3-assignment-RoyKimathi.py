# Program to read a file, modify its content, and write to a new file with error handling

def readingfile(filename):
    """
    Function to read a file and return its content.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content

        with open(filename, 'r') as file:
            modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: The file '{filename}' cannot be read due to permission issues.")
        return None

# Prompt the user for a filename
filename = input("Enter the name of the file to read: ")

# Call the function to read the file
content = readingfile(filename)
if content:
    print(content)
    print("File content:")

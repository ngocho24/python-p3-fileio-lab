def write_file(file_name, file_content):
    # Adding the file extension to the file_name
    file_name = str(file_name) + ".txt"
    
    # Writing content to the file
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Adding the file extension to the file_name
    file_name = str(file_name) + ".txt"
    
    # Appending content to the file
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    # Adding the file extension to the file_name
    file_name = str(file_name) + ".txt"
    
    # Reading content from the file
    with open(file_name, 'r') as file:
        content = file.read()
        return content
    
## Example usage of write_file function
        # write_file(file_name="example_file", file_content="This is the initial content.")

## Example usage of append_file function
        # append_file(file_name="example_file", append_content="\nThis is the appended content.")

## Example usage of read_file function
        # content = read_file(file_name="example_file")
        # print(content)

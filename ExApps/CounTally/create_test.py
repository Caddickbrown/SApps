import os

# Get the directory of the script
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, "test_file.txt")

# Create and write to the file when run directly
if __name__ == "__main__":
    with open(file_path, 'w') as test_file:
        test_file.write('Hello, this is a test file!')
    input(f'Test file created at: {file_path}')

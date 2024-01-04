import os

# Get the directory of the script
test_file_path = os.path.dirname(os.path.abspath(__file__))

# Create and write to the file
with open(test_file_path, 'w') as test_file:
    test_file.write('Hello, this is a test file!')

input(f'Test file created at: {test_file_path}')

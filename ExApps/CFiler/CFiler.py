import os
from datetime import datetime
#import pyperclip  # Import the pyperclip library

# Variables
save_in_parent_folder = False # Set to True to save in the parent folder
custom_file_name = "Contents"
version_number = "1.0.0"
postage_version_number = "n/a"
sapp_version_number = "n/a"

# Standard Variables
folder_path = "Library"
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")

# Get the path to the script's parent folder
script_folder = os.path.dirname(os.path.abspath(__file__))
parent_folder = os.path.dirname(script_folder)

# Function to remove the file extension
def remove_extension(file_name):
    base_name, extension = os.path.splitext(file_name)
    return base_name

# Get a list of files in the folder
file_names = os.listdir(folder_path)

# Filter only HTML files (you can customize this filter)
html_files = [file for file in file_names if file.endswith('.html')]

# Sort the HTML files in descending order
html_files = sorted(html_files, reverse=True)

# Define the path for the HTML file (add the .html extension)
if save_in_parent_folder:
    file_path = os.path.join(parent_folder, f"{custom_file_name}.html")
else:
    file_path = f"{custom_file_name}.html"

# Start generating the HTML code
html_code = f"""<!DOCTYPE html>
<html>
<head>
    <title>{custom_file_name}</title>
    <style>
        :root {{
            --background-color: #f0f0f0;
            --default-text-color: #414141;
            --colourful-color: #4bc67c;
        }}
        body {{
            font-family: system-ui, sans-serif;
            color: var(--default-text-color);
            background-color: var(--background-color);
            transition: background-color 0.3s ease, color 0.3s ease;
            margin-bottom: 5em;
            justify-content: center;
            width: 60%;
            display: flex;
        }}
        body a:link, body a:visited {{
            color: var(--default-text-color);
            text-decoration: underline;
        }}
        body a:hover {{
            color: var(--colourful-color);
            text-decoration: none;
        }}
        footer {{
            text-align: right;
            font-size: 0.8em;
            vertical-align: middle;
            position: fixed;
            bottom: 0;
            width: 95%;
        }}
    </style>
</head>
<body>
    <h1>{custom_file_name}</h1>
    <ul id="fileList">\n"""

# Add list items with links and file names without extensions
for file_name in html_files:
    base_name = remove_extension(file_name)
    html_code += f'        <li><a href="{folder_path}/{file_name}">{base_name}</a></li>\n'

# Complete the HTML code
html_code += f"""    </ul>
    <footer>
        <p>Updated: {current_datetime}</p>
        <p>Version: {version_number} - Created by <a href="https://caddickbrown.com">Caddick & Brown</a></p>
    </footer>
</body>
</html>"""

# Copy the generated HTML code to the clipboard
# pyperclip.copy(html_code)

# Check if the file already exists and remove it if it's saved in the parent folder
if os.path.exists(file_path):
    os.remove(file_path)

# Write the new HTML code to the file
with open(file_path, "w") as file:
    file.write(html_code)

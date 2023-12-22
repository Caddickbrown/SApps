import os
import markdown2
import tkinter as tk
from tkinter import filedialog

def convert_markdown_to_html(markdown_file_path):
    with open(markdown_file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    html_content = markdown2.markdown(markdown_content)
    return html_content

def create_homepage(markdown_files):
    homepage_content = "<h1>Markdown Files Homepage</h1>\n<ul>\n"

    for markdown_file in markdown_files:
        file_name = os.path.splitext(os.path.basename(markdown_file))[0]
        homepage_content += f"<li><a href='{file_name}.html'>{file_name}</a></li>\n"

    homepage_content += "</ul>\n"
    return homepage_content

def create_individual_html_page(markdown_file_path, output_folder='output'):
    html_content = convert_markdown_to_html(markdown_file_path)

    file_name = os.path.splitext(os.path.basename(markdown_file_path))[0]
    output_file_path = os.path.join(output_folder, f'{file_name}.html')

    # Create a simple HTML page with the converted content and a back button
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{file_name}</title>
    </head>
    <body>
        <a href="index.html">Back to Homepage</a>
        {html_content}
    </body>
    </html>
    """

    # Write the HTML content to a file
    os.makedirs(output_folder, exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_template)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        process_folder(folder_selected)

def process_folder(folder_path):
    # Get a list of Markdown files in the selected folder
    markdown_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.md')]

    # Create HTML homepage with links to each file
    homepage_content = create_homepage(markdown_files)
    homepage_path = os.path.join('output', 'index.html')
    with open(homepage_path, 'w', encoding='utf-8') as homepage_file:
        homepage_file.write(homepage_content)

    # Create individual HTML pages for each Markdown file
    for markdown_file in markdown_files:
        create_individual_html_page(markdown_file)

    print("HTML pages generated. Open 'output/index.html' to start exploring.")

if __name__ == "__main__":
    # Create a simple Tkinter GUI to select the folder
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Call the file picker
    browse_folder()

    # Keep the Tkinter event loop running
    root.mainloop()

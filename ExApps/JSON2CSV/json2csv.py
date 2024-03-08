import json
import csv
import tkinter as tk
from tkinter import filedialog

def convert_json_to_csv():
    # Open file dialog to select JSON file
    root = tk.Tk()
    root.withdraw()
    json_file_path = filedialog.askopenfilename(title="Select JSON file", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))

    if not json_file_path:
        print("No file selected. Exiting.")
        return

    # Extract directory and file name
    directory = '/'.join(json_file_path.split('/')[:-1])
    filename = json_file_path.split('/')[-1]

    # Open the JSON file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Prepare CSV file path
    csv_file_path = f"{directory}/{filename.split('.')[0]}.csv"

    # Open the CSV file in write mode
    with open(csv_file_path, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the header based on the keys of the first dictionary in the JSON
        writer.writerow(data[0].keys())

        # Write the data
        for row in data:
            writer.writerow(row.values())

    print(f"CSV file saved at: {csv_file_path}")

# Call the function to start the process
convert_json_to_csv()

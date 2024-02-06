import csv
import os
from datetime import datetime

import tkinter as tk
from tkinter import ttk, messagebox

class CounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Counter App")

        # Path to the CSV file
        self.csv_file_path = 'counter_data.csv'

        # Create and load data from the CSV file
        self.load_data()

        # Counter variables
        self.counters = []

        # Create GUI elements
        self.create_widgets()

    def load_data(self):
        # Check if the CSV file exists
        if os.path.exists(self.csv_file_path):
            # Read CSV file and store data in a list
            with open(self.csv_file_path, 'r') as csvfile:
                csvreader = csv.DictReader(csvfile)
                self.counters = list(csvreader)

    def save_data(self):
        # Save data to the CSV file
        with open(self.csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['Date', 'Counter Name', 'Tally', 'Notes']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for counter in self.counters:
                writer.writerow(counter)

    def create_widgets(self):
        # Counter frame
        counter_frame = ttk.Frame(self.master)
        counter_frame.pack(padx=10, pady=10)

        # Counter label
        ttk.Label(counter_frame, text="Counter Name:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        counter_name_entry = ttk.Entry(counter_frame)
        counter_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Counter value
        count_label = ttk.Label(counter_frame, text="0")
        count_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        # Buttons
        ttk.Button(counter_frame, text="-", command=lambda: self.update_count(count_label, -1)).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(counter_frame, text="Reset", command=lambda: self.update_count(count_label, 0)).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(counter_frame, text="+", command=lambda: self.update_count(count_label, 1)).grid(row=2, column=2, padx=5, pady=5)

        # Manual input field
        manual_input_entry = ttk.Entry(counter_frame)
        manual_input_entry.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

        # Add Counter button
        ttk.Button(counter_frame, text="Add Counter", command=lambda: self.add_counter(counter_name_entry.get())).grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

        # Export button
        ttk.Button(counter_frame, text="Export", command=lambda: self.export_data(counter_name_entry.get(), count_label.cget("text"), manual_input_entry.get())).grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

    def update_count(self, count_label, delta):
        current_count = int(count_label.cget("text"))
        new_count = max(current_count + delta, 0)
        count_label.config(text=str(new_count))

    def add_counter(self, counter_name):
        if not counter_name:
            messagebox.showwarning("Warning", "Counter Name cannot be empty.")
            return

        # Check if the counter already exists
        for counter in self.counters:
            if counter['Counter Name'] == counter_name:
                messagebox.showwarning("Warning", "Counter with the same name already exists.")
                return

        # Add new counter to the list
        new_counter = {
            'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Counter Name': counter_name,
            'Tally': 0,
            'Notes': ''
        }
        self.counters.append(new_counter)

        # Save data to CSV file
        self.save_data()

        messagebox.showinfo("Information", f"Counter '{counter_name}' added successfully.")

    def export_data(self, counter_name, tally, notes):
        if not counter_name:
            messagebox.showwarning("Warning", "Counter Name cannot be empty.")
            return

        # Find the counter by name
        for counter in self.counters:
            if counter['Counter Name'] == counter_name:
                # Update tally and notes
                counter['Tally'] = tally
                counter['Notes'] = notes

                # Save data to CSV file
                self.save_data()

                messagebox.showinfo("Information", "Data exported successfully.")
                return

        messagebox.showwarning("Warning", f"No counter found with the name '{counter_name}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()

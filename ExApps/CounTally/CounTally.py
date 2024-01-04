import csv
import os

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the CSV file
csv_file_path = os.path.join(script_directory, 'counter_data.csv')

# Check if the CSV file exists
if not os.path.exists(csv_file_path):
    # Create a new CSV file with headers
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Counter Name', 'Tally', 'Notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# Read CSV file and store data in a list
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = list(csvreader)

# Function to generate HTML for historical reporting
def generate_historical_html(data):
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Historical Reporting</title>
    </head>
    <body>
        <h1>Historical Reporting</h1>
        <table border="1">
            <tr>
                <th>Date</th>
                <th>Counter Name</th>
                <th>Tally</th>
                <th>Notes</th>
            </tr>
    '''

    for entry in data:
        html_content += f'''
            <tr>
                <td>{entry['Date']}</td>
                <td>{entry['Counter Name']}</td>
                <td>{entry['Tally']}</td>
                <td>{entry['Notes']}</td>
            </tr>
        '''

    html_content += '''
        </table>
    </body>
    </html>
    '''
    
    return html_content

# Function to generate HTML for the new count page
def generate_new_count_html(latest_tally):
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>New Count Page</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }}
            button {{
                font-size: 24px;
                padding: 10px 20px;
                margin: 0 10px;
            }}
            #count {{
                font-size: 36px;
                margin-top: 10px;
            }}
            #manualInput {{
                font-size: 16px;
                margin-top: 10px;
                width: 60px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <button onclick="increment()">+</button>
        <span id="count">{latest_tally}</span>
        <button onclick="decrement()">-</button>

        <input type="text" id="manualInput" placeholder="Manual" oninput="manualChange(this.value)">

        <script>
            let count = {latest_tally};
            const countElement = document.getElementById('count');
            const manualInputElement = document.getElementById('manualInput');

            function updateCount() {{
                countElement.textContent = count;
                manualInputElement.value = count; // Update the manual input field when count changes
            }}

            function increment() {{
                count++;
                updateCount();
            }}

            function decrement() {{
                if (count > 0) {{
                    count--;
                    updateCount();
                }}
            }}

            function manualChange(value) {{
                const parsedValue = parseInt(value, 10);
                if (!isNaN(parsedValue)) {{
                    count = parsedValue;
                    updateCount();
                }}
            }}
        </script>
    </body>
    </html>
    '''

    return html_content

# Save historical reporting HTML to a file
historical_html_content = generate_historical_html(data)
with open(os.path.join(script_directory, 'historical_reporting.html'), 'w') as f:
    f.write(historical_html_content)

# Save new count page HTML to a file
latest_entry = data[-1] if data else {'Tally': 0}  # If data is empty, set initial Tally to 0
new_count_html_content = generate_new_count_html(latest_entry['Tally'])
with open(os.path.join(script_directory, 'new_count_page.html'), 'w') as f:
    f.write(new_count_html_content)

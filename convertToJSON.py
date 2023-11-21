import pandas as pd

# Load Excel file
excel_file_path = 'your_excel_file.xlsx'
df = pd.read_excel(excel_file_path)

# Convert timestamp to datetime for the date column
df['Date'] = pd.to_datetime(df['Date'], unit='ms').dt.strftime('%m/%d/%Y') 

# Convert to JSON
json_data = df.to_json(orient='records', indent=2)

# Save JSON to a file
output_json_file_path = 'output.json'
with open(output_json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Conversion complete. JSON file saved at: {output_json_file_path}")
print(df.columns)
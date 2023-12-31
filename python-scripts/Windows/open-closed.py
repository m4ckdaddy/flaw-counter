import pandas as pd

# Load the CSV file
file_path = 'application.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Filter the DataFrame for rows where the app_name is 'truist-reporting'
filtered_df = df[df['app_name'] == 'truist-reporting']

# Separate the filtered data into two DataFrames based on the 'status' value
open_df = filtered_df[filtered_df['status'] == 'Open']
closed_df = filtered_df[filtered_df['status'] == 'Closed']

# Save the 'Open' status data to a CSV file
output_file_path_open = 'Open-Flaws.csv'  # Replace with your desired output file path
open_df.to_csv(output_file_path_open, index=False)

# Save the 'Closed' status data to a CSV file
output_file_path_closed = 'Closed-Flaws.csv'  # Replace with your desired output file path
closed_df.to_csv(output_file_path_closed, index=False)


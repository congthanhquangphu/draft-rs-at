import pandas as pd
import os

def excel_to_csv(excel_file, output_folder):
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Get the base name of the file (without extension)
    base_name = os.path.splitext(os.path.basename(excel_file))[0]
    
    # Create the output CSV file path
    csv_file = os.path.join(output_folder, f"{base_name}.csv")
    
    # Convert to CSV
    df.to_csv(csv_file, index=False)
    
    print(f"Converted {excel_file} to {csv_file}")
    return csv_file

def convert_all_excel_files(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    converted_files = []
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.xlsx'):
            excel_file = os.path.join(input_folder, filename)
            csv_file = excel_to_csv(excel_file, output_folder)
            converted_files.append(csv_file)
    
    return converted_files

# Define the input and output folders
input_folder = os.path.join('data', 'excel')
output_folder = os.path.join('data', 'csv')

# Run the conversion
converted_files = convert_all_excel_files(input_folder, output_folder)

# Print the results
print(f"Converted files: {converted_files}")
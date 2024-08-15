import os
import pandas as pd
import json
import re

# Define a function to clean the text data by removing POS tags, annotations, and repetitive symbols
def clean_text_pos(text):
    # Remove POS tags and numeric values after each word (e.g., _PRP$_57.57)
    cleaned_text = re.sub(r'_[A-Z$]+_\d+(\.\d+)?', '', text)
    
    # Remove repetitive symbols like @ @ @ @ @
    cleaned_text = re.sub(r'(@\s*)+', '', cleaned_text)
    
    # Remove extra spaces and strip leading/trailing spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

# Define a function to process a single CSV file
def process_csv_file(input_file_path, output_file_path):
    # Load the CSV file
    df = pd.read_csv(input_file_path)

    # Check if either 'text' or 'text_pos' column exists
    if 'text' in df.columns:
        # Use the 'text' column directly if it exists
        df['cleaned_text'] = df['text']
    elif 'text_pos' in df.columns:
        # If 'text' column doesn't exist, clean the 'text_pos' column
        df['cleaned_text'] = df['text_pos'].apply(clean_text_pos)
    else:
        print(f"Skipping {input_file_path}: Neither 'text' nor 'text_pos' column found.")
        return

    # Create a list of dictionaries containing the cleaned text
    cleaned_data = [{"text": row['cleaned_text']} for _, row in df.iterrows()]

    # Save the cleaned text data as a JSON file
    with open(output_file_path, 'w') as json_file:
        json.dump(cleaned_data, json_file, ensure_ascii=False, indent=2)

# Define a function to process all CSV files in a folder
def process_csv_folder(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all CSV files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_name = os.path.splitext(file_name)[0] + '.json'
            output_file_path = os.path.join(output_folder, output_file_name)

            # Process each CSV file
            process_csv_file(input_file_path, output_file_path)
            print(f"Processed {input_file_path} -> {output_file_path}")

# Example usage
input_folder = 'CoANZSE/csv'  # Replace with your input folder path
output_folder = 'CoANZSE/CoANZSE_dataset'  # Replace with your output folder path

# Process all CSV files in the folder
process_csv_folder(input_folder, output_folder)
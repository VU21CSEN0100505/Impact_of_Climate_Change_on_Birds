import os
import pandas as pd

# Paths to the occurrence files
occurrence_paths = [
    r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\0018853-241126133413365\occurrence.txt",
    r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\0018869-241126133413365\occurrence.txt"
]
                                            
# Function to load and display data from occurrence files
def process_occurrence_files(file_paths):
    combined_data = []  # List to hold data from all files

    for file_path in file_paths:
        if os.path.exists(file_path):
            print(f"Processing file: {file_path}")
            try:
                # Read the file into a DataFrame
                bird_data = pd.read_csv(file_path, sep="\t")  # Adjust delimiter if necessary
                print(f"File {file_path} loaded successfully!")
                print(f"Sample Data:\n{bird_data.head()}\n")
                
                # Append the data to the combined list
                combined_data.append(bird_data)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
        else:
            print(f"File not found: {file_path}")
    
    # Combine all data into a single DataFrame (optional)
    if combined_data:
        combined_df = pd.concat(combined_data, ignore_index=True)
        print("Combined Data Sample:")
        print(combined_df.head())
        return combined_df
    else:
        print("No data to process.")
        return None

# Process the occurrence files
bird_data_combined = process_occurrence_files(occurrence_paths)

# Optional: Save combined data to a new file
if bird_data_combined is not None:
    output_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\combined_occurrence.csv"
    bird_data_combined.to_csv(output_path, index=False)
    print(f"Combined data saved to {output_path}")

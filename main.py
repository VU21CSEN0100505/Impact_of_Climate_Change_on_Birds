import os
import pandas as pd

occurrence_paths = [
    r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\0018853-241126133413365\occurrence.txt",
    r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\0018869-241126133413365\occurrence.txt"
]
                                            
def process_occurrence_files(file_paths):
    combined_data = []  
    for file_path in file_paths:
        if os.path.exists(file_path):
            print(f"Processing file: {file_path}")
            try:
                bird_data = pd.read_csv(file_path, sep="\t")  
                print(f"File {file_path} loaded successfully!")
                print(f"Sample Data:\n{bird_data.head()}\n")
                
                combined_data.append(bird_data)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
        else:
            print(f"File not found: {file_path}")
    
    if combined_data:
        combined_df = pd.concat(combined_data, ignore_index=True)
        print("Combined Data Sample:")
        print(combined_df.head())
        return combined_df
    else:
        print("No data to process.")
        return None

bird_data_combined = process_occurrence_files(occurrence_paths)

if bird_data_combined is not None:
    output_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\combined_occurrence.csv"
    bird_data_combined.to_csv(output_path, index=False)
    print(f"Combined data saved to {output_path}")

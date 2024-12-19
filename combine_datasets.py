import os
import pandas as pd

occurrence_paths = [
    r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\0018853-241126133413365\occurrence.txt",
    r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\0018869-241126133413365\occurrence.txt"
]

def combine_datasets(file_paths, output_path):
    combined_data = []

    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                bird_data = pd.read_csv(file_path, sep="\t")
                combined_data.append(bird_data)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
        else:
            print(f"File not found: {file_path}")

    if combined_data:
        combined_df = pd.concat(combined_data, ignore_index=True)
        combined_df.to_csv(output_path, index=False)
        print(f"Combined data saved to {output_path}")
    else:
        print("No data to combine.")

output_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\combined_occurrence.csv"
combine_datasets(occurrence_paths, output_path)

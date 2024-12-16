import pandas as pd
path1 = "climate change/bird dataset/0018853-241126133413365/occurrence.txt"
path2 = "climate change/bird dataset/0018869-241126133413365/occurrence.txt"

data1 = pd.read_csv(path1, sep="\t")  
data2 = pd.read_csv(path2, sep="\t")

print("Dataset 1:")
print(data1.head())
print("\nDataset 2:")
print(data2.head())

combined_data = pd.concat([data1, data2], ignore_index=True)

print("Combined Dataset:")
print(combined_data.head())

combined_data = combined_data.drop_duplicates()

print("Number of rows after removing duplicates:", len(combined_data))

print("Missing Values:")
print(combined_data.isnull().sum())

combined_data.to_csv("climate change/bird dataset/combined_occurrence.csv", index=False)
print("Combined dataset saved as 'combined_occurrence.csv'")

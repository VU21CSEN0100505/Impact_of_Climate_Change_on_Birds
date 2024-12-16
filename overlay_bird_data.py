import pandas as pd
import rasterio
import matplotlib.pyplot as plt

# Load bird data
bird_data_path = "combine_datasets.csv"
birds = pd.read_csv(bird_data_path)

# Load the climate map
map_file = "climate change/climate data/current/wc2.1_2.5m_bio/wc2.1_2.5m_bio_1.tif"
with rasterio.open(map_file) as src:
    map_data = src.read(1)
    transform = src.transform

# Plot the map and bird points
plt.figure(figsize=(8, 6))
plt.imshow(map_data, cmap='viridis', extent=(src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top))
plt.colorbar(label="Map Data")
plt.title("Bird Locations on Climate Map")

# Add bird points
for _, row in birds.iterrows():
    plt.scatter(row["Longitude"], row["Latitude"], label=row["Species"], s=10, alpha=0.7)

plt.legend(loc="upper right")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

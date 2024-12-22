import os
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
import pandas as pd
from rasterio.plot import show
import numpy as np

# Paths to datasets
combined_data_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\combined_occurrence.csv"
time_periods = {
    "current": r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\climate data\current",
    "future_2021_2040": r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\climate data\future 2021-2040",
    "future_2041_2060": r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\climate data\future 2041-2060",
    "future_2081_2100": r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\climate data\future 2081-2100"
}

def find_first_tif(folder_path):
    """
    Find the first .tif file in the given folder and return its path.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".tif"):
                return os.path.join(root, file)
    return None

def overlay_bird_data(map_path, bird_data_path):
    """
    Overlay bird data on a raster map.
    """
    try:
        # Read bird occurrence data
        bird_data = pd.read_csv(bird_data_path)

        # Ensure required columns exist
        if 'decimalLongitude' not in bird_data.columns or 'decimalLatitude' not in bird_data.columns:
            raise ValueError("The dataset does not contain required columns 'decimalLongitude' and 'decimalLatitude'.")

        bird_gdf = gpd.GeoDataFrame(
            bird_data,
            geometry=gpd.points_from_xy(bird_data.decimalLongitude, bird_data.decimalLatitude),
            crs="EPSG:4326"
        )

        # Open the raster map
        with rasterio.open(map_path) as src:
            raster_data = src.read(1)

            # Replace invalid or NaN values with a default (e.g., NaN for plotting)
            raster_data = np.where(np.isfinite(raster_data), raster_data, np.nan)

            # Plot the raster map
            fig, ax = plt.subplots(figsize=(10, 8))
            show(raster_data, transform=src.transform, cmap="viridis", ax=ax)
            
            # Overlay the bird data points
            bird_gdf.plot(ax=ax, color="red", markersize=5, label="Bird Locations")
            
            # Add additional details
            plt.title(f"Bird Data Overlay on Map: {os.path.basename(map_path)}")
            plt.xlabel("Longitude")
            plt.ylabel("Latitude")
            plt.legend()
            plt.show()

    except Exception as e:
        print(f"Error while overlaying bird data on map: {e}")

# Main execution
if __name__ == "__main__":
    # Ask the user to select a time period
    print("Select a time period for climate data:")
    for i, period in enumerate(time_periods.keys(), start=1):
        print(f"{i}. {period}")
    
    try:
        choice = int(input("Enter the number corresponding to your choice: ").strip())
        selected_period = list(time_periods.keys())[choice - 1]
        climate_folder = time_periods[selected_period]

        # Find the first available .tif file for the selected period
        map_path = find_first_tif(climate_folder)
        if not map_path:
            print(f"No .tif files found in {climate_folder}. Please add climate data and try again.")
        else:
            overlay_bird_data(map_path, combined_data_path)

    except (ValueError, IndexError):
        print("Invalid choice. Please run the script again and select a valid option.")

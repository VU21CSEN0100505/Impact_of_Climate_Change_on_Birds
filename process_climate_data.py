import os
import rasterio
import matplotlib.pyplot as plt

# Base folder for climate data
base_path = r"climate change/climate data"

# Subfolders for different time periods
time_periods = {
    "current": os.path.join(base_path, "current"),
    "future_2021_2040": os.path.join(base_path, "future 2021-2040"),
    "future_2041_2060": os.path.join(base_path, "future 2041-2060"),
    "future_2081_2100": os.path.join(base_path, "future 2081-2100")
}

def display_raster(file_path):
    """
    Open and display a raster file.
    """
    try:
        with rasterio.open(file_path) as src:
            # Read the first band of the raster
            raster_data = src.read(1)
            
            # Display metadata
            print(f"Metadata for {file_path}:")
            print(f"  CRS: {src.crs}")
            print(f"  Dimensions: {src.width} x {src.height}")
            print(f"  Transform: {src.transform}")
            
            # Plot the raster data
            plt.figure(figsize=(8, 6))
            plt.imshow(raster_data, cmap='viridis')
            plt.colorbar(label="Raster Data")
            plt.title(f"Raster Visualization: {os.path.basename(file_path)}")
            plt.xlabel("Longitude")
            plt.ylabel("Latitude")
            plt.show()
    except Exception as e:
        print(f"Error opening file {file_path}: {e}")

def find_and_display_raster():
    """
    Ask the user for a file name or path and display the raster.
    """
    print("\nAvailable time periods:")
    for key in time_periods:
        print(f"  {key}: {time_periods[key]}")
    
    # Ask the user to select a time period
    period = input("\nEnter the time period (e.g., 'current', 'future_2021_2040'): ").strip()
    if period not in time_periods:
        print("Invalid time period. Please try again.")
        return
    
    # List subfolders in the selected time period
    folder_path = time_periods[period]
    print(f"\nAvailable subfolders in {period}:")
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    for subfolder in subfolders:
        print(f"  {subfolder}")
    
    # Ask the user to select a subfolder
    subfolder = input("\nEnter the subfolder name (e.g., 'wc2.1_2.5m_bio'): ").strip()
    subfolder_path = os.path.join(folder_path, subfolder)
    if not os.path.exists(subfolder_path):
        print("Invalid subfolder. Please try again.")
        return
    
    # List .tif files in the selected subfolder
    tif_files = [f for f in os.listdir(subfolder_path) if f.endswith(".tif")]
    print(f"\nAvailable .tif files in {subfolder}:")
    for tif_file in tif_files:
        print(f"  {tif_file}")
    
    # Ask the user to select a .tif file
    tif_file = input("\nEnter the file name (e.g., 'wc2.1_2.5m_bio_1.tif'): ").strip()
    file_path = os.path.join(subfolder_path, tif_file)
    if not os.path.exists(file_path):
        print("Invalid file name. Please try again.")
        return
    
    # Display the selected raster
    display_raster(file_path)

# Main program loop
while True:
    print("\n--- Climate Data Map Viewer ---")
    find_and_display_raster()
    
    # Ask if the user wants to view another map
    another = input("\nDo you want to view another map? (yes/no): ").strip().lower()
    if another != "yes":
        print("Exiting the Climate Data Map Viewer. Goodbye!")
        break

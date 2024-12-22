import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Base folder for climate data
base_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\climate data"

time_periods = {
    "current": os.path.join(base_path, "current"),
    "future_2021_2040": os.path.join(base_path, "future 2021-2040"),
    "future_2041_2060": os.path.join(base_path, "future 2041-2060"),
    "future_2081_2100": os.path.join(base_path, "future 2081-2100")
}

def display_raster(file_path):
    """
    Open and display a raster file with improved handling of invalid values.
    """
    try:
        with rasterio.open(file_path) as src:
            raster_data = src.read(1)

            # Replace invalid or NaN values with a default
            raster_data = np.where(np.isfinite(raster_data), raster_data, np.nan)

            print(f"\nMetadata for {file_path}:")
            print(f"  CRS: {src.crs}")
            print(f"  Dimensions: {src.width} x {src.height}")
            print(f"  Transform: {src.transform}")

            plt.figure(figsize=(8, 6))
            img = plt.imshow(raster_data, cmap='viridis', interpolation='nearest')
            plt.colorbar(img, label="Raster Data")
            plt.title(f"Raster Visualization: {os.path.basename(file_path)}")
            plt.xlabel("Longitude")
            plt.ylabel("Latitude")
            plt.show()
    except Exception as e:
        print(f"Error opening file {file_path}: {e}")

def get_choice(options, prompt):
    """
    Display a list of options for the user to choose from.
    """
    while True:
        print(prompt)
        for i, option in enumerate(options, start=1):
            print(f"  {i}. {option}")

        try:
            choice = int(input("Enter your choice (number): ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def find_and_display_raster():
    """
    Guide the user through folder and file selection, then display the raster.
    """
    # Step 1: Select the time period
    period = get_choice(list(time_periods.keys()), "\nSelect a time period:")
    folder_path = time_periods[period]

    # Step 2: Check for .tif files in the selected folder
    tif_files = [f for f in os.listdir(folder_path) if f.endswith(".tif")]

    if period == "current":
        # For 'current', navigate subfolders to locate .tif files
        subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        if not subfolders:
            print("No subfolders available in this time period.")
            return

        subfolder = get_choice(subfolders, f"\nSelect a subfolder in '{period}':")
        subfolder_path = os.path.join(folder_path, subfolder)

        tif_files = [f for f in os.listdir(subfolder_path) if f.endswith(".tif")]
        if not tif_files:
            print("No .tif files available in the selected subfolder.")
            return

        tif_file = get_choice(tif_files, f"\nSelect a .tif file in '{subfolder}':")
        file_path = os.path.join(subfolder_path, tif_file)

    else:
        # For future periods, look directly in the folder
        if not tif_files:
            print("No .tif files available in this time period.")
            return

        tif_file = get_choice(tif_files, f"\nSelect a .tif file in '{period}':")
        file_path = os.path.join(folder_path, tif_file)

    # Step 3: Display the raster
    display_raster(file_path)

# Main loop
while True:
    print("\n--- Climate Data Map Viewer ---")
    find_and_display_raster()

    another = input("\nDo you want to view another map? (yes/no): ").strip().lower()
    if another != "yes":
        print("Exiting the Climate Data Map Viewer. Goodbye!")
        break

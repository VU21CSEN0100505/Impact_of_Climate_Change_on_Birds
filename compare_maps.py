import os
import rasterio
import matplotlib.pyplot as plt
import numpy as np

# Define paths to the datasets
base_path = r"Capstone 2/Climate Change/climate data"
time_periods = {
    "current": os.path.join(base_path, "current"),
    "future_2021_2040": os.path.join(base_path, "future 2021-2040"),
    "future_2041_2060": os.path.join(base_path, "future 2041-2060"),
    "future_2081_2100": os.path.join(base_path, "future 2081-2100"),
}

# List available layers for a given variable
def list_layers(folder, variable_prefix):
    """
    List files matching a given variable prefix in a folder or its subfolders.
    """
    file_list = []
    for root, dirs, files in os.walk(folder):  # Recursively walk through subfolders
        for file in files:
            if file.startswith(variable_prefix) and file.endswith(".tif"):
                file_list.append(os.path.join(root, file))
    return file_list

# Compare two maps and visualize the differences
def compare_maps(map1_path, map2_path, output_path):
    """
    Compare two raster maps and save the difference as a visual map.
    """
    try:
        with rasterio.open(map1_path) as src1, rasterio.open(map2_path) as src2:
            if src1.shape != src2.shape:
                raise ValueError("The two maps have different dimensions and cannot be compared.")

            # Read raster data
            data1 = src1.read(1)
            data2 = src2.read(1)

            # Calculate the difference
            difference = data2 - data1

            # Replace invalid or extreme values for clarity
            difference = np.where(np.isfinite(difference), difference, np.nan)

            # Plot the difference
            plt.figure(figsize=(10, 8))
            plt.imshow(
                difference,
                cmap='coolwarm',
                extent=(src1.bounds.left, src1.bounds.right, src1.bounds.bottom, src1.bounds.top)
            )
            plt.colorbar(label="Difference (Future - Current)")
            plt.title(f"Comparison: {os.path.basename(map2_path)} - {os.path.basename(map1_path)}")
            plt.xlabel("Longitude")
            plt.ylabel("Latitude")

            # Save the map
            plt.savefig(output_path)
            plt.show()
            print(f"Comparison map saved to: {output_path}")

    except Exception as e:
        print(f"Error comparing maps: {e}")

# Main function to drive user input and comparison
def main():
    print("\n--- Climate Change Map Comparison ---")

    # Step 1: Select the variable to compare
    variables = ["bio", "prec", "tavg", "tmax", "tmin"]
    print("\nAvailable Variables:")
    for i, var in enumerate(variables, 1):
        print(f"  {i}. {var}")
    
    variable_choice = int(input("Select a variable to compare (number): ")) - 1
    variable_prefix = f"wc2.1_2.5m_{variables[variable_choice]}"

    # Step 2: Select the time period for comparison
    print("\nAvailable Time Periods:")
    for i, (key, path) in enumerate(time_periods.items(), 1):
        print(f"  {i}. {key.replace('_', ' ').capitalize()}")

    time_choice_1 = int(input("Select the first time period (number): ")) - 1
    time_choice_2 = int(input("Select the second time period (number): ")) - 1

    time_periods_keys = list(time_periods.keys())
    folder1 = time_periods[time_periods_keys[time_choice_1]]
    folder2 = time_periods[time_periods_keys[time_choice_2]]

    # Step 3: Select a layer from the chosen variable
    print("\nAvailable Layers in First Time Period:")
    layers1 = list_layers(folder1, variable_prefix)
    for i, layer in enumerate(layers1, 1):
        print(f"  {i}. {os.path.basename(layer)}")
    
    if not layers1:
        print("No layers found for the selected variable in the first time period.")
        return

    layer_choice1 = int(input("Select a layer from the first time period (number): ")) - 1
    map1_path = layers1[layer_choice1]

    print("\nAvailable Layers in Second Time Period:")
    layers2 = list_layers(folder2, variable_prefix)
    for i, layer in enumerate(layers2, 1):
        print(f"  {i}. {os.path.basename(layer)}")
    
    if not layers2:
        print("No layers found for the selected variable in the second time period.")
        return

    layer_choice2 = int(input("Select a layer from the second time period (number): ")) - 1
    map2_path = layers2[layer_choice2]

    # Step 4: Perform the comparison
    output_filename = f"comparison_{variables[variable_choice]}_{time_periods_keys[time_choice_1]}_vs_{time_periods_keys[time_choice_2]}.png"
    output_path = os.path.join(base_path, output_filename)
    compare_maps(map1_path, map2_path, output_path)

# Run the script
if __name__ == "__main__":
    main()

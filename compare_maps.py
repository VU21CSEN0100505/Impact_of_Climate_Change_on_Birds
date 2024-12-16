import rasterio
import matplotlib.pyplot as plt

current_map = "climate change/climate data/current/wc2.1_2.5m_tavg/wc2.1_2.5m_tavg_1.tif"
future_map = "climate change/climate data/future 2081-2100/wc2.1_2.5m_tavg/wc2.1_2.5m_tavg_1.tif"

with rasterio.open(current_map) as src_current, rasterio.open(future_map) as src_future:
    current_data = src_current.read(1)
    future_data = src_future.read(1)

difference = future_data - current_data

plt.figure(figsize=(8, 6))
plt.imshow(difference, cmap='coolwarm', extent=(src_current.bounds.left, src_current.bounds.right, src_current.bounds.bottom, src_current.bounds.top))
plt.colorbar(label="Temperature Difference (Future - Current)")
plt.title("Temperature Change from Current to Future")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("temperature_change_map.png")  
plt.show()

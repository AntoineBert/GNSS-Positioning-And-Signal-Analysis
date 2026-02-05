import rasterio
import numpy as np
import matplotlib.pyplot as plt
import traitement
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "assets", "ensta_2015.jpg")

# Ouvrir l'image avec rasterio
with rasterio.open(image_path) as src:
    transform = src.transform
    RMC = traitement.list_RMC[-1]
    latitude = RMC.latitude
    longitude = RMC.longitude
    x, y = transform * (longitude, latitude)
    nx = src.width
    ny = src.height
    nb = src.count
    image = np.zeros((ny, nx, nb), dtype=np.uint8)
    for band_idx in range(nb):
        band = src.read(band_idx + 1)
        image[:, :, band_idx] = band

# Afficher l'image
plt.figure()
plt.xlim([500, 1000])
plt.ylim([1200, 800])
plt.imshow(image)
plt.plot(x, y, 'ro', markersize=10)
plt.show()





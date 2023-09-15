import cv2
import numpy as np
from src.utils import load_config

 # Load the configuration file
config = load_config("config.yaml")

# Load variables from the configuration file
nir_image_filepath = config["nir_image_filepath"]
rgb_image_filepath = config["rgb_image_filepath"]
ndvi_threshold = config["ndvi_threshold"]
pixel_sixe_in_meters = config["pixel_sixe_in_meters"]

# Load NIR and RGB orthomosaic images
nir_band = cv2.imread(nir_image_filepath, cv2.IMREAD_GRAYSCALE)
rgb_image = cv2.imread(rgb_image_filepath) # Apply white balance in preprocessing

# Extract the red channel from the RGB image
red_band = rgb_image[:,:,2] 

# Calculate NDVI
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Threshold NDVI to identify vegetation
threshold = ndvi_threshold  # You may need to adjust this threshold
vegetation_mask = ndvi > threshold

# Calculate the Leaf Area Index (LAI)
pixel_size = pixel_sixe_in_meters  # The size of each pixel in meters, adjust as needed
lai = np.sum(vegetation_mask) * pixel_size**2

print(f"Total LAI: {lai}")

# Display the NDVI image (for visualization)
cv2.imshow('NDVI Image', (ndvi * 255).astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Vineyard disease detection using vegetation indices and grids

## Overview

This Python script is specifically designed for assessing the health of a vineyard using data captured by Unmanned Aerial Vehicles (UAVs). It utilizes both RGB and multispectral sensors, enabling the analysis of orthomosaic images for vineyard health assessment. It calculates vegetation indices, such as NDVI (Normalized Difference Vegetation Index), and extracts essential information related to vineyard health, including the total vineyard area, plant health, and NDVI mean values.

## Prerequisites

Before using this tool, ensure you have the following prerequisites:

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/)
- [git](https://git-scm.com/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ICAERUS-EU/ddal.git
   cd vineyard-health-assessment
   ```

2. Install the required packages by running:
    ```bash
    pip install -r requirements.txt
    ```

3. Modify the **config.yaml** file to specify the file paths and configuration settings required for your specific vineyard dataset.

4. Run the script
    ```bash
    python main.py
    ```

## Configuration

The **config.yaml** file contains the following configuration options:

- **nir_image_filepath**: Filepath to the Near-Infrared (NIR) image.
- **rgb_image_filepath**: Filepath to the RGB image.
- **grid_image_filepath**: Filepath to save the output image with a grid overlay.
- **grid_size_x**: Width of the grid cells in pixels.
- **grid_size_y**: Height of the grid cells in pixels.
- **vineyard_total_hectareas**: Total area of the vineyard in hectares.
- **outside_vineyard_color**: Color representing areas outside the vineyard.
- **ground_color**: Color representing the ground.

## Output

The script generates an output image with a grid overlay, which can be found at the specified grid_image_filepath. Additionally, it prints information about vineyard health, including:

- Total vineyard pixels
- Total plant pixels
- Vine area in square meters
- NDVI mean healthiness value
- NDVI mean value as a percentage

## Authors
- [**Noumena**](https://noumena.io/es/) - [Paula Osés](https://www.linkedin.com/in/paula-os%C3%A9s-noguero-382937152)

## License
This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit/) file for details.

## Acknowledgements
This project is funded by the European Union, grant ID 101060643.

<img src="https://rea.ec.europa.eu/sites/default/files/styles/oe_theme_medium_no_crop/public/2021-04/EN-Funded%20by%20the%20EU-POS.jpg" alt="https://cordis.europa.eu/project/id/101060643" width="200"/>
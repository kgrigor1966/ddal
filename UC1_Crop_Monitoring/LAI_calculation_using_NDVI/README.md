# VINEYARD LEAF AREA CALCULATOR (LAI) USING NDVI


This Python script calculates the Leaf Area Index (LAI) of a vineyard from an orthomosaic image using the Normalized Difference Vegetation Index (NDVI) method.

## Prerequisites

Before using this script, make sure you have the following dependencies installed:

- Python (>= 3.0)
- OpenCV
- NumPy
- PyYAML

You can install the required Python packages using `pip`:

```bash
pip install opencv-python numpy pyyaml
```

## Usage
1. Clone this repository to your local machine
```bash
git clone https://github.com/ICAERUS-EU/ddal.git
```

2. Place your orthomosaic image in the repository directory and update the image file name in the Python script.

3. Run the script 
```bash
python main.py
```
4. The script will display the total LAI value on the console and show a visual representation of the NDVI image.

## Customization 
You may need to adjust the following parameters in the script to suit your specific image and requirements:

- **threshold**: The NDVI threshold for identifying vegetation pixels. Modify this value to separate vegetation from non-vegetation.
- **pixel_size**: The size of each pixel in meters. Adjust this value according to the spatial resolution of your orthomosaic image.

## Authors
- [**Noumena**](https://noumena.io/es/) - [Paula Osés](https://www.linkedin.com/in/paula-os%C3%A9s-noguero-382937152)

## License
This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit/) file for details.

## Acknowledgements
This project is funded by the European Union, grant ID 101060643.

<img src="https://rea.ec.europa.eu/sites/default/files/styles/oe_theme_medium_no_crop/public/2021-04/EN-Funded%20by%20the%20EU-POS.jpg" alt="https://cordis.europa.eu/project/id/101060643" width="200"/>

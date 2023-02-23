# Use Case x: Subject

This folder contains datasets and models subfolders. Which respectively contain datasets relating to the use-case, as found in the data-extraction task for ICAERUS WP1/T.2.
The data-extraction task identified the following papers and respective models and datasets:

| Title | Model in this repo | Dataset in this repo |
| ----- | ----- | -----| 
| [Cattle counting in the wild with geolocated aerial images in large pasture areas](https://www.sciencedirect.com/science/article/abs/pii/S0168169921003719?via%3Dihub) | x | x |
| [Automatic activity tracking of goats using drone camera](https://www.sciencedirect.com/science/article/abs/pii/S0168169918312894?via%3Dihub) | x | x |
| [Visual identification of individual Holstein-Friesian cattle via deep metric learning](https://www.sciencedirect.com/science/article/abs/pii/S0168169921001514?via%3Dihub) | x | x | 
## Datasets

Under the datasets folder, the following datasets are included:

| Article title | Dataset title | Dataset subject | Original dataset link | 
| ----- | ----- | ----- | ----- |
| Cattle counting in the wild with geolocated aerial images in large pasture areas|  [cattle_images_UAV](https://github.com/ICAERUS-EU/ddal/blob/main/UC3/datasets/cattle_images_UAV.md) | Image sets of cattle obtained by UAV | [cattle_images_link](https://vhasoares.github.io/downloads.html)
| Automatic activity tracking of goats using drone camera|  [goat_images_UAV](https://github.com/ICAERUS-EU/ddal/blob/main/UC3/datasets/goat_images_UAV.md) | Image sets of goats obtained by UAV | [goat_images_link](https://gitlab.com/inra-urz/drone-goat-detection)
| Visual identification of individual Holstein-Friesian cattle via deep metric learning|  [Holstein_Friesian_cattle](https://github.com/ICAERUS-EU/ddal/blob/main/UC3/datasets/Holstein_Friesian_cattle.md) | Image sets of Holstein Friesian cattle | [Holstein_Friesian_cattle_link](https://data.bris.ac.uk/data/dataset/10m32xl88x2b61zlkkgz3fml17)


## Models

Under the models folder, the following models are included:

| Article title | Model title | Model Classification | Original model link |
| ----- | ----- | ----- | ----- |
| Cattle counting in the wild with geolocated aerial images in large pasture areas | [tensorflow_detection_zoo](https://github.com/ICAERUS-EU/ddal/blob/main/UC3/models/deeplearning/tensorflow_detection_zoo.md) | Deep Learning: Object Detection | [tensorflow_detection_model_zoo_link](https://github.com/librahfacebook/Detection/blob/master/object_detection/g3doc/detection_model_zoo.md)
| Automatic activity tracking of goats using drone camera | [goat_detection](https://github.com/ICAERUS-EU/ddal/blob/main/UC3/models/deeplearning/goat_detection.md) | Color Threshold: Object detection | [goat_detection_model_link](https://gitlab.com/inra-urz/drone-goat-detection/-/tree/master/)
| Visual identification of individual Holstein-Friesian cattle via deep metric learning | [Holstein_Friesian_detection](https://github.com/ICAERUS-EU/ddal/blob/main/UC3/models/deeplearning/goat_detection.md) | Deep Learning: Object detection | [holstein_friesian_detection_model_link](https://github.com/CWOA/MetricLearningIdentification)


# Use Case 4: Forestry and biodiveristy monitoring

This folder contains datasets and models subfolders. Which respectively contain datasets relating to the use-case, as found in the data-extraction task for ICAERUS WP1/T.2.
The data-extraction task identified the following papers and respective models and datasets:

| Title | Model in this repo | Dataset in this repo |
| ----- | ----- | -----| 
| [Predicting Tree Mortality Using Spectral Indices Derived from Multispectral UAV Imagery](https://www.mdpi.com/2072-4292/14/9/2195) | x | x |
| [Individual Sick Fir Tree (Abies mariesii) Identification in Insect Infested Forests by Means of UAV Images and Deep Learning](https://www.mdpi.com/2072-4292/13/2/260) |  | x |
| [A Forest Fire Recognition Method Using UAV Images Based on Transfer Learning](https://www.mdpi.com/1999-4907/13/7/975) |  | x |
| [Performance of unmanned aerial vehicle with thermal imaging, camera trap, and transect survey for monitoring of wildlife](https://iopscience.iop.org/article/10.1088/1755-1315/771/1/012011/meta) |  | x |
| [Antler detection from the sky: deer sex ratio monitoring using drone-mounted thermal infrared sensors](https://onlinelibrary.wiley.com/doi/full/10.1002/wlb3.01034) |  | x |


## Datasets

Under the datasets folder, the following datasets are included:

| Article title | Dataset title | Dataset subject | Original dataset link | 
| ----- | ----- | ----- | ----- |
| Predicting Tree Mortality Using Spectral Indices Derived from Multispectral UAV Imagery  |  [dataset_tree_mortality_prediction](https://github.com/ICAERUS-EU/ddal/blob/main/UC4/datasets/dataset_tree_mortality_prediction.md) | Tree mortality prediction | [Tree mortality dataset link](https://doi.org/10.6084/m9.figshare.17283116.v1)
| Individual Sick Fir Tree (Abies mariesii) Identification in Insect Infested Forests by Means of UAV Images and Deep Learning  |  [dataset_sick_fir_tree](https://github.com/ICAERUS-EU/ddal/blob/main/UC4/datasets/dataset_sick_fir_tree.md) | Classifying tree health and species class from RGB images | [Sick Fir Tree dataset](https://zenodo.org/record/4054338#.Y9pws9LMJhE)
| Performance of unmanned aerial vehicle with thermal imaging, camera trap, and transect survey for monitoring of wildlife | [dataset_animal_movement](https://github.com/ICAERUS-EU/ddal/blob/main/UC4/datasets/dataset_animal_movement.md) | Animal movement samples | [Animal movement dataset](https://datadryad.org/stash/dataset/doi:10.5061/dryad.79cnp5hxc)
| Antler detection from the sky: deer sex ratio monitoring using drone-mounted thermal infrared sensors| [dataset_deer_detection](https://github.com/ICAERUS-EU/ddal/blob/main/UC4/datasets/dataset_deer_detection.md) | Deer monitoring dataset| [deer monitoring](https://datadryad.org/stash/dataset/doi:10.5061/dryad.jm63xsjcr)

## Models

Under the models folder, the following models are included:

| Article title | Model title | Model Classification | Original model link |
| ----- | ----- | ----- | ----- |
| Predicting Tree Mortality Using Spectral Indices Derived from Multispectral UAV Imagery | [rf_predicting_tree_mortality](https://github.com/ICAERUS-EU/ddal/blob/main/UC4/models/rf_predicting_tree_mortality.md) | Machine Learning: Random Forest | [random_forest_link](https://github.com/KaiOBerg/Predicting-tree-mortality-using-spectral-indices-derived-from-multispectral-UAV-imagery/blob/main/final%20model.R)

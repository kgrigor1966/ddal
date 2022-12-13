<img src="https://icaerus.eu/wp-content/uploads/2022/09/ICAERUS-logo-white.svg" align="right" />

# Drone Data Analytics Library
This repository contains a large set of models used in drone-analytics of five different drone use-cases:
- UC1: Crop Monitoring
- UC2: Crop Spraying
- UC3: Forestry/Biodiversity
- UC4: Livestock Monitoring
- UC5: Rural Transportation

An explanation on how these models were found can be read in the [wiki](https://github.com/ICAERUS-EU/ddal/wiki/Methodology:-finding-the-models).

## Repo structure
The repository is structured into a generic processing library, with models used across the use-cases. In addition, each use-case has a specific model-database. Which also includes deep learning models.

    .
    ├── models                  # library of wider applicable models
    ├── datasets                # library of wider applicable datasets
    ├── UCx                     # use-case specific models and datasets
        ├── models              # analytical models implemented in the notebooks
            └── deeplearning    # raw weights and biases for deep learning models
        ├── datasets            # open datasets available to use and test with
        └── notebooks           # set of notebooks that run the models and datasets, to be used as examples
    ├── docker                  # DOCKERFILES for various library environments
    ├── environment.yaml        # python requirements list to run the models in a jupyter environment
    ├── LICENSE
    └── README.md 

The models rely on various python packages being installed, which are stored under the environment.yaml.

## Getting started
As drone analytics leans on machine learning, computer vision, data science and various other disciplines, there are a lot of inter-acting packages and libraries the ddal relies on.
The most important are:
- python (3.9)
- pytorch 
    - torchvision
    - rastervision
- geopandas
- pyodm (and a [node-odm](https://github.com/OpenDroneMap/NodeODM) instance if you want orthomosaics in python)
- xarray

There are 3 different ways to get started: 1. Anaconda on bare metal, 2. A precompiled docker-container, 3. JupyterHub access

### 1. Anaconda on bare metal
To run on the ddal on your own machine, Mamboforge is used as a package manager.
1. a) Please install mambaforge on your machine, [here](https://github.com/conda-forge/miniforge#mambaforge).
1. b) in the installer, make sure that desktop shortcuts are enabled

2. Download this repository on your machine, navigate to your preferred directory and run:
```
    git pull https://github.com/icaerus-eu/ddal.git
```
Or download this repository as a .zip file from the top-right green button: 'Download ZIP'
and extract to the preferred directory.

3. a) Search for the newly installed Miniforge prompt and run it
3. b) `cd` to the git directory and install the `environment.yaml` file under a new python-processing environment called `ddal`
```
    mamba env create -n ddal -file environment.yaml 
```
Activate the environment
```
    conda activate ddal
```

4. Run the jupyterlab environment to start processing and analysing drone-data with the different notebooks:
Run in your anaconda prompt, with the ddal environment activated:
```
    jupyter-lab
```
This will start the jupyter-lab instance in your browser, and you are ready to process drone data!

### 2. Docker

Not wanting to deal with anaconda and environment.yamls? Run the ddal environment in a docker container:
1. Install [Docker](https://docs.docker.com/get-docker/)
2. Start Docker
3. Start the Jupyter-lab docker
from your command-line with docker running:
this pulls the most recent ddal with all packages and libraries installed.
```
    docker run --rm -it -p 8888:8888 jurrain/ddal:latest
```
4. for transferring files and folders to and from docker, use:


### 3. JupyterHub
Even simpler, but more expensive is requesting access to a personal processing-enviroment running on the icaerus-jupyterhub:
[icaerus.jupyterhub.eu](icaerus.jupyterhub.eu) # DOES NOT EXIST (YET?)

This will run a jupyterlab instance in the cloud, with your own personal files and processing resources. However, you would need access with a personal account, requested at the main login, and will cost some money to pay for the resources.

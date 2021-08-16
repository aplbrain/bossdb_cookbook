# IARPA MICrONS Pinky 100 Dataset


This dataset was collected as part of the [Machine Intelligenece from Cortical Networks (MICrONS)](https://www.iarpa.gov/index.php/research-programs/microns) project, which seeks to revolutionize machine learning by reverse-engineering the algorithms of the brain.


This dataset consists of Electron Microscopy (EM) image data, segmentation data, and corresponding meshes of the cortical circuitry from the mouse visual cortex. This dataset was acquired and analyzed in the initial phase of the MICrONS project. It is a 250 x 140 x 90 µm volume from layer 2/3 of a P36 male mouse visual cortex imaged at 3.58 x 3.58 x 40 nm resolution with a dense segmentation, proofreading of all dendrites and axons of the 364 excitatory neurons in the volume, and dense synapse detection.

More information, including up to date release notes, can be found at the [MICrONS Explorer website](https://www.microns-explorer.org/phase1).

## Access through BossDB

The Electron Microscopy image data and the segmentation data are hosted on BossDB and can be accessed using [`intern`](https://github.com/jhuapl-boss). 

Dataset on BossDB: [https://bossdb.org/project/microns-pinky](https://bossdb.org/project/microns-pinky)

Dataset on the Boss Management Console: [https://api.bossdb.io/v1/mgmt/resources/microns](https://api.bossdb.io/v1/mgmt/resources/microns)


The segmentation and EM data are in separate collections on BossDB because the segmentations were performed on a downsampled version of the EM data (8nm x 8nm x 40nm). 

To view the EM data and the segmentation data at the same resolution you will need to pull the EM data using intern with `resolution = 1`. 


### Electron Microscopy data

The BossDB URI for the EM data is `bossdb://microns/pinky100/em`

### Segmentation data

The BossDB URI for the segmentation data is `bossdb://microns/pinky100_8x8x40/segmentation`


### Example Jupyter Notebook

View our example notebook for using intern to download and interact with the data here: [IARPA MICrONS Pinky 100](https://github.com/aplbrain/bossdb_cookbook/blob/main/notebooks/IARPA-MICrONS-Pinky100.ipynb)

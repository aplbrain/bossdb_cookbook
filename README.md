<div align="center">
  <img src="logo.png" height = '300px'>
</div>

# [BossDB](https://bossdb.org/) Cookbook: How-tos and Examples for using BossDB

BossDB (Brain Observatory Storage Service & Database) is a volumetric database for 3D and 4D neuroscience data.

The BossDB Cookbook repository is a collection of introductory notebooks and examples for interfacing with the BossDB system. 

For a quick introduction to BossDB, check out our [Getting Started Page](https://bossdb.org/get-started) and [introductory videos](https://www.youtube.com/channel/UCOKBtUhLgr-AtfGUxA-K6lg/featured).

Click here for a Binder of this repository and test out our notebooks in your browser: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aplbrain/bossdb_cookbook/HEAD?filepath=notebooks%2F)

### Accessing Data

Our public datasets have an example of how to access their data using [intern](https://github.com/jhuapl-boss/intern) at the top of their [project page](https://bossdb.org/projects), however many datasets have more data available than shown in that example, such as additional segmentations or scans. To access these datasets you will need to know the dataset URI. 

- [How To Find The BossDB URI For A Dataset](https://github.com/aplbrain/bossdb_cookbook/blob/main/How-To-Find-The-BossDB-URI-For-A-Dataset.md)


### Jupyter Notebooks
In the `notebooks` folder we have jupyter notebooks with more advanced examples of interacting with the BossDB system

- [Advanced Getting Started](https://github.com/aplbrain/bossdb_cookbook/blob/main/notebooks/Get-Started-Downloading-Data-with-Intern.ipynb)
- [Custom Dataset Classes for Pytorch](https://github.com/aplbrain/bossdb_cookbook/blob/main/notebooks/BossDB-Dataset-Classes-for-Pytorch-DataLoaders.ipynb)

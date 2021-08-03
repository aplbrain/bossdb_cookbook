# How to find the BossDB URI for a specific dataset

In order to access a specific dataset from BossDB, you will need to know the URI (Uniform Resource Locator) of the dataset in the BossDB system. 


### What is a BossDB URI?

In BossDB, we have an hierarchical organizational structure (similar to file system) where we organize datasets by "collection", "experiment", and "channel". Collections are the top structure containing metadata like the lab name and date of creation. Experiments are middle-level structure containing more metadata about coordinate frames (where data exists), resolution levels, voxel size. Channels are the lowest structure and the ones that actually contain volumetric data.

A BossDB URI is made up of the "collection", "experiment", and "channel" information of the dataset in the following format: `bossdb://collection/experiment/channel`

For example, the BossDB URI for the electron microscopy dataset from Dataset 1 of the Witvliet et al. 2020 project is  `bossdb://witvliet2020/Dataset_1/em` where `witvliet2020` is the collection name, `Dataset_1` refers to the experiment name, and `em` is the channel name. 

Many projects will have more than one channel per experiment, such as one channel for the EM volume and one channel for the corresponding segmentations of that data.

Many will also have more than one experiment per collection. The Witvliet et al. 2020 project, for example, has 8 EM volumes, with one experiment set up for each volume. 

### Where can I find the BossDB URI?

To find the URI, start on the [BossDB.org](https://bossdb.org/projects) project page for the specific project you are interested in. 

Each project page will have an initial example for accessing one of the channels using [Intern](https://github.com/jhuapl-boss/intern). 

```
# Import intern (pip install intern)
from intern import array

# Save a cutout to a numpy array in ZYX order:
em = array("bossdb://witvliet2020/Dataset_1/em")
data = em[210:220, 7457:9505, 11020:13068]
```

In the `Links` box in the lower right hand side of the page you will see a link `View at BossDB.io`. If you click this link it will take you to the Boss Management Console where you can view more information about the dataset. You may need to log in and you can use the public login information to do so:

```
Username: public-access
Password: public
```

The `View at BossDB.io` link will take you to the `Collection Details` page for the project. Here you can view the Collection name at the top of the page, a list of the available experiments, as well as properties and various metadata related to the collection. 

If you click the `Details` button to the right of one of the experiments, you will go to the `Experiment Details` page for that specific experiment. Here you can view the available channels, as well as properties and various metadata related to the experiment. Next to the `Details` button you will find a link to the view the channel on `Neuroglancer`.

If you click the `Details` button to the right of one of the channels, you will go to the `Channel Details` page for that specific channel. Here you can find the properties and various metadata related to the channel. 

**You will need to combine the Collection, Experiment, and Channel names to make the URI for each channel. It is also shown at the top of the `Channel Details` page for each channel.**






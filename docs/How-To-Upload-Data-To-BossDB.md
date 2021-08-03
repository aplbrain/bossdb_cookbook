# How to upload data to BossDB

In order to upload data, you will first need to make a BossDB Account and set up a config file for intern. See how to do this [here](https://github.com/aplbrain/bossdb_cookbook/blob/main/docs/BossDB-Set-Up-For-Private-Datasets.md). 

Next you will need to email `info@bossdb.org` to obtain permission in order to upload new data to the ecosystem. The permission to upload will be added to your bossdb username and you will then be able to add your own collections, experiments, and channels. 


There are two main ways to upload data onto bossDB:

1. Ingest-client: A python-based client that can be used to transfer arbitrary file formats (PNGs, TIFFs, Zarr) into the bossDB. Its highly scalable (uses SQS queues) and works well with parallel infrastructure. There is some set-up involved however and requires a little more hands-on experience. [https://github.com/jhuapl-boss/ingest-client](https://github.com/jhuapl-boss/ingest-client)

2. Intern's array(): Function within intern that uses bossDB's RESTful API to send data through HTTP. Works only with numpy arrays. Much less set-up but not efficient for large uploads.

Typically we use intern for anything smaller than 25 GB of data. If we are uploading anything larger than that, we set up an ingest job using the ingest client to handle the upload. Please contact us if you have a particularly large dataset to upload so we can help with the ingest. 

You can view a video version of this tutorial [here](https://youtu.be/gbbfWDThELU).

## Setting up resources

Just like how we need a collection, experiment, and channel to download data,  we need to create a new collection, experiment, and channel to upload data. 

You can do this through `intern` directly or through the management console. We recommend using the managment console for set up if only uploading a single or a few datasets at a time. 

Please view the [API documentation](https://docs.theboss.io/docs/list-collections) for more detailed information!

--
Before uploading data, we first need to determine some information about our new dataset:

**Collection Name:**

This is basically the highest level "directory" of your data. Its just a name-space that you reserve like your lab name, dataset and/or project name, but it must be unique within the BossDB system.

**Coordinate Frame**

Every experiment in bossDB is attached to a coordinate frame. A coordinate frame is not a directory-like object but instead meta-data that specifies the x,y,z voxel extents and size. Coordinate frames are always public and can be used across multiple experiments. Since coordinate frames exist in the experiment level, all channels within the same experiment share the same coordinate frame. This is especially important for aligning image with segmentation or other data derivatives.

Most of the fields for a coordinate frame are pretty self-explanatory but there are a few quirks:

- we heavily recommend that x,y,z starts are all set to 0. Having a non-zero start can complicate downsample and cuboid-alignment.
- It is also recommended that x,y,z stops are cuboid aligned. The bossDB standard cuboid size is 512,512,16 in XYZ. This means that X and Y stops are multiples of 512 while z stop is a multiple of 16.
- Voxel resolution and units do matter for neuroglancer.
- Coordinate frames are cheap. It doesn't create any "data", it just marks what areas in the XYZ spatial domain data does exist. So if you don't know exactly how much data you are going to process, its probably **better to make the coordinate frame larger than you expect**. Once the XYZ values are inputted and submitted, they are difficult to change.

**Experiment Name:**

The experiment name must be unique to the specfic collection. This might be the name for a particular subject (e.g. mouse_1) as the channels within the experiment should all be co-registered data.

**Channel Name:**

The channel name must be unique within the specific experiment. This should indicate what type of data it is (e.g. segmentation, EM)

**Voxel Information:**

You will need to know the voxel size of your dataset, if the data is isotropic or anisotropic, as well as the voxel unit (e.g. nanometers). 

--
### Using the management console to set up a resource

Navigate to the management console website and log in: https://api.bossdb.io/

*Step 1: Collection Name and Description*

Once there, you can click "Manage Resources" and then "Add Collection". A modal will pop up where you can fill in the Collection name and a short description. You can also decide to make the datset public or not.

Once you've created the collection, find your collection name and click the "Details" button to the right of the name. (You might have to filter by the name or scroll through some pages to find the collection you created). 

In the details page you will see a table with the experiments available, which should be empty since the collection was just created. 

Scroll down to collection permissions. Here you should see admin access for the account that created the collection (presumably yours) as well as other admins. You can add read (or write) access to other groups by clicking "Add Permissions" and then inputting the name of the group to add permissions for as well as the type of permission.

*Step 2: Set Up Coordinate Frame*

Before setting up experiments, we need to create the coordinate frame. To create a coordinate frame, navigate back to the "Manage Resources" tab. If you scroll down you will see a list of coordinate frames. You can add one by clicking the "Add Coordinate Frame" button which will open a modal with a form. 

Here you give the coordinate frame a name and description, you set the x, y, and z extents of the data, you set the x, y, z voxel sizes, and you set the voxel unit of measurement.

*Step 3: Experiment Name and information*

Go back to view the Collection Details and click the 'Add Experiment' button.

A modal will pop up with a form to fill out. 

- Add the name and a short description of the experiment.
- Provide the name of the coordinate frame you just created.
- Num hierarchy levels lets bossDB know how many levels of downsample this dataset should have.
- Heirarchy method is either isotropic or anisotropic and it will depend on your dataset voxel resolution
- num time samples is relevent if using timeseries data otherwise it is 1. 
- time step information is only relevant if timeseries data and can be left empty

Similar to collection, you can click the "Details" button on the experiment and scroll down to permissions

*Step 4: Channel Name and information*

Once we've created an experiment and collection, we can finally add channels which actually CONTAIN the volumetric data. To create a channel, go to the experiment details page and click the "Add Channel" button. A modal with several fields should appear prompting you for channel name, type, and other information. 

Note about channel types:

"image" is reserved for 8-bit or 16-bit image data from EM, x-ray, and other modalities. "annotation" type is always 64-bit. 

Base resolution should be 0 in most cases except when you are uploading an already downsampled version of the data. For annotation channels, its help to also specify the source channel if it exists within the same collection. For example, if I have annotation channel of synapse locations based off of image channel "em_chan3" in the same experiment, I would write "em_chan3" as my source chan.

Once you've created the channel, add read/write permissions by click "Details" next to the channel and "Add permissions". 

At this point you are ready to upload data to bossDB!

### Using intern to set up a resource

Using intern we can set up some metadata for the dataset and fill in more information (like descriptions) using the management console: 

- the collection, experiment, and channel names
- the coordinate frame (`extents`) we expect the data to fill (z, y, x order)
- the voxel sizes (`voxel_size`) (z, y, x, order)
- and we indicate that we are creating a new dataset (`create_new=True`)

```python
from intern import array

dataset = array(
    "bossdb://my_collection/my_experiment/my_channel", 
    create_new=True,
    extents=[2048, 4096, 5123],
    voxel_size=[2, 1, 1]
)
```

See the [intern array code](https://github.com/jhuapl-boss/intern/blob/655fcd16e3067766848616ad592cce43d3175656/intern/convenience/array.py#L186-L205) for all input options!

## Uploading data through intern

To upload data through intern your data must be first loaded into python as a numpy array using your favorite method

```
data = np.array(...)

```

Then we point the intern array at our newly created URI:

```python
from intern import array

dataset = array("bossdb://my_collection/my_experiment/my_channel")
```
Then we can upload by indexing the array at our desired extents and setting those indices equal to our data:

```
dataset[0:1,0:512,0:512] = data

```
In this example we have now uploaded one 512x512 image slice to our new channel. 

You can iterate through slices of your data or upload it all at once. 
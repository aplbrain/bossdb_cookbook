# Introduction to the world of connectomics and BossDB

This file should serve as a quick introduction to some of the more common and fundamental concepts in the field of connectomics and how it relates to our goals at BossDB. 


## What is connectomics? Why is it important?


Connectomics is a relatively newly-developed field in the realm of computational neuroscience and big data which focuses on mapping the structural and functional properties of brain tissue and ultimately developing "connectomes", which are full maps of all the connections between neurons in the brain. These connectomes can help medical research understand brain pathologies and can also help AI researchers develop more bio-fidelic machine learning algorithms. 

Connectomics leverages recent advancements in computer science, graph theory, and AI to enable the community to develop the tools and infrastructure to generate connectomes for complex brain structures such as ours (humans). Researchers have mapped the 300 or so neurons in the nervous system of the worm C. elegans. Janelia Research has recently released the largest [synaptic connectome of a portion of a drosophila brain](https://www.janelia.org/project-team/flyem/hemibrain). The IARPA MICrONS project recently released [large scale electron microscopy based reconstructions of cortical circuitry from mouse visual cortex, with corresponding functional imaging data from those same neurons](https://bossdb.org/project/microns-minnie).

## How are connectomes created? What are the underlying neuroscience principles?

In short: Connectomes are usually mapped with electron microscopy (EM), and sometimes with X-ray microtomography, fMRI, and dMRI. Researchers use speciailized machines to process brain tissue into small "slices" and then scan these slices using EM to get volumetric spatial data of the brain. 

To map the connections, humans would have to manually comb through the EM data slices, one by one, and find and label each neuron and its synapses (i.e. axon and dendrite connections). This process is time-consuming and not viable for complex brain structures. Therefore the field has moved to using more automated approaches using computer vision, flood-fill networks, and semi-supervised proofreading. 

## What is BossDB's role in this process?

Our goals at BossDB are to help democratize data access and provide analytical tools to help gain insight to the underlying processes of the brain. We are a team of research scientists and engineers who are passionate about **enabling discovery** by **reducing the barriers** to large-scale exploration of cutting-edge neuroscience datasets. We've developed a system to help scalably and securely store, share, and process data in the cloud, called the Brain Observatory Storage Service & Database (BossDB).

The Brain Observatory Storage Service & Database (BossDB) is a scalable cloud-native data ecosystem for storing, accessing, and processing multidimensional and volumetric neuroscience datasets. The ecosystem makes use of Amazon Web Services capabilities that ensure highly available and highly scalable endpoints, data caching and load balancing, and durable multitier data storage. A well-documented interface and API support a suite of tools and software development kit (SDK) to allow a user to easily ingest, validate, visualize, and query neuroscience data from any data generator, making it possible for scientists to discover and share insights on massive datasets. 

Check out https://bossdb.org for more info and to see the public datasets we currently host.

## Exciting Connectomics Datasets on BossDB


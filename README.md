# An arXiv Recommender System

## Directory Structure

```
.
├── Docker/
├── README.md
├── data/
├── notebooks/
├── postgres.json
├── vectors/
└── word_clouds/
```


## Directory Outline
For more details on the files within the directories, there is a `README.md` file within each subdirectory.

* *Docker*
> In this directory you will find a Dockerfile that defines a Docker image in which you should be able to run all of the notebooks and other code within this repository.
> Please keep the following caveats in mind
    1. There are large files that you will download by using this Dockerfile, in particular a plain text version of the tokenized abstracts of every article on __arXiv__. If you don't want to download the vectors and various files associated with the output of GloVe, you can remove the final run command from the Dockerfile.
    1. The current implementation for fitting GloVe vectors on a corpus uses the [Stanford NLP C code](https://nlp.stanford.edu/projects/glove/). This process is intensive and can take up substantial memory and CPU resources.
* README.md
> You're looking at it.

* *data*
> Where raw data obtained form __arXiv__ is stored. These include various `XML`, `JSON` and log files from the metadata harvesting process.


* *notebooks*
> The Jupyter notebooks, and some other files, which make up the bulk of this project.

* *postgres.json*
> A `JSON` file which contains credentials for a user on my `postgreSQL` database. Currently this user has select only permissions so cannot be used to the various database updating processes that some of these notebooks contain.

* *vectors*
> Contains the files associate with the GloVe word embedding trained on the __arXiv__ corpus.

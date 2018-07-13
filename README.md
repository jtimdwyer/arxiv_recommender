# An arXiv Recommender System

## Directory Structure

```
.
├── Docker
├── Final_Report.md
├── README.md
├── data
├── notebooks
├── postgres.json
├── vectors
└── word_clouds
```


## Project Outline

This project is a recommender system for articles on the pre-print repository [__arXiv__](https://arxiv.org). There are more than 1.4 million articles on __arXiv__ and it is used by physicists, mathematicians, computer scientists and others to allow access to their papers before they are formally reviewed and published in a journal. Some papers on __arXiv__ are never published. There are hundreds of papers submitted to __arXiv__ every day.

![][submissions]

[submissions]: notebooks/02_Data_Analysis_And_Processing/submissions.png

When Grigori Perelman won (and declined) the Fields Medal in 2006, arguably the most prestigious prize in mathematics, the work for which he won the award was never published in a journal. It was posted on __arXiv__.

 From the Telegraph:
>["If anybody is interested in my way of solving the problem, it's all there - let them go and read about it," said Dr Perelman. "I have published all my calculations. This is what I can offer the public."](https://www.telegraph.co.uk/news/1526782/Worlds-top-maths-genius-jobless-and-living-with-mother.html)

In the modern research world, pre-print repositories like __arXiv__ are a first-class citizen in the distribution of research results.

In this repository I have built an system which, based on the abstract of an article on __arXiv__, tries to recommend articles that might also be of interest to the user. This system uses a `word embedding` vector, specifically the [GloVe word vector](https://nlp.stanford.edu/projects/glove/) developed by at the Natural language processing group at Stanford. GloVe word embedding vector that, like `word2vec` or `fastText` tries to capture not term frequencies (relative or absolute), but semantic relations between words. For a more in-depth explanation of how GloVe works, you can read the paper [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf). Ironically enough, this paper doesn't seem to be on __arXiv__. There is also a briefer outline of the process in the GloVe notebook.



## Directory Outline
For more details on the files within the directories, there is a `README.md` file within each subdirectory.

* *[Docker](Docker)*

> In this directory you will find a Dockerfile that defines a Docker image in which you should be able to run all of the notebooks and other code within this repository.

__Please keep the following caveats in mind:__

1. There are large files that you will download by using this Dockerfile, in particular a plain text version of the tokenized abstracts of every article on __arXiv__. If you don't want to download the vectors and various files associated with the output of GloVe, you can remove the final run command from the Dockerfile.

1. The current implementation for fitting GloVe vectors on a corpus uses the [Stanford NLP C code](https://nlp.stanford.edu/projects/glove/). This process is intensive and can take up substantial memory and CPU resources.


* *[Final_Report.md](Final_Report.md)*

> A techinical summary of the project. Includes the main text of the `README.md` files in the notebook directories.


* *README.md*

> You're looking at it.

* *data*

> Where raw data obtained form __arXiv__ is stored. These include various `XML`, `JSON` and log files from the metadata harvesting process. Not present in the Github repository.

* *[notebooks](notebooks)*

> Mostly Jupyter notebooks, which make up the bulk of this project.

* *[postgres.json](postgres.json)*

> A `JSON` file which contains credentials for a user on my `postgreSQL` database. Currently this user has select only permissions so cannot be used to the various database updating processes that some of these notebooks contain.

* *vectors*

> Contains the files associate with the GloVe word embedding trained on the __arXiv__ corpus. Not present in the Github repository.

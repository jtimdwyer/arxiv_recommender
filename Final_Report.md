# Final report
> This summary contains the summaries in the `README.md` files for the three notebook directories in this project, as well as a final report at the end. The first three subsections are the same summaries as the ones in those directories. 

## Data From Arxiv

> __arXiv__ has an API for obtaining the metadata of every article they possess. This API adheres to the Open Archives Initiative syntax which means it has a standardized query structure. More information on this __arXiv__ API can be found [here](https://arxiv.org/help/oa/index). I used this API to collect information, including the title, abstracts and a unique identifier for each article in __arXiv__ (through June 19 2018). The format of the unique identifier has changed over the lifetime of __arXiv__, but it can be used to create a URL for the landing page for a given article.

## Data Analysis and Processing

> This directory contains notebooks which primarily deal with examining and processing the data obtained from __arXiv__. The primary piece of information we are using to describe an article is its abstract. The abstract of articles on __arXiv__ often are not meant to be read as simple plain text but to be compiled by some `LaTeX` compiler into a something with rendered mathematical notation. This means that we do not have simple human readable text, but something more like a code for a program. The [first notebook](./notebooks/02_Data_Analysis_And_Processing/01_D01_Processing_Latex.ipynb) in this directory does performs some processing using `pypandoc` (a python wrapper for the `pandoc` program) and `detex` (a tool for stripping `LaTeX` commands from text).  

> In the [second notebook](./notebooks/02_Data_Analysis_And_Processing/02_Exploring_Processed_LaTeX.ipynb) we indulge in some exploratory data analysis. First we show the results from the `pypandoc` and `detex` programs (i.e. determine the number of abstracts which have ill-formed `LaTeX`) Next we consider the rate of growth of submissions to __arXiV__. Finally, to get some kind of visual sense of the subject matter, we make some word clouds for the different general categories of articles.

> In the third and [final notebook](./notebooks/02_Data_Analysis_And_Processing/03_GloVe_Word_Embeddings.ipynb), we finally actually construct a numerical representation of the articles. We do this so that we can work with something that we can actually mathematically manipulate. Our choice of GloVe vectors is, while not arbitrary, certainly not a condemnation of any other word embedding models. I would be very curious as to the results of similar systems using `word2vec` or `fastTest`. For concreteness I will state this, to each article, GloVe assigns a vector (a list of numbers) which GloVe has decided, according to its own internal logic, represents that article. An important point here is that this process is not, at least not in any obvious way, reversible. We have lost some, a lot really, information about the article by doing this. The hope is that what we've lost is noise and what we've retained is good signal.

## Recommender Systems

> Vectors are one of the nicest mathematical objects there are. After we've assigned a vector to each article, we want to leverage the vector to say something about the articles. I think that it would be uncontroversial to say that parallel vectors are similar to one another while orthogonal vectors very dissimilar. A concrete way to measure whether vectors are parallel or orthogonal is by considering their `dot product`. This is precisely how the so-called `cosine similarity` method of comparison works, and it's how we choose to make our recommendations.

> To be more explicit, the code the [notebook](./notebooks/03_Recommender_Systems/01_Similarity) in this directory defines a process for the following list of tasks

1. Create the matrix X, with rows corresponding to the articles in __arXiv__ and 300 columns (each row is the vector for that article).

1. Computing the similarity between a given article and all other articles, using the matrix X.

1. Sorting the resultant numbers so that we can keep those which score the highest. These articles with the highest scores will then be the recommended articles given to the user.

> With this process in hand, I created a Flask app that will, upon request, look up an article in my postgres database and try to deliver recommendations. If there are none in the database it's because the preprocessing script hasn't gotten to that one yet. Since this is likely the case, for now at least, I'm keeping the matrix X in memory so that these requests can be handled. Once the database is updated with the newly requested article we deliver the recommendations to the user. Right now this is not implemented as a user-facing website but just delivers a `JSON` file with the information.

## Summary

> In manually inspecting some of the results I noticed some truly odd results. I chose a sample of 1000 articles and plotted their best similarities. and got such and such

## Future Evaluation

> I'm planning to send this out to some friends to evaluate.

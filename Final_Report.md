# Final report
> This summary contains the summaries in the `README.md` files for the three notebook directories in this project, as well as a final report at the end. The first three subsections are the same summaries as the ones in those directories. Some of the text of the Summary section is repeated from the [01_Similarity_of_Articles](notebooks/03_Recommender_Systems/01_Similarity_of_Articles.ipynb) notebook.

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

In evaluating the performance of the recommndations I tried three sample articles to generate requests for.

One was chosen at random, one is an article I wrote, and the third is a paper that I had trouble finding good external material for when I was graduate school.

### The random article

Suppose someone wanted a recommendation for similar material to a physics article: [Bounds on the Probability of Success of Postselected Non-linear Sign Shifts Implemented with Linear Optics](https://arxiv.org/abs/quant-ph/0307015).
I used the system I'd built to generate the following recommendations.

1. [Feed-forward and its role in conditional linear optical quantum dynamics](https://arxiv.org/abs/quant-ph/0509075)
1. [An efficient quantum filter for multiphoton states](https://arxiv.org/abs/quant-ph/0406008)
1. [Minimum-energy pulses for quantum logic cannot be shared](https://arxiv.org/abs/quant-ph/0611137)
1. [Linear optics implementation of general two-photon projective measurement](https://arxiv.org/abs/quant-ph/0207112)
1. [Optimal Signal-to-Quantum Noise Ratio for Nonclassical Number States](https://arxiv.org/abs/quant-ph/9712020)

A quick read of the abstracts of these articles tells me that they're all related to optics and and photon gates. I would say these recommendations are good, and that these paper are certainly similar, but I can't really judge how perfectly aligned they are.

### My paper

We do the same thing we did above, but with a paper I wrote with my former PhD thesis advisor Sergi Elizalde: [Wilf equivalence relations for consecutive patterns](https://arxiv.org/abs/1801.08262)

The GloVe vector based recommender system generated the following top recommended articles.

1. [On Pattern Avoiding Alternating Permutations](https://arxiv.org/abs/1212.2697)
1. [Egge triples and unbalanced Wilf-equivalence](https://arxiv.org/abs/1410.0230)
1. [The Length of the Longest Common Subsequence of Two Independent Mallows Permutations](https://arxiv.org/abs/1611.03840)
1. [Quadrant marked mesh patterns in 123-avoiding permutations](https://arxiv.org/abs/1705.00164)
1. [Avoidance of Partially Ordered Generalized Patterns of the form  k-σ-k](https://arxiv.org/abs/0805.1872)

I can, without qualification, say that these are good recommendations. All of these papers absolutely are a part of a topic in combinatorial mathematics called __permutation patterns__. This is a very specialized sub-field of mathematics, and the recommender is definitely staying within this sub-field.


### A non-example

No recommender system is perfect, sometimes recommendations just don't make sense. Sometimes even if they do make sense, they're still bad. I was curious about what the system would recommend for the following article: [The Goulden-Jackson Cluster Method: Extensions, Applications and Implementations](https://arxiv.org/abs/math/9806036). This paper gave me a lot of trouble when I was in graduate school and I spent a lot of time looking for articles with similar content. I genuinely had a hard time at it so I really wanted to see what the system would say. The system generated the following recommendations:

1. [The Number of Same-Sex Marriages in a Perfectly Bisexual Population is Asymptotically Normal](https://arxiv.org/abs/1106.5646)
1. [Schwerdtfeger-Fillmore-Springer-Cnops Construction Implemented in GiNaC](https://arxiv.org/abs/cs/0512073)
1. [Balls in Boxes: Variations on a Theme of Warren Ewens and Herbert Wilf](https://arxiv.org/abs/1106.5531)
1. [Automatic Enumeration of Generalized Menage Numbers](https://arxiv.org/abs/1401.1089)
1. [The Fedosov *-product in Mathematica](https://arxiv.org/abs/0801.3194)

Looking at these papers, these are not very good recommendations. But it's easy to figure out what signal the system is picking up on as a similarity between the abstracts just by looking at them. Looking at the abstracts of these papers nothing about the content that indicates a strong relationship between these articles and the the article we're finding recommendations for. There is however on striking similarity in all of these abstracts. The all contain the phrase `this http url` in reference to a link. I have no idea if this is some old school way of describing links, but this idiom really seems to have boosted the scores between these articles.

## Future Evaluation



> I'm planning to send this out to some friends to evaluate.

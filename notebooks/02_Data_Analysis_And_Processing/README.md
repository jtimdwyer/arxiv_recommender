# Data Analysis and Processing


> This directory contains notebooks which primarily deal with examining and processing the data obtained from __arXiv__. The primary piece of information we are using to describe an article is its abstract. The abstract of articles on __arXiv__ often are not meant to be read as simple plain text but to be compiled by some `LaTeX` compiler into a something with rendered mathematical notation. This means that we do not have simple human readable text, but something more like a code for a program. The [first notebook](01_Processing_Latex.ipynb) in this directory does performs some processing using `pypandoc` (a python wrapper for the `pandoc` program) and `opendetex` (a tool for stripping `LaTeX` commands from text).  

> In the [second notebook](02_Exploring_Processed_LaTeX.ipynb) we indulge in some exploratory data analysis. First we show the results from the `pypandoc` and `opendetex` programs (i.e. determine the number of abstracts which have ill-formed `LaTeX`) Next we consider the rate of growth of submissions to __arXiV__. Finally, to get some kind of visual sense of the subject matter, we make some word clouds for the different general categories of articles.

> In the third and [final notebook](03_GloVe_Word_Embeddings.ipynb), we finally actually construct a numerical representation of the articles. We do this so that we can work with something that we can actually mathematically manipulate. Our choice of GloVe vectors is, while not arbitrary, certainly not a condemnation of any other word embedding models. I would be very curious as to the results of similar systems using `word2vec` or `fastTest`.





## Directory Structure

```
.
├── 01_Processing_Latex.ipynb
├── 02_Exploring_Processed_LaTeX.ipynb
├── 03_GloVe_Word_Embeddings.ipynb
├── glove.log
├── glove_arxiv.sh
└── sqlalchemy_arxiv.py
```

## Summary of contents

* *01_Processing_Latex.ipynb*

> The articles we see on __arXiv__ are (almost always) PDFs. But typically when one submits an article to __arXiv__, it's submitted as a `LaTeX` file, and then compiled into the PDF on the other end. For our purposes this means that abstracts we're getting from __arXiv__ are snippets of `LaTeX`. A non-trivial proportion, about 6% of these abstracts are not well-formed `LaTeX`. In this notebook I investigated this phenomenon.

* *02_Exploring_Processed_LaTeX.ipynb*

> This notebook is concerned with three different tasks. First I determine the failure rate for the `LaTeX`, i.e. the proportion of articles which have abstracts with improper `LaTeX`. Then I examine the submission rate to __arXiv__ over time, which, as can be seen in the plot below, has grown considerably. Lastly, I create some word clouds for different categories of article as defined by __arXiv__.


* *03_GloVe_Word_Embeddings.ipynb*

> In this notebook I used some regular expressions to transform the abstracts of articles into `tokens`. In natural language parlance a `token` is a typically a word, but really it's just the way that we break a whole document of text into some discrete units. Typically words are their own tokens, but sometimes we might want to combine multiple words into one token. Specifically, since we're dealing with a highly specialized style of writing with highly non-natural syntax (`LaTeX` is code!), I did not want to rely on out of the box tokenizers.

> Once the articles were tokenized, I used the [Stanford GloVe library](https://nlp.stanford.edu/pubs/glove.pdf) to compute word vectors for the tokens. After those have been computed we can compute a vector associated to each article by simply taking the abstract, looking at the words in the abstract, and summing up their corresponding vectors. This vector is now the vector representation of the article. For all intents and purposes, as far as the system for making recommendations is concerned, this vector is the article.

* *glove_arxiv.sh*

>  A Bash wrapper script for running the GloVe programs.

* *glove.log*

> A log file of the output of `glove_arxiv.sh`.

* *sqlalchemy_arxiv.py*

> A convenience module for interacting with the Postgres server where the information is stored.

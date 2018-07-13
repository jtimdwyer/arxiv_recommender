# Recommender Systems

> Vectors are one of the nicest mathematical objects there are. After we've assigned a vector to each article, we want to leverage the vector to say something about the articles. I think that it would be uncontroversial to say that parallel vectors are similar to one another while orthogonal vectors very dissimilar. A concrete way to measure whether vectors are parallel or orthogonal is by considering their `dot product`. This is precisely how the so-called `cosine similarity` method of comparison works, and it's how we choose to make our recommendations.

> To be more explicit, the code the [notebook](./notebooks/03_Recommender_Systems/01_Similarity) in this directory defines a process for the following list of tasks

1. Create the matrix X, with rows corresponding to the articles in __arXiv__ and 300 columns (each row is the vector for that article).

1. Computing the similarity between a given article and all other articles, using the matrix X.

1. Sorting the resultant numbers so that we can keep those which score the highest. These articles with the highest scores will then be the recommended articles given to the user.

> With this process in hand, I created a Flask app that will, upon request, look up an article in my postgres database and try to deliver recommendations. If there are none in the database it's because the preprocessing script hasn't gotten to that one yet. Since this is likely the case, for now at least, I'm keeping the matrix X in memory so that these requests can be handled. Once the database is updated with the newly requested article we deliver the recommendations to the user. Right now this is not implemented as a user-facing website but just delivers a `JSON` file with the information.

## Directory Structure

```
.
├── 01_Similarity_of_Articles.ipynb
├── 02_Flask.md
├── README.md
├── app.py
├── flask_utils.py
├── preprocessing.py
└── sqlalchemy_arxiv.py
```



## Summary of contents


* *01_Similarity_of_Articles.ipynb*

> Processing the article's (actually their associated vectors) so that we can compare them. We consider the similarity between two vectors to be measured by the angle they make. The easiest way to think about this is that parallel vectors are incredibly similar (they have no angle between them). The angle between the two vectors is measured implicitly by computing their `dot product`, which can be done very efficiently and quickly using the numpy computational library.

* *02_Flask.md*

> An overview of how the Flask app functions including explanations of the code in [app.py](app.py).

* *app.py*

> The main process for the Flask app. This program defines how Flask will handle the user requests and what processes need to be run in response to those requests.  

* *flask_utils.py*

> This module defines certain helper functions for the Flask app. They're moved out of [app.py](app.py) to make that file more readable.

* *preprocessing.py*

> This program will, over time, process all the articles we have and compute the recommendations for them. Once this is done, we can modify the Flask app so that it doesn't have to store the whole vector array in memory to do online computation.

* *sqlalchemy_arxiv.py*

> A convenience module for interacting with the Postgres server where the information is stored.

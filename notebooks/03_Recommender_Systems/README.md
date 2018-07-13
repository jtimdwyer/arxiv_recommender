# Recommender Systems

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

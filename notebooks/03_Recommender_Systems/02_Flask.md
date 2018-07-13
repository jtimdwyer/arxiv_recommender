# Flask
Flask is a Python web framework. We are using it to take requests from users for recomendations and then render the response to them. In the [previous notebook in the current directory](./01_Similarity_of_Articles), we showed how we are actually deciding what papers to recommend. For us Flask's purpose is two-fold:

1. Receive input from a user on a webpage, i.e. the id for a paper on __arXiv__.

1. Deliver a response to the user, titles and abstracts of papers we recommend as well as a link to the papers on __arXiv__.

I'm choosing to present this material in this markdown file, rather than a notebook. This is due to the fact that Flask's recent version upgrade has some compatibility issue with running in a Jupyter notebook. We'll reproduce the code in the [app.py](app.py) file here with some more explanation.

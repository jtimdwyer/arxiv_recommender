# Flask
Flask is a Python web framework. We are using it to take requests from users for recomendations and then render the response to them. In the [previous notebook in the current directory](./01_Similarity_of_Articles), we showed how we are actually deciding what papers to recommend. For us Flask's purpose is two-fold:

1. Receive input from a user on a webpage, i.e. the id for a paper on __arXiv__.

1. Deliver a response to the user, titles and abstracts of papers we recommend as well as a link to the papers on __arXiv__.

I'm choosing to present this material in this markdown file, rather than a notebook. This is due to the fact that Flask's recent version upgrade has some compatibility issue with running in a Jupyter notebook. We'll reproduce the code in the [app.py](app.py) file here with some more explanation.
```python
from flask import Flask, jsonify, request
from sqlalchemy_arxiv import Session, articles_similar, articles_raw

from flask_utils import vectors, all_ids\
request_recs, send_to_server,\
 compute_recs_paper_id, compute_recs_batch
```

The `flask` imports are for actually using the flask app to manage the API. The `sqlalchemy_arxiv` imports are convenience functions and classes, they define how we are interacting with the `Postgres` database. The `flask_utils` imports are the functions and objects needed to interact with the server and perform online computation of recommendations.

```python
app = Flask(__name__)
```
This snippet instantiates the flask app object.


```python
@app.route('/')
def home():
    arxiv_id = request.args.get('arxiv_id')
    if arxiv_id:
        #look up the article in our recs table
        if arxiv_id in all_ids:
            session = Session()
            db_entry = (request_recs(id_request=arxiv_id, table_class_recs=articles_similar, session=session)
            session.close()
        else:
            return "We don't actually have this one :("

        #if we've got it fro4m the db, go ahead and return it.
        if db_entry:
            return jsonify(db_entry)

        #otherwise, we'll compute the answer and store it
        else:
            recs = compute_recs_paper_id(arxiv_id, all_ids, vectors)
            session = Session()
            send_to_server(recs=recs, table_class_recs=articles_similar, session=session)
            session.close()
            return jsonify(recs)
    else:
        return "You need to tell us what article you want to look at."
```

This larger block does two things really. The decorator `app.route('/')` modifies the function `home` so that `home` acts as the response function to an http request. The function then looks for an `arxiv_id` argument and checks to see if we have recommendations for it in the database. If we don't have any recommendations for it we do one of two things.

First we check if it's even a article we have any information on! If the article is too new, then we don't have any information it and can't make recommendations. If we do have information for that article, but no recommendations, we compute the recommendation and update the database accordingly.


```python
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
```

This snippet actually runs the app when the file `app.py` is run. To get this to actually run (say if you used the dockerfile in this repo to build the environment), you could do the following commands, from the current directory (and within the docker container), in a `bash` shell

```bash
$ export FLASK_APP=app.py
$ python -m flask run -p 5000 -h 0.0.0.0
```

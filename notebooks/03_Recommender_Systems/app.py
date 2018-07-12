from flask import Flask, jsonify, request
from sqlalchemy_arxiv import Session, articles_similar, articles_raw

from flask_utils import vectors, all_ids\
request_recs, send_to_server,\
 compute_recs_paper_id, compute_recs_batch


app = Flask(__name__)
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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

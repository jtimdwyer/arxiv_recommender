from flask import Flask, jsonify, request, render_template
from sqlalchemy_arxiv import Session, articles_similar
from flask_utils import vectors, ids, request_recs, send_to_server, compute_recs_paper_id

app = Flask(__name__)
@app.route('/')
def home():
    arxiv_id = request.args.get('arxiv_id')    
    if arxiv_id:
        #look up the article in our recs table
        session = Session()
        db_entry = request_recs(arxiv_id, table_class=articles_similar, session=session)
        session.close()

        #if we've got it, go ahead and return it.
        if db_entry:
            return jsonify(db_entry)
        
        #otherwise, we'll compute the answer and store it
        else:
            recs = compute_recs_paper_id(arxiv_id, ids, vectors)
            session = Session()
            send_to_server(arxiv_id, recs, table_class=articles_similar, session=session)
            session.close()
            return jsonify(recs)
    else:
        return "You need to tell us what article you want to look at."
        

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
            

from flask import Flask, jsonify, request, render_template

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
        
        
        #otherwise, we'll look it up and give a message.
        #the working set 
        else:
            
            if arxiv_id not in working_set:
                working_set.add(arxiv_id)
                p = Process(target=update_db, args=(arxiv_id, working_set, Session, all_ids_list))
                p.start()
                return "Sorry! We're working on it, try again in a few minutes."
            else:
                return "We're working on it!!!! Wait a few minutes."
            
    else:
        return "You need to tell us what article you want to look at."
        

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
            

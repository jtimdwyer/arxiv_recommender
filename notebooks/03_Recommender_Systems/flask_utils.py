import numpy as np
import json
import pickle


with open('../../vectors/vectors.pkl', 'rb') as vec_pkl:
    vectors = pickle.load(vec_pkl)
    
with open('../../vectors/id.json', 'r') as ids_json:
    ids = json.load(ids_json)

def score(vectors, all_ids, id_low, id_high):
    """
    Outputs an array, scores. The columns of scores 
    are correspond to the slice of article_ids 
    
    all_id[id_low:id_high]
    
    The rows are indexed by all_ids.
    
    The value in column C and row R is the 
    similarity between the articles all_ids[R]
    and all_ids[id_low+C].
    """
    mask = [id_low <= index < id_high for index, _ in enumerate(all_ids)]
    rows = vectors[mask]
    scores = vectors @ rows.T
    return scores

def sort_scores(scores, all_ids, cur_ids):
    """
    Returns a dictionary of lists. The keys are the ids 
    of articles we're currently evaluating.
    
    The lists contain tuples of scores and ids. The 
    score is the similarity score between the current article
    and the other component of the tuple.
    """
    recs = {}
    for col_num, col in enumerate(scores.T):
        article_id = cur_ids[col_num]
        recs[article_id] = list(zip(col, ids))
        recs[article_id].sort(key=lambda x: x[0], reverse=True)
        recs[article_id] = recs[article_id][:51]
    return recs


def compute_recs_paper_id(arxiv_id, ids, vectors):
    """
    Takes the list of id_number in question, 
    the list ids, and array of vectors
    and returns a dictionary whose key is the arxiv_id
    and the only value is the 
    """
    
    id_num = ids.index(arxiv_id)
    scored = score(vectors, ids, id_num, id_num+1)
    recs = sort_scores(scored, ids, ids[id_num:id_num+1])
    return recs


def send_to_server(arxiv_id, recs, table_class, session):
    """
    Sends computed recommendations to the the database
    """
    new_recs = [{'id':key,'recs':value} for key, value in recs.items()]
    new_recs = [table_class(**args) for args in new_recs]
    session.add_all(new_recs)
    session.commit()

def request_recs(id_request, table_class, session):
    """
    Retrieves computed recommendations to the the database
    """
    query = session.query(table_class).filter(table_class.id==id_request)
    records = query.all()
    if records:
        return records[0].recs
    
    
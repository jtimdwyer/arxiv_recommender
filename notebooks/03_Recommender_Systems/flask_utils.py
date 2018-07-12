import numpy as np
import json
import pickle


with open('../../vectors/vectors.pkl', 'rb') as vec_pkl:
    vectors = pickle.load(vec_pkl)

with open('../../vectors/id.json', 'r') as ids_json:
    all_ids = json.load(ids_json)


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
        recs[article_id] = list(zip(col, all_ids))
        recs[article_id].sort(key=lambda x: x[0], reverse=True)
        recs[article_id] = recs[article_id][:51]
    return recs


def compute_recs_batch(all_ids, vectors, low, high):
    """
    Computes the recommendations for the articles in
    the list all_ids[low:high].
    Returns a dictionary that can be fed into
    send_to_server for upload to the postgres database.
    """
    scored = score(vectors, all_ids, low, high)
    recs = sort_scores(scored, all_ids, all_ids[low:high])
    return recs


def compute_recs_paper_id(arxiv_id, all_ids, vectors):
    """
    Takes the list of id_number in question,
    the list of all ids, and array of vectors
    and returns a dictionary whose key is the arxiv_id
    and values a list of the recommended articles and scores
    """

    id_num = ids.index(arxiv_id)
    scored = score(vectors, all_ids, id_num, id_num+1)
    recs = sort_scores(scored, all_ids, all_ids[id_num:id_num+1])
    return recs


def send_to_server(recs, table_class_recs, session):
    """
    Sends computed recommendations to the the database
    """
    new_recs = [{'id':key,'recs':value} for key, value in recs.items()]
    new_recs = [table_class_recs(**args) for args in new_recs]
    for new in new_recs:
        session.merge(new)
    session.commit()

def request_recs(id_request, table_class_recs, session):
    """
    Retrieves computed recommendations from the database
    """
    query = (session
             .query(table_class_recs)
             .filter(table_class_recs.id==id_request)
            )
    records = query.all()
    if records:
        return records

def recs_list(records, table_class_info, session):
    """
    Takes the recomendations from request_recs,
    obtains the titles and abstracts of those papers.

    Outputs a list of tuples. Each tuple contains the
    id, title, abstract and score of a recommended article.
    """

    rec_ids = [rec[1] for rec in records[0].recs[1:]]
    recs_scores = [rec[0] for rec in records[0].recs[1:]]

    query = (session.query(table_class_info)
             .filter(table_class_info.id.in_(rec_ids))
            )

    article_info = [(a.id, a.title, a.abstract) for a in query.all()]
    article_info.sort(key=lambda article: rec_ids.index(article[0]))
    article_info = [(*info, score) for info, score  in zip(article_info, recs_scores)]
    return article_info

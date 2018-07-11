# This script is meant to process all of the arxiv ids
# into the postgres database
# Keeps a list 

from sqlalchemy_arxiv import Session, articles_similar
from flask_utils import vectors, all_ids, compute_recs_batch, send_to_server
from itertools import count

# You can pass an argument to this in the command line
# to specify the batch size. 
# In case you don't just default to 100

import sys
if len(sys.argv) == 1:
    my_steps = 100
else:
    my_steps = sys.argv[1]
    

def preprocess_recs(step_size=my_steps,
                    all_ids=all_ids,
                    Session=None,
                    table_class=articles_similar,
                   ):
    
    low_iter = count(start=0, step=step_size)
    high_iter = count(start=step_size, step=step_size)
    
    with open('./ids.log', 'w') as log_file:
        for low, high in zip(low_iter, high_iter):
            recs = compute_recs_batch(all_ids, low, high)
            session = Session()
            send_to_server(recs=recs, table_class=articles_similar, session=session)
            session.close()
            log_file.write(','.join(all_ids[low:high]))

if __name__ == "__main__":
        preprocess_recs(Session=Session)
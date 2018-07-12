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
                    Session=Session,
                    table_class=articles_similar,
                    vectors=vectors,
                    all_ids=all_ids,
                   ):

    low_iter = count(start=0, step=step_size)
    high_iter = count(start=step_size, step=step_size)

    for low, high in zip(low_iter, high_iter):
        # this if else is just checking if
        # we are actually still looking at
        # any ids.
        if all_ids[low:high]:
            recs = compute_recs_batch(all_ids, vectors, low, high)
            session = Session()
            send_to_server(recs=recs, table_class_recs=articles_similar, session=session)
            session.close()
        else:
            break

        with open('./ids.log', 'a') as log_file:
            log_file.write(','.join(all_ids[low:high]) + '\n')

if __name__ == "__main__":
        preprocess_recs()

# An arXiv Recommender System

## File Structure

```
.
├── data
│   ├── json
│   ├── oai_logs
│   └── xml
└── notebooks
    ├── 01_Data_From_arXiv
    ├── 02_Data_Analysis
    ├── 03_Modeling
    └── 04_Recommender_Systems
```


## Outline
In this repository, I build a content based recommender system for articles on the pre-print repository [__arXiv__](arxiv.org) usign their Open Archive Initiative (OAI) API. To this end I performed the following tasks



## Collecting the Data
1. Collected information about the individual papers on __arXiv__, and putting the following information into a PostgreSQL database

| `id`  | `created` | `setspec` | `title` | `abstract` |
| -- | -- | -- | -- | -- |
| 1609.01476 | 2016-09-06 | math | Can decay be ascribed to classical noise? | No. |

### Data Dictionary

`id`: The internal __arXiv__ id of the paper. The homepage of the paper can be found at `arxiv.org/abs/id`. For example the paper above can be found at `arxiv.org/abs/1609.01476`

`created`: The date the paper was originally submitted to __arXiv__.

`setspec`: This is a strange piece of information. The __arXiv__ OAI API categorizes papers with the `setspec` label, but these do not always match the __arXiv__ category. For example, the paper above is listed under the category `Quantum Physics (quant-ph); Mathematical Physics (math-ph)`.

`title`: The title of the paper.

`abstract`: A brief (though not usually as brief as the one above) summary of the paper.

## Processing the Data
2. Use spaCy models to obtain word embeddings on the abstracts and titles for implementing a cosine-similary recommender system. Before this I have to create some annotated examples of $\LaTeX$ code so that spaCy can try to make sense of it. I could have done this as a preprocessing step, but there is a significant proportion of the text has LaTeX that cannot be parsed by tools like `pandoc`


Caveats: I'm currently doing the spaCy work and the notebooks in `02_Data_Analysis` are kind of a mess right now. The notebooks in `01_Data_From_arXiv` are fairly coherent but need editing. 

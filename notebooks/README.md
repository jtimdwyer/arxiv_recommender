# Notebooks Directory

This directory contains the main work of this project, mostly in Jupyter notebooks, but also a some python and  bash scripts.

## Directory Structure

```
.
├── 01_Data_From_arXiv
├── 02_Data_Analysis_And_Processing
├── 03_Recommender_Systems
└── README.md
```


Outline

* *[01_Data_From_arXiv](./01_Data_From_arXiv)*

> This directory contains the code used to gather the information about articles on __arXiv__ from their API, as well as the processing and transferring of this data to a Postgres database.

* *[02_Data_Analysis_And_Processing](./02_Data_Analysis_And_Processing)*

> This directory contains notebooks and a scripts pertaining to data analysis and processing, specifically important considering the specialized nature of the LaTeX in the text being processed
This directory also contains the scripts for transforming the text into GloVe vectors which will be used to comparing articles.

* *[03_Recommender_Systems](./03_Recommender_Systems)*

> This directly contains the notebooks which are used to determine the recommendations for articles as well as the code for a flask app which can serve up these recommendations as a JSON file.

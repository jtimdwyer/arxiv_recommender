# Data Collection

__arXiv__ has an API for obtaining the metadata of every article they possess. This API adheres to the Open Archives Initiative syntax which means it has a standardized query structure. More information on this __arXiv__ API can be found [here](https://arxiv.org/help/oa/index). I used this API to collect information, including the title, abstracts and a unique identifier for each article in __arXiv__ (through June 19 2018). The format of the unique identifier has changed over the lifetime of __arXiv__, but it can be used to create a URL for the landing page for a given article.




## Directory Structure
```
.
├── 01_Obtain_XML.ipynb
├── 02_XML_to_JSON.ipynb
├── 03_Update_Local_Data.ipynb
├── 04_Migrate_Postgres.ipynb
└── README.md
```

## Summary of each Notebook
* *01_Obtain_XML*
> Using the `requests` module, obtained the `XML` files containgn the metadata on articles on __arXiv__.
* *02_XML_to_JSON*
> Using the `lxml` library  to traverse the `XML` trees of the information from __arXiv__, transformed the results of the previous notebook into `JSON` files.
* *03_Update_Local_Data*
> Again using the `requests` module can be used to update my copy of the database by getting information about newer papers from __arXiv__.
* *04_Migrate_Postgres*
> Used `SQLAlechemy` to create a table on a `Postgres` server to store the information from __arXiv__. In future notebooks, these interactions with the database are shifted to external modules and imported to avoid too much repetition.

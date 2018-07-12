# Data Files


## Directory Structure

```
.
├── README.md
├── harvest_info.txt
├── json/
├── oai_logs/
└── xml/
```
## Directory Outline

* `harvest_info.txt`
> A plain text file that records the dates on which our copy of the __arXiv__ data was updated. The main purpose of this file is to allow updates to request only those articles that have been submitted since the last time we updated our copy.

* `json/`
> A directory which contains the `JSON` files of the __arXiv__ metadata. Each file corresponds to a response from the __arXiv__ OAI API.

* `oai_logs/`
> Simple log files that record the process of updating our copy of the database. Used to correct errors in the event of network (or other) failure during updates.

* `xml/`
> `XML` files provided by the __arXiv__ OAI API.

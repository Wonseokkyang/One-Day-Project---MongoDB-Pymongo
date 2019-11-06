# One-Day-Project---MongoDB-Pymongo
A one day project learning to work with a document style database (MongoDB) including DB population and DB queries and learning python for the first time!

Project goals:
- Build a database to model HetioNet 
- Given disease name or disease DOID, find in a single query:
  + Name/DOID
  + Drug/compound names that treat or palliate the disease
  + Gene names that cause the disease
  + Disease localization

![alt text](https://github.com/Wonseokkyang/One-Day-Project---MongoDB-Pymongo/blob/master/graph.jpg)


Data aquired from HetioNet.
- <file> `nodes.tsv`
  -  TSV file of database nodes; Disesases, Genes, Anatomy, Compound.
- <file> `edges.tsv`
  -  TSV file of relationships between nodes; Up regulates, down regulates, associates, expresses, interacts, covaries, regulates, binds, treats, paliates, resembles, localizes.
  
Project files:
- <file> `process_nodes.py`
  -  Pymongo script uded to process database nodes for document assimilation.
- <file> `process_edges.py`
  -  Pymongo script used to process database node relationships for document assimilation.
- <file> `query.py`
  -  Pymongo script used to access database for document queries.

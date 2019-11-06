import csv
import pymongo
import json

from process_node import node_process
from mongoLogin import mongoLogin

#sensitive login details
collection = mongoLogin();

#========================================================

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

#========================================================

post = {}	#collection of all

diseases = {}
genes = {}
compounds = {}
locations = {}

#populate dictionaries
node_process(diseases, genes, compounds, locations)

with open('edges.tsv') as tsvfile:
	reader = csv.DictReader(tsvfile, dialect='excel-tab')
	for row in reader:
		metaedge = row['metaedge']
		split_source = row['source'].split(":")
		split_target = row['target'].split(":")

		if metaedge == "CtD":	#compound treats disease
			comp_id = split_source[2]
			d_id = split_target[3]
			comp_name = compounds.get(comp_id)
			disease_name = diseases.get(d_id)
			if (d_id not in post):
				post[d_id] = {'Disease_id':d_id}
				post[d_id]['Name'] = disease_name
				post[d_id]['Treatments'] = []
			elif 'Treatments' not in post[d_id]:
				post[d_id]['Treatments'] = []
			post[d_id]['Treatments'].append(comp_name)

		elif metaedge == "DaG":	#disease associates gene
			d_id = split_source[3]
			g_id = split_target[2]
			gene_name = genes.get(g_id)
			disease_name = diseases.get(d_id)
			if d_id not in post:
				post[d_id] = {'Disease_id':d_id}
				post[d_id]['Name'] = disease_name
				post[d_id]['Associations'] = []
			elif 'Associations' not in post[d_id]:
				post[d_id]['Associations'] = []
			post[d_id]['Associations'].append(gene_name)

		elif metaedge == "DlA":	#disease localizes anatomy
			d_id = split_source[3]
			a_id = split_target[3]
			anatomy_name = locations.get(a_id)
			disease_name = diseases.get(d_id)
			if d_id not in post:
				post[d_id] = {'Disease_id':d_id}
				post[d_id]['Name'] = disease_name
				post[d_id]['Locations'] = []
			elif 'Locations' not in post[d_id]:
				post[d_id]['Locations'] = []
			post[d_id]['Locations'].append(anatomy_name)
#
for i in list(post):
	popped = post.pop(i)
	collection.insert_one(popped)

# print(post)
import csv
import pprint

# node file format
# <id> <name> <kind>
def node_process(diseases, genes, compounds, locations):
	with open('nodes.tsv') as tsvfile:
		reader = csv.DictReader(tsvfile, dialect='excel-tab')
		for row in reader:
			split = row['id'].split(":")	#to get kind and ID
			
			kind = split[0]
			name = row['name']
			#id is found after the row type is identified

			#if "split[0]" is gene or compound
				#0=kind, 1=nothing, 2=id
			#else if is disease
				#0=kind, 1=nothing, 2=DOID, 3=disease_id
			#else if is anatomy it's not important

			if kind == 'Disease':
				diseases[split[3]] = name
			elif kind == 'Gene':
				genes[split[2]] = name
			elif kind == 'Compound':
				compounds[split[2]] = name
			elif kind == 'Anatomy':
				locations[split[3]] = name
			else:
				print("else")

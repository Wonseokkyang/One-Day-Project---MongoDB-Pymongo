import pprint
from mongoLogin import mongoLogin

#sensitive login details
collection = mongoLogin();


query_in = input("Please enter disease DOID or name: ")
query_in = query_in.lower()
print('Searching for \"', query_in, '\"...')

#for testing
# query_in = "obesity"

results = collection.find_one({"$or":[ {'Name':query_in}, {'Disease_id':query_in} ]})

if results == None :
	print('\nDisease not found..')
else:
	for key,values in results.items():
		if key != '_id': 
			print(key, ':')
			print(values,'\n')

input("\nPlease press enter to exit.")
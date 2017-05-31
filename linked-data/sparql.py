from SPARQLWrapper import SPARQLWrapper, XML, JSON


sparql = SPARQLWrapper("")
queryString = ""

sparql.setQuery(queryString)
sparql.setReturnFormat(JSON) # OR XML, OR RDF etc.
# return the spqarl object containing bound results
results = sparql.query().convert()

for result in results:
	print(result)

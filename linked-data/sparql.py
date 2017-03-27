from SPARQLWrapper import SPARQLWrapper, JSON, RDF, XML


sparql = SPARQLWrapper("")
queryString = ""

sparql.setQuery(queryString)
sparql.setReturnFormat(XML)
# return the spqarl object containing bound results
results = sparql.query().convert()

for result in results:
	print(result)
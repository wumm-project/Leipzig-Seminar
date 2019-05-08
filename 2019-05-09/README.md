# Anmerkungen zum Seminar am 09.05.2019

Mofeed Hassan und Amrapali Zaveri aus dem [AKSW Team](http://aksw.org) haben
mehrere Millionen Datensätze aus der Datenbank des USPTO analysiert und als
RDF in einem Store bereitgestellt.  Details dazu siehe 

http://aksw.org/Projects/USPatents.html

Each year, the United States Patent and Trademark Office (USPTO) grants over
150,000 patents to individuals and companies all over the world. As of
December 2011, 8,743,423 patents have been issued and 16,020,302 applications
have been received. The USPTO patents are accepted in electronic form and are
filed as PDF documents. However, the indexing is not perfect and it is
cumbersome to search through the PDF documents. Additionally, Google has also
made all the patents available for download in XML format, albeit only from
the years 2002 to 2015. Thus, we converted this bulk of data (spanning 13
years) from XML to RDF to conform to the Linked Data principles.

SPARQL Endpunkt: http://us.patents.aksw.org/sparql



PREFIX patent: <http://us.patents.aksw.org/> 
PREFIX patents: <http://us.patents.aksw.org/ontology/> 
PREFIX patentp: <http://us.patents.aksw.org/property/> 
PREFIX dc: <http://purl.org/dc/terms/> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

select ?p ?o from
<http://us.patents.aksw.org/>
where { patent:06906845 ?p ?o .}



Hans-Gert Gräbe, 07.05.2019

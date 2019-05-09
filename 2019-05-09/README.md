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

Im RDF-Graphen <http://uspatents.aksw.org> sind die Informationen zu den
einzelnen Patenten enthalten, im RDF-Graphen <http://links.uspatents.aksw.org>
werden Verweise auf die entsprechenden Patente im EPO (European Patent Office)
angegeben.

Beispiel-Anfragen dazu in der Datei Queries.txt

Dazu gibt es auch ein Paper:

Mofeed M. Hassan, Amrapali Zaveri, Jens Lehmann: A linked open data
representation of patents registered in the US from 2005–2017.
Sci. Data. 5:180279 doi: 10.1038/sdata.2018.279 (2018).

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6278688/

Dort ist in einem Diagramm auch die genaue Modellierung zu finden. 

Hans-Gert Gräbe, 09.05.2019

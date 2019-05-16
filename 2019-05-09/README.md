# Anmerkungen zum Seminar am 09.05.2019

## Der AKSW RDF-Store zu US Patenten

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

## Patentrecherchen

**Frage:** Warum so kompliziert? Kann man nicht einfach die Sucheseite eines
der Patentämter hernehmen und dort die Indexsuche oder die Suche nach
Schlagworten verwenden?

**Antwort:** Im Prinzip ja, und das sollte als erstes untersucht werden.
Allerdings sind diese Suchschnittstellen meist statisch in dem Sinne, dass nur
solche Suchanfragen gestellt werden können, die von den Anbietern
vorausgesehen wurden.  Oft werden auch Datensätze zu Patentmetadaten
regelmäßig veröffentlicht, die man sich herunterladen kann und darauf seine
eigene Suche organisieren.  Im Rahmen der oben besprochenen Arbeit wurde dies
mit Daten des US-Patentamts (USPTO) ausgeführt, die vom USPTO
veröffentlichten Daten auf ein RDF Datenmodell gemappt und dieses für eine
semantische Suche in einen RDF-Store hochgeladen.  Die Ausdrucksmöglichkeiten
einer solchen semantischen Suche sind mit denen einer klassischen
Datenbank-Anfragesprache vergleichbar und damit um Größenordnung flexibler als
eine einfache Indexsuche.  Man kann hier oft auf der Ebene einer "einfachen"
*Anfrage* das herausbekommen, was man einem lokalen Index selbst
*programmieren* müsste. 

### Patentrecherche in den Daten des USPTO

* [Einstiegsseite im Web](https://www.uspto.gov/)
* [Indexsuche](https://www.uspto.gov/)
* Das USPTO stellt vierteljährlich Datensätze im XML-Format zur Verfügung:
  * https://www.uspto.gov/learning-and-resources/xml-resources

### Europäisches Patentamt (EPO)

* [Einstiegsseite im Web](https://www.epo.org)
* [Indexsuche](https://www.epo.org/searching-for-patents_de.html)
* [Linked Open EP Data](https://www.epo.org/searching-for-patents/data/linked-open-data_de.html)
  * Der Dienst Linked Open EP Data verknüpft Patentinformationen des EPA und
    anderer Anbieter zu einem offenen Netz aus Daten, die mit
    Standard-Webtechnologien wie HTTP, URI, RDF und SPARQL durchsucht,
    abgefragt und angezeigt werden können.
  * Dort auch Nutzerleitfaden und Beispiele für SPARQL Queries
* [SPARQL Endpunkt des Linked Open EP Data Service](https://data.epo.org/linked-data/sparql.html)
* [Patent Ontology Overview](https://data.epo.org/linked-data/documentation/patent-ontology-overview.html)


### Deutsches Patent- und Markenamt (DPMA)

* [Einstiegsseite im Web](https://www.dpma.de)
* [Indexsuche](https://www.uspto.gov/)
* Das USPTO stellt vierteljährlich Datensätze im XML-Format zur Verfügung:
  * https://www.uspto.gov/learning-and-resources/xml-resources

### Die [Internationale Patentklassifikation (IPC)](http://depatisnet.dpma.de/ipc/)

(Quelle: https://www.dpma.de/patente/recherche/index.html) 

In der Internationalen Patentklassifikation (IPC) sind technische Sachverhalte
klassifiziert. Die IPC dient der Ordnung der Patent- und
Gebrauchsmusterschriften und ermöglicht mit Hilfe von Klassifikationssymbolen
die sprachunabhängige Recherche dieser Dokumente. Die IPC bildet das gesamte
Gebiet der Technik ab und enthält über 70.000 Unterteilungen, denen die
Dokumente zugeordnet werden.

In [DEPATISnet](https://depatisnet.dpma.de/) finden Sie die aktuelle und alle
früheren Ausgaben/Versionen der Internationalen Patentklassifikation: in
deutscher, englischer und französischer Sprache. Die Recherchefunktion
ermöglicht das Auffinden von IPC-Stellen mit Hilfe von Stich- und
Schlagworten. Hier finden Sie auch die IPC-Konkordanz, mit der Sie Änderungen
zwischen aufeinander folgenden Versionen der IPC nachvollziehen können. Die
Hilfsfunktion enthält neben einer Anleitung zur Nutzung des IPC-Verzeichnisses
auch Informationen zum Aufbau der IPC.

(Quelle: https://data.epo.org/linked-data/documentation/patent-ontology-overview.html) 

To aid finding patent applications, they are classified using the Cooperative
Patent Classification (CPC) classification scheme or the older International
Patent Classification (IPC) scheme which CPC extends.

* https://www.cooperativepatentclassification.org/about.html
* http://www.wipo.int/classifications/ipc/en/

(Quelle: https://www.cooperativepatentclassification.org/about.html)

The EPO and USPTO both had highly developed patent classification systems, the
European CLAssification (ECLA) and the United States Patent Classification
(USPC) respectively. CPC is the outcome of an ambitious harmonization effort
to bring the best practices from each Office together. In fact, most
U.S. patent documents are already classified in ECLA. The conversion from ECLA
to CPC at the EPO will ensure IPC compliance and eliminate the need for the
EPO to classify U.S. patent documents. At the USPTO, the conversion will
provide an up-to date classification system that is internationally
compatible.

* [The linked data representation of the CPC taxonomy](https://www.cooperativepatentclassification.org/cpcSchemeAndDefinitions/CPCopenLinkedData.html)

Hans-Gert Gräbe, 12.05.2019, ergänzt am 16.05.

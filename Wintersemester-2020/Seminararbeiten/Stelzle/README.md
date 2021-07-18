# Wintersemester 2020/21. Seminararbeit Tarek Stelze

## Thema Funktionale Analyse 

Funktionale Analyse ist im heutigen Verständnis der Kern der TRIZ.
Wesentliches Instrument sind die _40 Prinzipien_ und (bereits bei Altschuller
mit Abstrichen betrachtete) Widerspruchsmatrix. Beides liegt bereits als RDF
in den WUMM RDFData vor, müsste aber möglicherweise noch einmal gegen die
historische Genese abgeglichen werden.

Im Rahmen des TOP Webinars wurde das Thema am 20.10.2020 von Nikolay Shchedrin
vorgetragen, siehe dazu <https://wumm-project.github.io/2020-10-20> und die
Folien (in Russisch) sowie Anmerkungen (in englischer Übersetzung) dort.  Der
Foliensatz ist auch in diesem Verzeichnis verfügbar, eine Übersetzung der
nicht-graphischen Teile ins Deutsche steht noch aus.

Die Konzepte sind im TRIZ Summit Ontologie-Projekt recht ausführlich,
allerdings in Russisch, dargestellt und von der Einstiegsseite
<https://triz-summit.ru/onto_triz/mod/metod/triz/fa/model_fa> aus erreichbar.

Siehe auch den Eintrag Functional Analysis
<http://wumm.uni-leipzig.de/displayuri.php?uri=FunctionalAnalysis> und die
dort weiterführenden Links in der Top Level Ontologie des WUMM-Projekts.

Weitere Literatur:
* Koltze, Souchkov (2018). Systematische Innovation. 
* Anmerkungen auf <https://wumm-project.github.io/2020-10-20>

## Arbeiten

1) Die __MATRIX 2003__ wurde für das Ontologieprojekt aufbereitet. Später
stellte sich allerdings heraus, dass es sinnvoller ist, die einzelnen
Versionen der Matrix direkt im JSON-Format als Liste von Matrix-Einträgen zu
speichern statt diese in ein komplizierteres RDF-Format zu verwandeln.
Entsprechend wurde die hier erstellte CSV-Variante der Matrix direkt in das
JSON-Zielformat umgewandelt und unter Matrix/Matrix2003.json in das Repo
_RDFData_ aufgenommen.  Die Daten im Verzeichnis _Scripts_ sind damit
übernommen, die dort entwickelten Werkzeuge obsolet.  Die Dateien
_TheMatrix2003.ttl_, _TheParameters.ttl_ und _ThePrinciples.ttl_ wurden im
Original weiterentwickelt und sind hier ebenfalls entfernt, um Konfusion zu
vermeiden.

2) __Entwicklung einer Ontologie "Functional Analysis"__. 
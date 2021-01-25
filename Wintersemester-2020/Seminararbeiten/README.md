# Wintersemester 2020/21. Seminararbeiten

## Hintergrund

Im Bereich der TRIZ-Forschung wurde vor einem Jahr ein TRIZ Summit
Ontologie-Projekt (TOP) <https://triz-summit.ru/onto_triz/> (in Russisch)
begonnen, um die verschiedenen Teile der TRIZ-Theorie ontologisch zu
„kartieren“ und die wesentlichen Zusammenhänge zwischen den einzelnen Teilen
mit Mitteln semantischer Technologien zu erfassen. Hierzu liegen aktuell vor

(1) eine „Übersichtskarte“ der verschiedenen Theoriefelder (des TRIZ Body of
    Knowledge) und der Zusammenhänge zwischen diesen,
(2) ein „Atlas“ von Ontokarten, die grob einzelne Bereiche markieren, die
    weiter zu detaillieren sind,
(3) zu einzelnen dieser Ontokarten erste Versuche, Struktur in das
    begriffliche Chaos zu bringen,
(4) ein Glossar (oder auch nur ein Thesaurus) von Begriffen, die hierfür
    wichtig sind.

Details hierzu sind auf der (englischen)
[TOP-Übersichtsseite](https://wumm-project.github.io/TOP) zusammengetragen.
Siehe dazu auch die
[TOP-Einstiegssteite](https://wumm-project.github.io/Ontology) sowie die
[Handreichung zu den Seminararbeiten](Seminararbeiten.pdf).

Während zu (1) und (2) weitgehend Konsens besteht, sind die Modellierungen in
(3) stark umstritten, da die entsprechenden Semantiken und Zusammenhänge in
den unterschiedlichen TRIZ-Schulen naturgemäß unterschiedlich verstanden
werden.

Streit gibt es auch zu (4), der aber deutlich einfacher zu klären ist, wenn 

(4a) zunächst einmal alle Begriffe gesammelt und „URIfiziert“ werden
     (Thesaurus raw),

(4b) URIs so weit zusammengeführt werden, dass verschiedene URIs auf
     verschiedene Konzepte verweisen, aber Raum bleibt, für gleiche Konzepte
     verschiedene Semantiken zu hinterlegen (Thesaurus final),

(4c) diese verschiedenen Semantiken auch wirklich zusammengetragen und
     formalisiert werden (Glossar raw) und schließlich

(4d) die Semantiken in einem komplexen sozialen Abstimmungsprozess so weit wie
     _möglich_ abgeglichen und essenzielle Differenzen semantisch modelliert
     werden.

Im Rahmen eines WUMM TOP Companion Projekts wurden und werden Teile dieser
Ontologisierungen nachmodelliert.

Siehe dazu das Verzeichnis _Ontologies_ im [github-Repo
RDFData](https://github.com/wumm-project/RDFData), die im Original bisher
ausschließlich durch grafische Ontogramme sowie die Möglichkeit einer
visuellen Inspektion im verwendeten OSA-Ontologie-Editor zugänglich sind.

Diese im Original ausschließlich russischsprachigen Quellen wurden dabei in
Teilen auch ins Englische und Deutsche übertragen.  Weitgehend semantisch
erfasst sind (1) und (2). Weiterhin wurde bereits früher das VDI-Glossar
„RDFiziert“ und die dort vorhandenen deutschen und englischen Erläuterungen um
eine russische Übersetzung ergänzt. Dies sowie der einfach zu transformierende
Thesaurus auf den Altschullerseiten bilden die Grundlage für einen eigenen
Thesaurus nach (4a), der mit den Begrifflichkeiten des Originalprojekts weiter
abzugleichen ist.

## Themen für Seminararbeiten

In den Seminararbeiten soll am Punkt (3) weitergearbeitet werden, indem für
eine konkrete Ontokarte X

(A) die Zusammenhänge für das WUMM-Projekt in RDF in einer gemeinsamen
    Rahmensetzung nachmodelliert werden sowie

(B) differierende Semantiken, Probleme und Widersprüche im Verständnis der
    modellierten TRIZ-Konzepte zusammengetragen und systematisiert werden.

Während (A) primär einen ingenieur-technischen Charakter hat, erfordert (B)
stärker einen akademischen Zugang von Recherche und Vergleich einschlägiger
Publikationen.

Die Seminararbeit soll in LaTeX erstellt werden und möglichst in Englisch
verfasst sein.  Bitte benutzen Sie dazu die (nicht sehr umfangreiche) Vorlage
ls.sty im Wurzelverzeichnis des Repos.

## Folgende Themen wurden dazu vergeben:

* Funktionale Analyse (Tarek Stelzle)
* Evolutionsbäume zur Beschreibung technischer Entwicklung (Tom Strempel)
* Flussmodelle und Flussanalyse (Immanuel Thoke) 
* Modellierung des IDM-Modells aus Vorgängerarbeiten (Karim Rakia)


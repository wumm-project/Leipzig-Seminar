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

## Anmerkungen zur Seminararbeit

### Matrix 2003

Die __MATRIX 2003__ wurde für das Ontologieprojekt aufbereitet. Später stellte
sich allerdings heraus, dass es sinnvoller ist, die einzelnen Versionen der
Matrix direkt im JSON-Format als Liste von Matrix-Einträgen zu speichern statt
diese in ein komplizierteres RDF-Format zu verwandeln.  Entsprechend wurde die
hier erstellte CSV-Variante der Matrix direkt in das JSON-Zielformat
umgewandelt und unter Matrix/Matrix2003.json in das Repo _RDFData_
aufgenommen.  Die Daten im Verzeichnis _Scripts_ sind damit übernommen, die
dort entwickelten Werkzeuge obsolet.  Die Dateien _TheMatrix2003.ttl_,
_TheParameters.ttl_ und _ThePrinciples.ttl_ wurden im Original
weiterentwickelt und sind hier ebenfalls entfernt, um Konfusion zu vermeiden.

### Translating

Hierzu wurde ein Skript entwickelt, um den Google Translator für
Textübersetzungen einzelner Literale in RDF-Dateien einzusetzen.  Die 
entsprechende Anleitung zum Einsatz ist aus der Arbeit hierher übernommen. 

For translating the various tags a python script was implemented, which takes
a turtle files as input and adds the missing language tags.  Therefore the
script checks each line which already has a language tag.  Then it makes an
api call with the first tag as the source language.  It adds the language tags
for English, German and Russian.  Each tag is a separate api call.  For
translation the Google Translator <https://pypi.org/project/deep-translator/>
is used.

Using the Script:

Requirements: Python3, pip, virtualenv
```
python3 -m venv env        # create env as virtualenv
source env/bin/activate    # start env, lines are prepended wirh (env)

# install library
python3 -m pip install deep-translator 
python3 -m pip install rdflib

# run translation
python translateText.py <InputTurtleFile>.ttl

# skip the venv
deactivate
```

This will output a file name `translated_<InputTurtleFile>.ttl` as a new
turtle file with new language tags added.  Furthermore all translated words or
sentences will be shown in the terminal output.

Skript arbeitet aktuell zeilenorientiert ohne Berücksichtigung der
RDF-Struktur, was für die Zwecke der Arbeit - Übersetzung von Literalen ohne
Zeilenumbrüche aus einer Targetsprache in die Zielsprachen - ausreichend ist. 

Eine Verwendung eines RDF Parsers (python redlib) für die strukturelle
Aufbereitung des RDF sollte in einer nächsten Version eingebaut werden, um die
zu übersetzenden Literale genauer fassen zu können.

### Entwicklung einer Ontologie "Functional Analysis"

Die Modellierung geht von der Darstellung der Funktionsanalyse bei
(Koltze/Souchkov, Kap. 4.4) aus.

Das Konzept geht davon aus, dass Komponenten, Objekte, Ressourcen in einem
_System_ durch funktionale Beziehungen miteinander verbunden sind, aus deren
Zusammenspiel sich die Gesamtfunktion des Systems ergibt. Zunächst ist ein
solches _Funktionales Modell_ des Systems zu erstellen. Dieses ist in einer
zweiten Phase im Rahmen einer _Funktionsanalyse_ nach der TRIZ-Methodik zu
untersuchen und eine Systemtransformation unter Einsatz der TRIZ-Instrumente
vorzunehmen, die Defizite des "Systems, wie es ist" als _Basisvariante_
beseitigt.

Die Aufgabenstellung ist einem frühen Versuch zuzuordnen, die Ontologisierung
von einzelnen TRIZ-Konzepten weiter zu schärfen.  An konkreten selbst zu
wählenden Anwendungsbeispielen war das entwickelte Begriffssystem im Einsatz
zu demonstrieren. Damit sollte gewährleistet werden, dass mit den entwickelten
Sprachkonzepten die TRIZ-methodischen Ansätze im Beispiel adäquat ausgedrückt
werden können.

In welchem Umfang es dabei sinnvoll ist, Unterscheidungen zwischen den beiden
oben genannten Phasen bereits auf der Ebene der Begriffssysteme zu treffen
(siehe dazu inzwischen <https://wumm-project.github.io/Texts/WOP-Basics.pdf>)
war zum Zeitpunkt der Erstellung der Seminararbeit noch nicht klar.  Im
Nachgang stellt sich heraus, dass man sich zunächst auf die Taxonomie des
funktionalen Modells konzentrieren sollte, da dieses Grundlage ist, um die
Methodik-Sprache überhaupt erst zu entwickeln.  WUMM postuliert an dieser
Stelle inzwischen, dass diese Sprachentwicklung in zwei Stufen erfolgen muss.

In den vier Beispielen wird auch nur an einer Stelle (CarExample) versucht,
mit der Beschreibung der Anwendung der Matrix auf die Ebene der
Systemtransformationen und damit der Funktionsanalyse zu wechseln. In den
anderen Beispielen konzentriert sich der Autor auf die Ebene der funktionalen
Modellierung.

Die Modellierung folgt der in (Koltze/Souchkov, Kap. 4.4) entwickelten
Vorgehensweise, wobei allerdings die Unterscheidung von "Systems, Components,
Subsystems, Objects, Subjects, ..." undeutlich bleibt. Hier werden allerdings
auch in der TRIZ die eigenen Definitionen in praktischen Beispielen wenig
konsequent umgesetzt.  Insbesondere scheint es angemessen, die Begriffe
_System_, _Komponente_ und _Funktion_ genauer zu unterscheiden und dabei eine
infaltionäre Verwendung des Systembegriffs zu vermeiden. Siehe dazu die
Definition "Untersystem" bei Souchkov, die einen neuen eigenen
Modellierungkontext aufspannt (Hierarchisches Modell).  Auch ist zu bedenken,
ob _Ressource_ als weiteres Konzept (etwa für Passagiere, Luft, Straße,
Benzin, ... im Car-Example) erforderlich ist, mit dem Stellen einer _Kopplung
von Systemen_ markiert werden.

In (Koltze/Souchkov) wird ein _System_ als Bündel von zusammenspielenden
Funktionalitäten gesehen, die Abgrenzung des Systems erfolgt auf dieser
funktionalen Ebene.  Für Systeme ist also eine White-Box-Betrachtung und Fokus
auf Implementierungen typisch.  Die Funktionalitäten werden als
(bidirektionale) _Interaktionen_ zwischen Komponenten gefasst (S. 119) oder
spezifischer als (unidirektionale) _Aktionen_ zwischen Werkzeug und
bearbeitetem Objekt.  Funktionen haben (in diesem systemischen Kontext)
verschiedene _Qualitäten_ (S. 120).

_Komponenten_ stellen einzelne Funktionen zur Verfügung, wobei Komponenten "im
System", im Obersystem oder als Produkt (Bild 4.35) lokalisiert werden können.
Komponenten können sich damit "innerhalb", aber auch "außerhalb" des Systems
befinden.  Für Komponenten ist eine Black-Box-Betrachtung und Fokus auf
(funktionsfähige) Spezifikationen typisch.

Die Erarbeitung des _Funktionsmodells_ erfolgt in fünf Schritten:

1. Erstellen des Komponenten-Modells des Systems.
2. Bestimmen der Interaktionen (vgl. die SCRUM Epics).
3. Aufspalten der Interaktionen in Funktionen. Es können mehrere Funktionen an
   einer Interaktion beteiligt sein.
4. Richtung der Funktionen bestimmen.
5. Qualität der Funktion bestimmen.

Entsprechend wird in den vier Beispielen jeweils zunächst ein
Komponentenmodell entwickelt und danach einzelne Funktionen modelliert.  Für
jede solche Funktion werden nacheinander die Konzepte tc:Action,
tc:Interaction, tc:SubjectActionObject und schließlich tc:Function
instanziiert.  Die Verwendung von Konzepten wie tc:Action sowohl als Subjekt
als auch Prädikat entspricht nicht den RDF-Modellierungsregeln. Ebenso sollten
Prädikatnamen mit Kleinbuchstaben beginnen und Verweise auf Tätigkeiten als
"sprechende Namen" tragen.  Objectives werden zwar in der Ontologie
_FunctionalAnalysis.ttl_ als Begriffe eingeführt, in den Beispielen fehlen
aber entsprechende Instanziierungen.
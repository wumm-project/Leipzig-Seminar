# Auswertung der Arbeit mit dem TRIZ-Trainer

Grundlage der folgenden Überlegungen sind eigene Beobachtungen sowie ein
ausführliches Gespräch mit den beteiligten Studierenden am 28.01.2020.

Zunächst die methodischen Erfahrungen:

1) Ziel ist es nicht, Probleme zu lösen, sondern am Lösen von Problemen mit
der Methodik vertraut zu werden. Die Studenten tun sich besonders am Anfang
sehr schwer damit, von einer schnellen Brainstorming-Lösung zu einer
systematischen Vorgehensweise entsprechend der vorgestellten Methodik
überzugehen.  Am Anfang ist wahrscheinlich eine stärkere Präsenzphase
erforderlich, in der im angeleiteten Praktikumsbetrieb der Einstieg in die
Thematik als stärker synchronisierter Lernprozess organisiert wird.  Ähnlich
geht auch Denis Cavallucci in Strasbourg vor.

2) Trotz der guten Online-Anleitung im Abschnitt "Lösungsprozess" wurde diese
initial kaum zur Kenntnis genommen. Im Sinne eines "flipped classroom"
Konzepts muss und soll das aber vorausgesetzt werden.  Bei Denis müssen
parallel zum Praktikumskurs hier Testfragen beantwortet werden, was zum
Bestehen des Praktikums zusätzlich auf angemessenem Niveau zu absolvieren ist.
Der Stand ist in einer Online-Übersicht wenigstens für den Dozenten einsehbar.

3) Es könnte hilfreich sein, die Arbeit in Zweierteams vorzusehen, da die
gemeinsame Diskussion ein wichtiges Moment im Kompetenzaufbau ist (siehe etwa
das "Pair Programming" im Bereich der Programmiermethodiken). Das müsste
im Trainer strukturell eingebaut werden.

Nun zu inhaltlichen Punkten:

1) Kontextualisierung der Problemstellung. Das ist ein allgemeines Problem des
TRIZ-Ansatzes, das auch schon Dima Bakhturin in Minsk 2019 thematisiert hat:
Die meisten Beispiele sind so gebaut, dass man im Nachhinein eine tolle Lösung
daraufhin analysiert, wie man auch mit TRIZ hätte drauf kommen können. Auch
Altschullers Patentanalyse hat diesen Charakter.  Die implizite
Kontextualisierung der Aufgabenstellung geht dabei allerdings verloren, womit
eine starke Erwartungshaltung an den Lösungsweg verbunden ist (? - ich kenne
keine Musterlösungen), die teilweise bis in die Aufgabenstellung hinein
formuliert ist.  Das methodische Problem ist aus der Mathematik gut bekannt -
ein Beweis wird üblicherweise durch Rückwärtsarbeiten "erarbeitet", ist aber
"im Vorwärtsgang" aufzuschreiben.  Wenn man das erstere nicht versteht, fallen
im zweiteren die Argumente "vom Himmel" (z.B.: Warum die Terme im Beweis nun
genau so exotisch zusammenfassen? Weil beim Rückwärtsarbeiten genau dieser
Term entstanden ist und auseinandergenommen wurde.). Eine wirkliche Antwort
auf dieses Problem habe ich nicht, sehe nur auf der anderen Seite aus den
Gesprächen mit Kirill Domkin, dass die Anwendung der TRIZ-Methodik auf
konkrete praktische Problemsituationen vor diesem Problem nicht steht, da dort
die Kontextualisierung bekannt und die Lösung auch den "Trainern" unbekannt
ist.

2) Wir haben dies intensiv an den drei Aufgaben
(a) Schiffsmast
(b) Wie kann man einen schweren Zug anfahren
(c) Kipper verschmutzt die Luft
diskutiert.

(a) Das hatte ich schon anderenorts thematisiert. Geht man vom System
"Wasserstraßennetz" aus, so ist eine einfache Lösung "gib im Navi ein, dass
die Brücke gesperrt ist, und lass das Navi einen anderen Weg suchen".  Das ist
wahrscheonlich nicht im Sinne der Aufgabenstellung, denn die fordert
eigentlich, dort durchzufahren, egal wie sinnvoll das ist.  Start könnte also
beim System "Boot" sein, bei dessen Analyse kommt der Mast aber nicht vor.  Es
bleibt hier also unklar, wozu der Mast überhaupt gut ist. Die beiden
Funktionen "Antenne" und "Oberlicht" lassen sich zuordnen - das Oberlicht
gehört zur vorgeschriebenen Beleuchtung (Obersystem "Wasserstraßennetz"), die
Antenne zur Komponente "Radiosystem" des Teilsystems "Steuerung". Beides hätte
man längst anders realisieren und den Mast rauswerfen können.  Hier scheinen
also noch zusätzliche Funktionen im Spiel zu sein, die zu der Randbedingung
führen, dass der Mast auf keinen Fall verändert werden kann.

Studentische Lösungen:
* Mast klappbar gestalten
* Mast durch biegsame Antenne ersetzen (Oberlicht braucht man nur, um den
  hohen Mast zu markieren - kein Mast, kein Oberlicht erforderlich)
* Hohlräume des Schiffs mit Wasser füllen, die Wasserlinie des Bootes kommt
  höher und das Boot passt wieder unter der Brücke durch.

An welche Lösung denken die Autoren? 

(b) Das war relativ klar, eine Analyse genau nach der Methodik war schwer (was
ist Inertialwiderstand, geht es um Kraft oder Energie, welche Energieformen
sind wo präsent?). Lösungen waren im Wesentlichen
* Kupplungen zwischen den Wagen durch Federn ersetzen
* Zug zunächst leicht zusammenschieben, Kupplungen hängen durch, dann Zug
  anfahren, der Inertialwiderstand der Wagen wird erst nach und nach wirksam.
  (Problem hier, ob die Kupplungen das aushalten).
* Mein Ansatz: Zug scharf zusammenschieben, so dass die Puffer krachen. Damit
  wird potenzielle Energie in den Federn der Puffer gespeichert und beim
  weiteren Anfahren Schritt für Schritt abgegeben. Analog 2. Lösung, abr nich
  etwas weiter analysiert.

An welche Lösung denken die Autoren? 

(c) Hier gab es die schärfste Diskussion zur Aufgabenstellung:

"Wir haben versucht, dieses Problem durch die Installation von Filtern am
Auspuffrohr des Lastwagens zu lösen. Die Kosten für solche Filter sind jedoch
hoch. Sie müssen häufig gereinigt werden. Dies führt zu Ausfallzeiten des
Lastwagens. Frage: Wie kann man Abgase filtern, ohne das Design und den
Betrieb des Autos zu verkomplizieren?"

Lösungen: 
* Eine studentische Lösung: Abgase in einem Ballon auffangen und außerhalb des
  Steinbruchs zentral bearbeiten (Abgasanlage also um eine Komponente
  erweitern).
* Meine Lösung: Analyse Maschine "Kipper", Teilsystem "Motoranlage" (von
  Ansaugeinrichtung bis Abgasanlage), Komponentenanalyse dieses Systems,
  vorhandene Komponente Filter in der Abgasanlage entweder modifizieren oder
  weitere Komponente mit entsprechender neutraisierender Funktion anhängen
  (typische Lösung heute: ad blue, also Harnstoff nutzen, um die schädlichen
  Gase zu neutralisieren; TRIZ Prinzip der starken Oxidationsmittel).

Beide Lösungen wurden in der Diskussion hart verworfen, da sie die Bedingung
"ohne das Design und den Betrieb des Autos zu verkomplizieren" nicht erfüllen.
Lösungen unter dieser Bedingung seien überhaupt nur im System "Steinbruch" als
Ganzem denkbar.

An welche Lösung denken die Autoren?
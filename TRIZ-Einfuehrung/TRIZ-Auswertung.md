# Auswertung der Arbeit mit dem TRIZ-Trainer

## Diskussion am 28.01.2020 mit den beteiligten Studierenden.

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
Konzepts muss und soll das aber vorausgesetzt werden.  Bei Denis Cavallucci
müssen parallel zum Praktikumskurs hier Testfragen beantwortet werden, was zum
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
eine starke Erwartungshaltung an den Lösungsweg verbunden ist, die teilweise
bis in die Aufgabenstellung hinein formuliert ist.  Das methodische Problem
ist aus der Mathematik gut bekannt - ein Beweis wird üblicherweise durch
Rückwärtsarbeiten "erarbeitet", ist aber "im Vorwärtsgang" aufzuschreiben.
Wenn man das erstere nicht versteht, fallen im zweiteren die Argumente "vom
Himmel" (z.B.: Warum die Terme im Beweis nun genau so exotisch zusammenfassen?
Weil beim Rückwärtsarbeiten genau dieser Term entstanden ist und
auseinandergenommen wurde.). Eine wirkliche Antwort auf dieses Problem habe
ich nicht, sehe nur auf der anderen Seite aus den Gesprächen mit Kirill
Domkin, dass die Anwendung der TRIZ-Methodik auf konkrete praktische
Problemsituationen vor diesem Problem nicht steht, da dort die
Kontextualisierung bekannt und die Lösung auch den "Trainern" unbekannt ist.

2) Wir haben dies intensiv an den drei Aufgaben
(a) Schiffsmast
(b) Wie kann man einen schweren Zug anfahren
(c) Kipper verschmutzt die Luft
diskutiert.

(a) Das hatte ich schon anderenorts thematisiert. Geht man vom System
"Wasserstraßennetz" aus, so ist eine einfache Lösung "gib im Navi ein, dass
die Brücke gesperrt ist, und lass das Navi einen anderen Weg suchen".  Das ist
wahrscheinlich nicht im Sinne der Aufgabenstellung, denn die fordert
eigentlich, dort durchzufahren, egal wie sinnvoll das ist.  Start könnte also
beim System "Boot" sein, bei dessen Analyse kommt der Mast aber nicht vor.  Es
bleibt hier also unklar, wozu der Mast überhaupt gut ist. Die beiden
Funktionen "Antenne" und "Oberlicht" lassen sich zuordnen - das Oberlicht
gehört zur vorgeschriebenen Beleuchtung (Obersystem "Wasserstraßennetz"), die
Antenne zur Komponente "Radiosystem" des Teilsystems "Steuerung". Beides hätte
man längst anders realisieren und den Mast rauswerfen können.  Hier scheinen
also noch zusätzliche Funktionen im Spiel zu sein, die zu der Randbedingung
führen, dass der Mast auf keinen Fall komplett entfernt werden kann.

Studentische Lösungen:
* Mast klappbar gestalten
* Mast durch biegsame Antenne ersetzen (Oberlicht braucht man nur, um den
  hohen Mast zu markieren - kein Mast, kein Oberlicht erforderlich)
* Hohlräume des Schiffs mit Wasser füllen, die Wasserlinie des Bootes kommt
  höher und das Boot passt wieder unter der Brücke durch.

(b) Das war relativ klar, eine Analyse genau nach der Methodik war schwer (was
ist Inertialwiderstand, geht es um Kraft oder Energie, welche Energieformen
sind wo präsent?). Lösungen waren im Wesentlichen
* Kupplungen zwischen den Wagen durch Federn ersetzen
* Zug zunächst leicht zusammenschieben, Kupplungen hängen durch, dann Zug
  anfahren, der Inertialwiderstand der Wagen wird erst nach und nach wirksam.
  (Problem hier, ob die Kupplungen das aushalten).
* Mein Ansatz: Zug scharf zusammenschieben, so dass die Puffer krachen. Damit
  wird potenzielle Energie in den Federn der Puffer gespeichert und beim
  weiteren Anfahren Schritt für Schritt abgegeben. Analog 2. Lösung, aber noch
  etwas weiter analysiert.

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
  weitere Komponente mit entsprechender neutralisierender Funktion anhängen
  (typische Lösung heute: ad blue, also Harnstoff nutzen, um die schädlichen
  Gase zu neutralisieren; TRIZ Prinzip der starken Oxidationsmittel).

Beide Lösungen wurden in der Diskussion hart verworfen, da sie die Bedingung
"ohne das Design und den Betrieb des Autos zu verkomplizieren" nicht erfüllen.
Lösungen unter dieser Bedingung seien überhaupt nur im System "Steinbruch" als
Ganzem denkbar.

## Antwort von Nikolay Shpakovsky

> Das Ziel ist nicht, Probleme zu lösen, sondern am Lösen von Problemen mit
> der Methodik vertraut zu werden.

Richtig, das Ziel ist es, sich mit der Methodik vertraut zu machen und die
Fähigkeiten zu trainieren. Der Kurs ist so konzipiert, dass die Vertrautheit
mit der Methodik durch Problemlösen entsteht. Die ersten Aufgaben werden mit
dem Trainer ausführlich besprochen, damit der Student die Essenz des
Algorithmus und die Aktionen in ihren spezifischen Schritten versteht. Dies
ist nicht möglich, ohne die Theorie zu verstehen. Mit zunehmendem Verständnis
wird der selbstständigen Arbeit, dem Training und der Entwicklung von
Fähigkeiten mehr Aufmerksamkeit geschenkt.

In der Tat wird das Prinzip des „flipped classroom“ angewendet, aber Folgendes
muss beachtet werden. In jedem Schritt gibt es Tipps und Links zu den
entsprechenden Abschnitten der Theorie.  Sie sollten besonders aktiv
eingesetzt werden, wenn die ersten 5-7 Aufgaben gelöst werden, bis die
Teilnehmer verstehen, was von ihnen verlangt wird. Hier spielt auch der
Trainer eine wichtige Rolle, der dies erklären muss.

> Parallel zum Praktikum einen Online-Kurs anbieten. 

Während des Fernunterrichts erfolgt die Kommunikation die gesamte Zeit über
den Chat - so kann direkt mit den Studenten gearbeitet werden.  Der Ansatz
eines begleitenden Online-Kurses unterscheidet sich kaum vom klassischen, wo
der größte Teil der Zeit für das Studium der Theorie aufgewendet wird. Dies
ist ohne Bezugnahme auf das Lösen von Problemen unproduktiv. Wir halten dies
für falsch, die Theorie sollte auf der Basis zu lösender Probleme
verinnerlicht werden.  Das schließt natürlich nicht aus, dass der Student sich
mit der Theorie vertraut macht.  Er soll diese bei der Lösung der Probleme
studieren.

> Arbeit in Zweier-Teams.

Dies ist eine sehr gute Idee, wir werden die Möglichkeit ihrer Umsetzung
prüfen.

> Kontextualisierung des Problems. 

Ganz richtig, das ist das Problem des TRIZ-Trainings. Altschuller tat dies in
seinen Büchern. Aber im Unterricht (bei Altschuller) lösten die Leute das
Problem und passten nicht die Antwort an die TRIZ-Methodik an. Leider ist das
weitgehend vergessen und TRIZ-Training besteht heute oft darin, die Antwort zu
begründen, die der Student bereits kennt.

Genau dieses Problem lösen wir mit unserem Ansatz. Es ist die Lösung von
Problemen nach dem zu trainierenden Algorithmus zu finden. Zu sagen, mit
welcher TRIZ-Methode ein bereits gelöstes Problem gelöst werden kann - das hat
nur einen sehr geringen Effekt.

An der Tatsache, dass die Lösung dem Trainer bekannt ist, ist nichts
auszusetzen, denn dafür ist er der Trainer. Seine Hauptaufgabe ist es, den
Studenten durch den im TRIZ-Trainer festgelegten Prozess zu führen. Die
Hauptsache ist, den Studenten zu überzeugen, nach dem Algorithmus und dem
empfohlenen Prozess zu arbeiten.

Wir glauben natürlich, dass Trainer von unseren Spezialisten geschult werden
sollten, um den Lernprozess des TRIZ-Trainers besser zu verstehen.  Das machen
wir jetzt mit den Ukrainern.  Außerdem bereiten wir methodische Materialien
vor. Das wichtigste davon ist die Analyse jeder Aufgabe nach dem Template. Nur
der Trainer kann diese Analysen sehen, was ihm hilft, die Studenten bei der
Lösung des Problems besser anzuleiten.  Natürlich wäre es besser, Schulungen
für Trainer zu organisieren. Wir werden in Zukunft darauf bestehen, aber jetzt
musste alles schnell gehen, um die deutsche Version noch in diesem Semester
produktiv zu schalten. Deshalb stellen sich Fragen.

## Zeite Auswertung vom 07.03.2020 

Das Hauptproblem, mit dem ich bisher bei allen Lösungen konfrontiert bin: Die
Studenten präsentieren im Prinzip eine Brainstorming-Lösung und biegen diese
so lange zurecht, bis sie - ihrer Meinung nach - auf den Lösungsalgorithmus
passt. Begünstigt wird das durch die recht laschen Modellierungsvorgaben im
Anfangsteil (der ganze Zweig bis zur Hypothese). Ich habe für diesen Teil
genauere Vorgaben entwickelt, die ich nun auch in den Lösungen konsequenter
abfordere, siehe die angehängte Datei (mit Auszügen aus der überarbeiteten
Version von TRIZ-Trainer.tex). Sie setzt meine früher bereits aufgeschriebenen
Überlegungen fort, wie ein Begriff "technisches System" sinnvoll gefasst
werden kann.

Zu den studentischen Lösungen: AK und FN haben ihren Teil noch vor diesen
Modifikationen abgeschlossen, dort sieht man also eher die Unzulänglichkeiten
der Argumentation. FH habe ich die 5 letzten Aufgaben zur Überarbeitung
zurückgegeben, seither aber nichts mehr von ihm gehört.  Allein LL arbeitet
aktuell weiter an den Aufgaben und bearbeitet derzeit "Angeln" und
"Bibliotheksumzug". Ich habe ihm die Aufgaben mehrfach zur Überarbeitung
zurückgegeben, um genau die genannten Aspekte besser auszuführen, wobei immer
wieder Ungereimtheiten und Inkonsistenten bis hin zu Widersprüchen in der
studentischen Argumentation auftauchen, die nach den Hinweisen Schritt für
Schritt in Richtung einer konsistenten Modellierung beseitigt werden.

Meine Kommentare schreibe ich nur noch in die offen sichtbaren Felder
"Teacher's Comment", denn das versteckte Feld "Teacher's Review" wurde von den
Studenten nicht beachtet (bzw. gar nicht wahrgenommen).

Mein Vorschlag geht dahin, diesen ersten Teil genau wie vorgeschlagen (Was ist
das System? Was ist das Obersystem? Welche Funktion erfüllt das System im
Obersystem? Wie ist das System aufgebaut? Wie sind die Systemfunktionen
implementiert?) detaillierter zu strukturieren. Man könnte sogar bewusst mit
der Aufforderung zu einer Brainstorming-Lösung beginnen (die sind nicht so
schlecht wie ihr Ruf) und dann am Ende in einer Frage "Lessons learned" den
Kontrast reflektieren lassen.


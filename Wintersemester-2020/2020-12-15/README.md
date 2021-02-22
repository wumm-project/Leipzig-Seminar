# Seminar am 15.12.2020

__Thema:__ Evolution Technischer Systeme bei B.I. Goldovsky

Diskussionsleitung: Tarek Stelzle

## Ankündigung

* [Handout](./handout.pdf)
* [Folien](./folien.pdf)

In dem Artikel werden die Ansichten von B.I. Goldovsky über die Gesetze der
Konstruktion technischer Systeme behandelt.  Das Handout ist eine kurze
Zusammenfassung des Artikels.  Die Folien dienen zusätzlich zu dem Handout bei
der Diskussion zur Einleitung in das Thema.

## Anmerkungen

B.I. Goldovsky war ein im betrieblichen Kontext tätiger Erfinder, der es bis
zum Chefkonstrukteur im U-Boot-Bau gebracht hat und damit neben Erfahrungen
aus einer technischen Erfindertätigkeit auch über umfangreiche Leitungs- und
Managementerfahrungen verfügte.

Er verstarb am 28.10.2020.  V.P. Petrov verfasste einen
[Nachruf](https://wumm-project.github.io/Texts/Goldovski-2020.pdf), in dem das
Leben von Goldovsky genauer dargestellt wird. Der Text ist in Russisch und
Englisch verfügbar.

Aus dem Vortrag habe ich in einem Koreferat die folgenden Punkte betont:

* Wie bei Zobel spielen auch bei Goldovsky mit dem Thema "Arbeitssicherheit"
  nichtfunktionale Anforderungen an technische Systeme eine wichtige Rolle.

* Der dargestellte Zusammenhang zwischen primär nützlicher Funktion PNF und
  den elementaren nützlichen Funktionen ENF weist noch einmal auf das
  Verständnis des Zusammenspiels der ENF der Komponenten (als Black Boxes) zur
  Konstitution der PNF hin. Hier wird wie bei Petrov betont, dass in der PNF
  primär das _Zusammenspiel_ der ENF wichtig ist, sich die PNF also als
  _emergentes_ Phänomen ergibt. Das Ganze ist mehr als die Summe seiner Teile.

* Funktionale Vollständigkeit (als Begriff der Beschreibungsform) ist nicht
  ohne funktionierende Energieflüsse (in der Vollzugsform) zu haben.  Das
  entspricht dem _Gesetz der Energieleitfähigkeit_.  Es bleibt die Frage, ob
  neben Energieflüssen durch alle Komponenten auch Stoff- und
  Informationsflüsse für die Arbeitsfähigkeit der Komponenten eine Rolle
  spielen.  An der Stelle wird noch einmal deutlich, dass für die
  Arbeitsfähigkeit eines TS nicht nur dessen funktionale Eigenschaften in
  Betracht zu ziehen sind, sondern auch das _Herstellen der infrastrukturellen
  Bedingungen_ für dessen Betriebsfähigkeit.

* Goldovsky betont immer wieder dazu Zusammenspiel von Funktion und
  _Wirkprinzip_.  Letzteres ist die Basis des Funktionierens auf der Ebene der
  Implementation und "verschwindet" in einer "Reduktion auf Wesentliches", in
  der das entsprechende TS nur noch als Black Box über seine _Spezifikation_
  eingeht.  Offensichtlich (so sieht es auch Shpakovsky) stellen die
  Zusammenhänge auf der Ebene der Wirkprinzipien eine zusätzliche kausale
  Verkettung in der "Welt der TS" dar, die bei einer rein funktionalen
  Betrachtung von TS auf Artefaktebene unzulässig unter den Tisch fällt.

* Das Verständnis von Steuerbarkeit entspricht dem eines unmittelbar
  arbeitenden Konstrukteurs und bleibt deutlich hinter den Ausführungen auf
  dem Seminar am 08.12.2020 zurück.  "Nichtsteuerung" und "Selbststeuerung"
  werden als Konzepte nicht unterschieden, womit auch die Stufen letzterer,
  die am 08.12. thematisiert wurden, argumentativ nicht zugänglich sind.

* Der in der klassischen TRIZ unterbelichtete Begriff der
  _Produktionseinführung_ spielt für einen Chefkonstrukteur wie Goldovsky eine
  wichtige Rolle, wird allerdings im Begriff des _Prototyps_ im Vergleich zu
  üblichen industriellen Inbetriebnahmeszenarien (wie sie auch in der
  Informatik am Lehrstuhl BIS gelehrt wurden) unterkomplex abgehandelt.

* Systeme entwickeln sich in Richtung zunehmender Komplexität, so dass immer
  wieder Phasen der "Reduktion auf Wesentliches" und damit die Separierung zu
  komplexer Zusammenhänge in technische Teilsysteme auf der Tagesordnung
  stehen.  Derartige Transformationsprozesse haben wir im Wintersemester
  2019/20 am Beispiel sozio-ökologischer Systeme genauer studiert, siehe dazu
  den
  [Seminarbericht](http://www.informatik.uni-leipzig.de/~graebe/Forschung/SIM/Report-W19.pdf).
  Es steht insbesondere die Frage, ob hier auch über die Zunahme von
  _Abstraktionsebenen_ in der Beschreibungsform technischer Systeme
  nachgedacht werden muss, wie dies in der Vorlesung am Beispiel des
  OSI-Schichtenmodells durchgespielt wird.

* Symmetrie: Symmetrie vereinfacht die Konstruktion, etwa durch Reduktion der
  Zahl der Dimensionen.  Allerdings ist dabei das Phänomen der
  [Symmetriebrechung](https://de.wikipedia.org/wiki/Spontane_Symmetriebrechung)
  zu beachten.  Asymmetrie ist ein bewährtes Lösungsprinzip für Widersprüche,
  die in symmetrischen Designs nicht lösbar sind (siehe "Buridans Esel").

## Kommentierter Chat

### Entwicklung der PNF (und damit des TS) in der Zeit

[09:36] Tom Strempel : Kann die PNF eine Funktion der Zeit sein? Wenn sich bei
einem Gegenstand der Nutzen mit der Zeit ändert, sollte sich ja auch die PNF
ändern.
* Ja, Anforderungen ändern sich über die Zeit. Dies muss als
  Transitionsprozess gestaltet werden.

[09:38] Immanuel Thoke : @Tom würde ich auch so verstehen, dann kann man auch
PNF-Invarianten einfacher betrachten

[09:39] Immanuel Thoke : mit einer mehrperiodischen ENF-Funktionsstruktur
(daher dann auch die Nicht-Trivialität)
* Hier wurde noch einmal über den Zusammenhang der Konzepte PNF und ENF
  gesprochen.

[09:41] Tom Strempel : @Immanuel Dadurch könnte man auch subjektive
Unterschiede erklären

[09:46] Immanuel Thoke : jap und trotzdem objektiver Wirkprinzipien

### Technische Systeme und Zustände

In der Informatik werden zustandslose und zustandsbehaftete Systeme
unterschieden.  Der in der TRIZ favorisierte Ansatz einer funktionalen
Modellierung mit einer PNF im Zentrum ist ein auf den ersten Blick
zustandsloser Ansatz, im Beispiel in der Vorlesung (Autokarosserie) hatte ich
gezeigt, dass in dem Ansatz das durch die PNF bearbeitete Objekt Träger von
Zustand ist, da es ja genau durch die PNF in einen für die weitere Nutzung
geeigneten Zustand überführt wird. Solche Ansätze werden in (Szyperski 2002)
genauer beleuchtet. Ob allerdings die dort getroffene Unterscheidung in
zustandslose Komponenten und zustandsbehaftete Objekte auch hier insgesamt
trägt, müsste genauer ausgeleuchtet werden. 

[09:49] Immanuel Thoke : die Zustandslosigkeit ist nur in der aktiven ENF -
die Zustandsänderung schlägt sich im Kontext der PNF und der anderen ENF
nieder
* Nein, die Zustandsänderung wird am _Objekt_ bewirkt, auf welches die PNF
  (als konzertierte Wirkungen der ENF) _wirkt_.

[09:50] Kleemann : wie funzt gedächtnisfunktion bei kombination von funktion
und struktur im System?
* Gute Frage, die Trennung in (zustandslose) Komponente und
  (zustandsbehaftete) Objekte lässt sich nicht ohne Weiteres durchhalten, wenn
  man auf den Werkzeugmaschinenbau schaut, denn dort sind ja Komponenten die
  _nützlichen Produkte_.

### Weitere Anmerkungen

[09:58] Immanuel Thoke : die Symmetriebrechung kommt denke ich daher, dass
sich die Funktion der ENF nicht auf übergeordnete Wirkprinzipien reduzieren
lässt, meine mehrperiodischen PNF-Invarianten mehr, sondern höchstens
quasiperiodische Zyklen mit fraktaler Dimension und Veränderung der
Grenzzyklen

[10:05] Tom Strempel : Quasi das Halteproblem technischer Systeme

[10:10] Tom Strempel : Ich finde die "Evolution" hier beschreibt eher die
"kirchliche" Interpretation der biologischen Evolution, d. h. eine geleitete
Evolution, anstatt der realen natürlichen Evolution.  Den Evolutionsbegriff
sollte man da aus meiner Sicht etwas schärfen.
* Darüber ging bereits mehrfach die Debatte. Ich denke, dass der Begriff
  _Entwicklung_ für die Einbeziehung einer historisierenden
  Betrachtungsperspektive vollkommen ausreicht.  Siehe dazu auch
  <http://temm.ru/en/> für Ansätze von Rubin und Murashkovsky. 
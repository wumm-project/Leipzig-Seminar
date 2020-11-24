# Seminar am 24.11.2020

__Thema:__ Evolution Technischer Systeme bei D. Zobel

Diskussionsleitung: Karim Rakia, Sabine Lautenschläger

## Ankündigung

* Nur als [Folien](EvolutionTS_DrZobel.pdf).
* [Folien von Sabine Lautenschläger](Lautenschlaeger-20201124.pdf)

## Literatur 

* Dietmar Zobel (2007). Kreatives Arbeiten. Expert Verlag, Renningen.
  Abschnitt 3.3.3.
* Dietmar Zobel (2020). TRIZ für alle. Expert Verlag, Renningen. Abschnitt
  3.4.
* Dietmar Zobel, Rainer Hartmann (2009). Erfindungsmuster. Expert Verlag,
  Renningen. Abschnitt 3.3.
* Dietmar Zobel (2020a).  Beiträge zur Weiterentwicklung der TRIZ.  LIFIS
  Online, 19.01.2020.
  * <http://dx.doi.org/10.14625/zobel_20200119>

## Kommentierter Chat

### Bei Dietmar Zobel wird ein neues Gesetz formuliert

> Die Funktionssicherheit eines Systems wird primär nicht durch konstruktive
> Gesichtspunkte, sondern durch die sich aus dem Verfahrens-Funktions-Prinzip
> ergebenden Notwendigkeiten bestimmt.

[10:36] S. Lautenschläger : Für mich wäre nochmal zu diskutieren, was das Neue
an dem genannten Gesetz von Herrn Zobel ist, inwiefern wurde es bisher nicht
abgedeckt? Sei es durch andere Gesetze oder den ARIZ.

graebe : Das neue Gesetz ist eines der nichtfunktionalen Qualität, gut bekannt
aus dem Softwarequalitätsmanagement.  Es wird festgestellt, dass
Funktionssicherheit mehr durch die Ablauforganisation als durch die
Aufbauorganisation bestimmt ist.  Mit der PNF stehen in der TRIZ aber
funktionale Konzepte im Vordergrund, nichtfunktionale Eigenschaften (die
insbesondere für den Betrieb von TS wichtig sind), kommen so gut wie nicht
vor.  In der aktuellen
[SQuaRE-Norm](https://www.enzyklopaedie-der-wirtschaftsinformatik.de/wi-enzyklopaedie/lexikon/is-management/Systementwicklung/Management-der-Systementwicklung/Software-Qualitatsmanagement/Qualitatsmerkmale-von-Software/index.html)
für Software- und Systemqualität ist nur einer der 8 Bereiche den funktionalen
Anforderungen gewidmet.  Hier wird ein Defizit des TRIZ-Mainstreams deutlich -
man nimmt so gut wie keine Ansätze selbst aus benachbarten Bereichen der
Ingenieurtechnik zur Kenntnis.  

### Fokus auf TRIZ-Prinzipien

Was bedeutet der Fokus auf TRIZ-_Prinzipien_ in unserem Bemühen, die _Gesetze_
der Entwicklung technischer Systeme besser zu verstehen?

TRIZ-"Prinzipien" sind eigentlich "best practices" (im Russischen "Prijom").
Die TRIZ enthält weitere Werkzeuge (Separationsprinzipien, Katalog der
naturgesetzlichen Effekte, Katalog der Standardlösungen in 5 Lösungsklassen,
SF-Modellierung), die ebenfalls in die Kategorie der "best practices" gehören
in dem Sinne, dass es dumm ist, diese Design-Prinzipien beim Entwurf konkreter
technischer Systeme nicht zu berücksichtigen.

In (Gräbe 2020) wird argumentiert, dass die Entwicklungsgesetze in diesem
Sinne auch "best practices" sind, da sie handlungsleitend (auf verschiedenen
Abstraktionsstufen) für den Designer (und Betreiber) von technischen Systemen
sein sollten.  Gesetze haben dagegen eine gewisse "analytische" Qualität, aber
das haben aus der Erfahrung gewonnene "best practices" auch.  Gesetze sollten
allerdings nicht nur induktiv als Erfahrungstatbestände systematisiert werden,
sondern auch deduktiv in umfassendere Theoriezusammenhänge eingeordnet
werden.

Es bleibt nach wie vor die Frage zu diskutieren, in welche allgemeineren
Theoriezusammenhänge bis hin zu sehr allgemeinen philosophischen
Zusammenhängen sich derartige "best practices" einordnen lassen.  In den
Folien von Sabine Lautenschläger heißt es dazu (Zitat aus Zobel)

> In der neuesten TRIZ-Literatur wurde und wird viel zu wenig berücksichtigt,
> dass TRIZ im Grunde auf der Hegelschen Dialektik beruht (These - Antithese -
> Synthese). Daraus ergibt sich, dass im Prinzip auf allen Gebieten, auch den
> eindeutig nicht-technischen, das „TRIZ-Denken“ eine erhebliche Rolle spielen
> müsste. An Beispielen habe ich belegt, dass dies der Fall ist, ohne dass
> dies den jeweiligen Akteuren, insbesondere den Künstlern, unbedingt bewusst
> ist. Kreative Lösungen, unabhängig vom betrachteten Gebiet, sind jedoch
> immer dann besonders überzeugend bzw. anregend, wenn sie einen inneren
> Widerspruch und dessen überraschende Lösung erkennen lassen. ...

Das wurde nicht weiter diskutiert und soll beim nächsten Mal auf der Basis
eines Impulsbeitrags von Nadine Schumann noch einmal aufgenommen werden.

In den konkreten Beispielen aus dem SW-Engineering im Vortrag von Karim Rakia
kam ein anderer Geschichtspunkt zum Ausdruck: Das "Spiegeln" dieser
allgemeineren Prinzipien in immer wieder neuen Beispielen des Designs
technischer Systeme.

### Historische Betrachtungsweise

Die historische Entwicklung technischer Systeme ist für die Begründung der
"Gesetze" wie auch für Altschuller insgesamt (Altschuller 1979/83, S. 23) eine
der wichtigsten argumentativen Quellen. Das wird auch in (Zobel 2020,
Abschnitt 3.4) als "historische Methode" betont, im Seminar aber nur auf den
Folien 5 und 6 von Sabine Lautenschläger mit der 9-Felder-Matrix und deren
Verallgemeinerung im Managementbereich thematisiert. 

Die "historische Methode" ist keine Erfindung der TRIZ, sondern wird von
dieser angewendet, allerdings umfassender im _TRIZ-Systemoperator_, von dem
die "9-Felder-Matrix" eine ähnliche Verkürzung darstellt wie die Reduktion der
Anwendung der TRIZ-Prinzipien auf das Auslesen der Widerspruchsmatrix.

Dazu etwa <https://wumm-project.github.io/2020-11-03>. Das wurde aber nicht
weiter diksutiert.

### Systemische Entwicklung von System und Obersystem

[09:57] Immanuel Thoke : Frage wäre auch wieder, inwiefern TRIZ auf sich selbst
anwendbar ist. Das Verfahrens-Funktions-Prinzip von Zobel deutet, denke ich ein
wenig auf dieses Problem hin (Wie Prof. Gräbe auch anmerkt Funktionssicherheit
priorisiere Ablauforganisation), inwiefern technische Prinzipien hinreichend
sind, um die Prozessierung des Verfahrens der Entwicklung des Systems und
dessen Kontext zu interpolieren. Der Pfad des idealen Endresultat ist a priori
sicher eine intraspektive Entwicklungslinie, kann allerdings mittels des
Prinzip des Übergangs zum Obersystem insofern auf sich selbst angewendet
werden, als dass in diesem Moment der Kontext aktualisiert wird und neue
Idealitätsbedingungen integriert werden können und somit eine nicht-lineare
Entwicklung anstößt. 

* Das steht in deutlichem Widerspruch zu meiner Position in der Vorlesung:
  Dort führe ich aus, dass jedes System sowohl eine _Ideallinie_ als auch eine
  _Reallinie_ hat, die sich beide aus der systemspezifischen "Reduktion auf
  Wesentliches" ergeben. (Mit der Reallinie ist es etwas komplizierter, da wir
  zum Vergleich ebenfalls eine Beschreibungsform brauchen, deshalb dort
  "System, wie es geworden ist"). Das ist nicht "intraspektiv" (was das auch
  sein soll), sondern ein _äußeres_ methodisches Prinzip, das auf konkrete
  Modellierungssituationen angewendet wird. Bei den dabei zu Tage tretenden
  "Pfaden" (können nur die _Ideallinien_ sein) von System und Obersystem gibt
  es aber - auf Grund der verschiedenen "Reduktionen auf Wesentliches" -
  zunächst keinen logischen Zusammenhang. In jedem der beiden Systeme taucht
  das andere nur als "Komponente" (bzw. "Nachbarsystem") mit seiner
  Spezifikation auf und damit dem _Postulat_ des Zusammenfallens von Ideal-
  und Reallinie (des Verhaltens dieser importierten Komponente).  Das Ganze
  kann erst submersiv in einem weitere System aufgelöst werden, in dem dann
  _beide_ Entwicklungslinien thematisiert werden können. Erst _das_ bildet die
  Basis für Koevolutionsargumente.  Ich gebe allerdings zu, dass das in meinem
  Modell einer "Welt technischer Systeme" noch gar nicht vorkommt, da das neu
  zu konstituierende System zwei Komponenten enthält, wobei die eine
  "Komponente" der anderen und die andere "Nachbarsystem" (nicht Umwelt, denn
  dann wäre kein Platz mehr für das neu zu konstituierende System!) der einen
  ist.

### TRIZ ist mehr als die Widerspruchsmatrix

[10:04] graebe : Die Widerspruchsmatrix wurde bereits von Altschuller selbst
in den 1970er Jahren gegenüber engeren Schülern kritisiert.  Dazu Leonid Shub
<https://wumm-project.github.io/Texts/Shub-2006.pdf>. 

[10:14] graebe : Folie 32: Das wird in der SF-Modellierung systematischer
vorangetrieben.

[10:11] graebe : Folie 22: TRIZ selbst geht auch weiter: Theorie der
Entwicklung des kreativen Vorstellungvermögens usw. Dazu
* A. Kuryan, M. Rubin, N. Shchedrin, O. Eckardt, N. Rubina. TRIZ Ontology.
  Current State and Perspectives. TDS 2020.
  * <https://wumm-project.github.io/Texts/Ontology-TDS2020-en.pdf>
* A. Kuryan, V. Souchkov, D. Kucharavy. Towards ontology of TRIZ. Proceedings
  of TRIZ Developers Summit 2019 Conference, Minsk, 2019.
  * <https://wumm-project.github.io/Texts/Ontology-TDS2019-en.pdf>

### Das "Von-Selbst-Prinzip"

[10:14] Immanuel Thoke : Selbstversorgung trotzdem abhängig von Infrastruktur?
(Was ist das Selbst?)

* In der 11. Feuerbachthese postuliert Karl Marx: "Die Philosophen haben die
  Welt nur verschieden interpretiert, es kommt darauf an, sie zu verändern."
  Was aber heißt es, eine Welt zu verändern, die sich selbst auch dauernd
  ändert? Heißt das nicht, dass der Anspruch besteht, das Ändern der Welt zu
  ändern? Das Von-Selbst-Prinzip verstehe ich so, dass Ziele erreicht werden
  ohne das Ändern der Welt zu ändern (öder möglichst minimal).  

[10:17] graebe : Ist Software nicht per se "von selbst"? Und ist das nicht
identisch mit dem "Gesetz der Verdrängung des Menschen aus TS"?

* Diese Frage wurde nicht weiter aufgenommen. Wäre natürlich sehr spannend
  gewesen - in welchem Umfang fällt das "Von-Selbst-Prinzip" mit
  Automatisierung zusammen und was machen wir mit den Änderungen (etwa der
  Denktätigkeit), die vorab erforderlich waren, damit das Ganze "Von-Selbst"
  funktioniert?  

### Prinzip der Funktionsumkehr

[10:19] graebe : Effekt und Umkehreffekt treten aber nicht gleichzeitig auf?

[10:20] graebe : Umkehren von Axiomen/Paradigmen findet aber auf höheren
Stufen der Abstraktion statt.

* Hier ging es um das Prinzip der Funktionsumkehr. Zobel schlägt vor, dass
  jeder Erfinder, der ein bestimmtes Wirkungs-Funktions-Prinzip zur Lösung
  einer konkreten Aufgabe "erfunden" hat, nicht nur darüber nachdenken soll,
  für welche Aufgaben dieses neue Prinzip noch angewendet werden kann, sondern
  auch darüber, wo das Umkehrprinzip angewendet werden kann. 
* Dahinter steht folgende Überlegung: Beides geht über den "Stand der Technik"
  hinaus. Das Funktions-Prinzip (etwa der Kasimir-Effekt) kann nicht
  patentiert werden, wohl aber die Anwendung des Funktions-Prinzips auf
  konkrete Probleme. Deshalb ist es sinnvoll, in dieser zweiten Phase das Feld
  nach weiteren Anwendungen abzugrasen, wo das neue Funktions-Prinzip alte,
  bisher nicht gelöste Widersprüche lösen kann. Erfinder machen das
  üblicherweise nur für das direkte Prinzip, sehr selten für das
  Umkehrprinzip, so Zobels Beobachtung.  Dabei führt die Analyse der
  Anwendbarkeit des Umkehrprinzips auch schnell auf eine Explizierung von
  Kontextbedingungen der Anwendung des Prinzips selbst.
* Es gibt weitere TRIZ-Prinzipien und -Konzepte in dieser Richtung ("vorherige
  Wirkung", "vorherige Gegenwirkung", "Antisystem" im Systemoperator ...), die
  zeigen, dass es sinnvoll ist, Wirkungen dialektisch zu betrachten und die
  Schritte "These - Antithese - Synthese" zügig zu gehen, wenn man das einmal
  verstanden hat.  Angewendet auf die TRIZ und insbesondere die
  Entwicklungsgesetze, ist aber davon auszugehen, dass jedes dieser Gesetze
  mit seinem Gegenteil schwanger geht. Ich habe das in (Gräbe 2020) am
  Beispiel des "Prinzips der Ablösung mechanischer Wirkschemata" diskutiert,
  das im Zuge einer Revolution der Materialwissenschaften und der massenhaften
  Verfügbarkeit von Klettverschlüssen in machen Einsatzbereichen (Baumarkt) in
  sein Gegenteil umschlägt. Dabei wird auch deutlich, warum das frühere
  Prinzip eine gewisse Zeit dominant war - das hing mit der massiven
  Verfügbarkeit neuer elektronischer Steuerungen zusammen.

[10:22] Daniel : gleichzeitiges Auftreten vll. nicht in der gleichen Materie,
aber in einem System z.B. Transformator kann doch Effekt und Umkehr
gleichzeitig genutzt werden.

* Verstehe ich nicht. Funktion ist Wechselstrom einer Spannung in Wechselstrom
  einer anderen Spannung zu transformieren. Was ist die Umkehrfunktion? Ein
  dem nahes Beispiel wären Wechselrichter (an der Foto-Voltaikanlage) und
  Gleichrichter (im USB-Ladekabel). 

[10:27] Nadine : ich hätte nochmal eine Frage zum Verhältnis von
Trizprinzipien und Standardlösungen/Separationsprinzipien?

* Das wird Thema im nächsten Seminar sein.

[10:36] Immanuel Thoke : Das ist ja auch das Wesen von Managementprinzipien:
Sortierung von Prioritäten nach möglichst "objektiven" Kriterien (entsprechend
des Kontexts)

[10:48] Bingqing Hu : Es gibt mir den Eindruck, dass die Evolution technischer
System nach Information System geht.

* Was "information system" auch immer meint. Dazu der in der Vorlesung noch zu
  entwickelnde Informationsbegriff, der das Phänomen "Konzertbeispiel" aus
  (Gräbe 2020) umfassen muss.  In der TRIZ existieren (auch) hierzu zu großen
  Teilen Vorstellungen und Begrifflichkeiten der 1960er Jahre vor. Dazu etwa
  die Debatte um "flow of information" unter
  <https://wumm-project.github.io/2020-10-27>.

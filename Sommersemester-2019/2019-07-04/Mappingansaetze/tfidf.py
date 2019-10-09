#!/usr/bin/python3
# -*- coding: utf-8 -*-
from stop_words import get_stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
from data.trizprinciples import methoden, methods


def tfidf(text, compareset, stopwords):
    vect = TfidfVectorizer(min_df = 1, stop_words = stopwords)
    tfidf = vect.fit_transform([text] + compareset)
    return((tfidf * tfidf.T).A[0][1:])

if __name__ == '__main__':
    abstract_de_1 = """Zigaretten-Gruppen (11) sind innerhalb einer als Klapp­schachtel ausgebildeten Zigaretten-Packung durch einen Innen­zuschnitt (16) aus Stanniol oder dgl. umhüllt. Für die erleich­terte Entnahme von Zigaretten (12) ist der Innenzuschnitt (16) mit einem infolge von Stanzlinien (27) abziehbaren Lappen (26) - Flap - versehen. Zur weiteren Erleichterung der Entnahme von Zigaretten (12) ist der Innenzuschnitt (16) durch Seitenstanzlinien (31, 32) mit einem Aushebestreifen (30) versehen, der das Anheben einer Anzahl von Zigaretten (12) zur Entnahme derselben ermög­licht. Der Aushebestreifen (30) erstreckt sich mit einer Griff­lasche (34) in den Bereich des Lappens (26). Wird dieser abge­zogen, kommt die Grifflasche (34) frei, derart, daß sie aus der geöffneten Zigaretten-Packung herausragt und von Hand erfaßt werden kann. Der Aushebestreifen (30) ist dauerhaft mit dem Innenzuschnitt (16) verbunden als Teil desselben."""    
    print(tfidf(abstract_de_1, methoden, get_stop_words('de')))
    
    #abstract_de_2 = """1. Aufzuganlage mit einer Fahrstuhl-Kabine (1; 1'), einem Gegengewicht (6; 6') und einem Fahr-Schacht, in welchem sich die Kabine und das Gegengewicht bewegen, mit sich über die Länge des Schacts ersterckenden Schienen (2; 2'; 7; 7'), einem vom Gegengewicht getragenen Stator eines Linearinduktionsmotors (8; 8'), einer Einrichtung zum Speisen des Motors (mit Strom), einer Seilrolle (4, 5; 4') am oberen Ende des Schachts, (und) einem über die Seilrolle geführten und die Kabine mit dem Gegengewicht verbindenden (Trag-)Seil (3; 3'), wobei die Schienen zusätzlich als Motoranker wirken, gekennzeichnet durch eine Batterie (9; 9'), einen von der Batterie gespeisten Wechselrichter (10; 10') zur Lieferung von Energie oder Strom für den Motoranker, (und) eine Einrichtung (11; 11') zum Laden der Batterie, sowie dadurch, daß der Wechselrichter und die Batterie im Gegengewicht (6; 6') untergebracht sind."""
    #print(tfidf(abstract_de_2, methoden, get_stop_words('de')))
    
    #print(tfidf(abstract_en_1, methods, get_stop_words('en')))
    #abstract_en_1 = """Known conventional cigarette packs, especially those with a hinge-lid box (10), an inner blank (29) made of tin-foil and possibly an outer wrapping made of plastics foil, are not suitable for disposing of smoked cigarettes (waste-cigarettes 48). It is felt to be undesirable that smoked cigarettes be thrown away individually. This is especially true for "artificial cigarettes" which have recently appeared on the market. In order to achieve an improved waste-disposal, the present cigarette pack, especially as regards its embodiment with a hinge-lid box (10), is provided with a waste compartment (47) for holding waste-cigarettes (48). Park of the inner blank (28), namely its rear-wall (30), forms a partition between the waste compartment (47) and a cigarette compartment (46). Smoked cigarettes are reinserted into the pack through an insert-opening (54)."""
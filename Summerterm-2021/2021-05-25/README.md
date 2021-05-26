# Seminar on 25 May 2021

## Short Announcement

* __Theme:__  Business Process Definition Metamodel &ndash; BPDM
* __Presenter:__ B.D.

## Abstract

To be able to manage a processes within an organization it is necessary to be
able to describe the process in an unambiguous way. This enables the
comparison of different processes without actually implementing them. This in
turn is necessary to distinguish between desirable and undesirable
modifications to this process. Different metamodels are applicable like petri
networks, UML-activity diagrams or event-driven process chain charts. One of
the more common metamodels used for this application are BPMN models. To
enable automated translation from one metamodel into another and improve
cross-organizational communication about business processes the Business
Process Definition Metamodel (BPDM) was created. The idea behind BPDM is to
define a very extensive set of concepts so that other modeling tools can
easily be implemented in a compatible way by providing mappings from their own
modeling language to the concepts of BPDM.

## Material

* [Handout](Handout.pdf)


## Notes

tba


##  From the Chat


[09:27] Kleemann : also for later: connection atom model?

Graebe, Hans-Gert :

_ How does the business process (BP) concept fit with our systems approach?

_ GP and GP instance - system template and real-world system?  

- Why can GP be managed? Only GP instances are in motion (?)

- Does GP exist other than in model form?

- Model, system, representative of a complicated original - how does this
  relate to our concept of system?

_ Model depends on purpose. Where does purpose come from?

- Metamodel - how is modelling related to language? What is language? Where
  does language come from?

- Slide 4: How are the GP model and GP related? The two in the company talking
  ("first phase"), are they talking about GP or GP model?

- Slide 6: Is it about GP or GP model? BPMN metamodel consists of the
  different "boxes".  How does it relate to other GP?

- Essential elements of BPMN (model?): Activities, Gateways, Events (slide 7),
  Flows (slide 8), Pools, Lanes (slide 9 - areas of responsibility), Artefacts
  (slide 10 - resources?), Annotations (comments).

- What about "process" and GP instance, paths, critical paths? 

- How do "artefacts" feed into the GP? Where do they come from? Don't they
  have to be produced as well? How do they attach to both nodes (GP) and
  arrows (flow between GP)?

- How are GP models and domain knowledge related? (Explanation to slide 10)

- "Register incoming goods" - different names for the same thing.  Is solved
  in ontology models by URIs ("digital identities").

- Slide 11: BPDM as meta-meta-model as language to compare meta-models?  Then
  also meta-model = language for comparing models?

- What are the essential elements of the BPDM model? What is the relationship
  to the meta-models? Why "mapping"? Isn't BPDM simply a common glossary for
  _all_ GP metamodels? So more like "embedding" the terminologies?  How does
  this relate to the notion of "language binding" that is common in computer
  science?

- Historically (slide 17), one can see the intensive effort to agree on a
  common language as well. BPMN and BPDM are stages on this path. How are the
  levels of abstraction related to each other?

- Daniel Werner : How exactly does BPDM work in modelling these metamodels?
  Similar to BPMN using graphical elements or via languages like XML?

- Jannis de Riz : the instance can be managed or not?

- Daniel Werner : Maybe BPDM is more about administration and less about
  managing processes? Especially since "managing" is sometimes translated as
  "administering"?

- Daniel Werner : BPMN is ultimately just an extension of classical activity
  diagrams, I would argue.
  - Ralf Laue : The only difference is that UML AD never had its execution
    semantics defined in a sensible way (there are nice papers by Harald
    Störrle on this).


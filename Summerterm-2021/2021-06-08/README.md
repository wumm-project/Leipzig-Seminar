# Seminar on 08 June 2021

## Short Announcement

* __Theme:__  Goal-Models and the i* Modelling Method
* __Presenter:__ Marie Windhorst

## Abstract

One problem with goals is, that often they are not expressed directly, but
more often indirect or informally. A possible approach to identify goals is to
analyze the current system and use it as a source to identify goals. Having a
closer look a the current state of the system might end up in a list of
problems, and simply turning the problems around can provide in a list of
goals to be achieved for the system-to-be.

There are several modelling languages that help to analyze, conceptualize and
model the requirements of a system to be developed or transformed. Some of the
well known goal oriented modelling languages are KAOS and i*. The modelling
language i* (pronounced iStar) was developed by Yu. It is based on the goal
modelling approach, but takes it as a starting point for an agent-oriented
modelling language.

## Material

* [Handout](Handout.pdf)
* [Slides](Slides.pdf)

## Notes

##  From the Chat

Marie Windhorst : <https://www.cin.ufpe.br/~jhcp/pistar/tool/#>
- This is the link for a little tutorial, for everyone who wants to join :)
  Would be great if we could make it active and together :) But don't worry, I
  won't ask too complicated questions ;)
- Don't be surprised, when you open the link a model is already available,
  just go to File and load a new model.
  
Graebe, Hans-Gert :

- How are these approaches related to Design Thinking?
  - Kleemann : The combination of customer orientation and iterative process
    is what makes DT work, isn't it?
  - Ralf: DT is just a big hype on methods well known in RE. Also other RE
    methods are oriented on the needs of customers, possibly not so rigorous
    as DT.
  - HGG: Agent orientation and customer orientation are very different
    approaches. The former takes the "third party" as active prosumer, the
    latter as partner who is "served".  This requires very different
    management modes.

- What are agents? How are agents related to action spaces and the delineation
  of components? Can agents also be cooperative agents?
  - Reference to ProHEAL and the ABER matrix.

- What is the difference between active and passive components?  Isn't  a
  "passive" component (without output) meaningless?

- Goal -> Requirement. Does this hava any relation to model or system
  transformation (see lecture)? Black Box vs. White Box?

- GORE - does it have anything to do with TRIZ development laws (completeness,
  energy flow through all components ...)?

  - Kleemann : Another question about the process character of goal oriented
    RE. Isn't it a very linear and step-like process?

- i*: The whole thing has a lot of parallels with RDF graphs and an ontology
  editor. What is the exact connection?
  - Slide 13: Is there an RDF realisation as ontology for this taxonomy?
  - No, this was not found in the literature.

- Slide 12: The structure has a lot of similarity to Root Cause Analysis in
  TRIZ, but also to a hierarchical component model (structural design)? It
  also looks like a flow chart?

- Slide 12: Refining goals means a division of actions into activities in the
  sense of MBO?

- Slide 14: Are tasks always just leaves in the DAG? On slide 16 it didn't
  look like that. What is the difference between goals and tasks? What is the
  concept of resources? Is a distinction made between resource descriptions
  and resource assignments? Aren't resources also a "dependees"?

- Kleemann : how is the environment determined, only by the external situation?

- Marie Windhorst : WHY is also referred to as THE question by Yu, from which
  modelling takes place

- Kleemann : aren't we back to the problem of iterative processing with goal
  and task adaptation?

- Daniel Werner : Don't the arrow directions also give a certain hierarchy?
  Goals have tasks as children, etc. The tasks, for example, at the end of the
  arrows ("from bottom to top") are then more general/important than the
  sub-tasks. For example, one could use a score system (analogous to graph
  analysis) to give AND arrows a higher score than OR arrows and thus
  propagate a score through to the root.

- Ralf Laue : Absolutely correct. There is good work by Jennifer Horkoff on
  the algorithm of "propagating through" and thereby scoring.

- Marie Windhorst :
  <https://www.researchgate.net/publication/319482801_Does_Goal-Oriented_Requirements_Engineering_Achieve_Its_Goal>

- Sabine Lautenschläger: The approaches/instruments are the same for us (in
  socio-ecological modelling). The usage and meaning of the term _goal_ is or
  should be different: a sustainability goal always initially arises as a
  _coordination process_ between different actors and cannot initially be set
  as a specific goal of a technical development, as discussed in the seminar.
  Even if sustainability goals are often (blindly) defined in such a way in
  practice.  Sustainability goals serve to coordinate, prioritise and as
  guidelines; as soon as they become a "goal" in the sense of the approach
  discussed today in the seminar, one has to be cautious.  As far as
  "modelling" is concerned, it has been used so far more for description than
  for design purposes (yet!?), except of course in the design e.g. of
  environmental facilities. Both aspects are, of course, colsely related.
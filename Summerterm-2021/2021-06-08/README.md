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

### Systemic Structuring Processes. Theory and Practice

Systemic concepts have proven themselves useful in engineering applications
and are the basis of the design of technical systems from components.
Systemic concepts are thus the core of systematic innovation methodologies
such as TRIZ. They allow to delimit different levels of analysis and synthesis
on the one hand and on the other to connect them alternating black box and
white box modes. The dialectical conceptual pair of _system_ and _context_
plays a central role here.

The mental systemic structure of analysis and synthesis as forms of
description has a clear influence also on the _practical_ structuring of the
world as "reality for us". Systemically based forms of reflection are
transferred to real-world structures in the course of action, even if in this
process "the material" offers more or less "resistance" based on own laws of
motion.  Thus the establishing form of relationship in this process is to be
understood as a dialectically shaped co-evolutionary relationship. Such
co-evolutionary relationships between real-world and reflexive processes of
formation of structure are in no way a privilege of anthropomorphic action,
but are typical for coupled flow equilibria in other developed, metabolising
biological systems as well.

### Structural, Functional and Processual Systemic Forms of Description

Engineering approaches in general and TRIZ in particular have difficulties in
switching from structural and functional to processual forms of description.
For example, TRIZ knows a larger selection of function-oriented methods and
tools, but flow-oriented approaches are weak developed. This has much to do
with the fact that systemic composition methods can exploit functional
specifications of interfaces, but in rare cases processual performance
parameters are specified as interfaces. Such imbalances are also widespread in
computer science - functional tests start early in integration scenarios in
software testing, including the use of test drivers and mock objects, which
are _functionally_ designed, whereas load, stress and performance tests
usually only start at the system test level.

### Systemic Approaches in Engineering and Management

The central aim of our seminar is to identify systemic approaches in different
management theories and to investigate which parallels and differences exist
between engineering and management action. We established that the context of
management action can be well captured with self-similar systemic approaches,
even if the associated hierarchical scaling approach remains underexposed in
most management theories.

The major management theories we have looked at so far focus on _practical_
management action. Descriptive forms and theoretical approaches are considered
merely as support and tools for this main focus. The context for such
management actions are systemically structured "living organisations"
(Shchedrovitsky) _in operating mode_. Thus the context of management action
differs fundamentally from engineering action, which - at least in the horizon
of the experience of most TRIZ practitioners - refers to systems in
_maintenance_ or even _design mode_. This is, however, only a provisional
demarcation, because the majority of engineers are _production engineers_ and
concerned as such with the _operating mode_ of large-scale technical systems.
Moreover, the maintenance mode of a technical system is part of the operating
mode of the (socio-technical) supersystem.

Embedding management action in an already _well developed systemically
structured real-world context_ and thus in an advanced structured "living
organisation" also makes sense under another aspect. We consider objectives,
rules and frameworks - including the authorisation of the managers themselves - 
as _given_ existing conditions of the management action and consequently
fade out the analysis of their historical genesis as part of a "reduction to
essentials".

From a TRIZ perspective, management in this sense is a _function_ of the
control component of the corresponding system. It remains open to what extent
this function can still be _personalised_ under modern technical conditions as
in classical management theories, if methodological knowledge (of the manager)
and deep domain-specific special knowledge (of the production engineer) are
both required for appropriate management. It is also open to what extent
management action under modern technical conditions can be primarily directed
at the inside of the system.  It may well be that division of management as in
SCRUM (between product owner, SCRUM master and team) are methodologically more
appropriate.

### i* Models and Business Process (BP) Modelling

The long introduction served primarily once again to mark the place of the
explanations on i* models in the presentation in the overall building. The
repeated comment that various of the discussed management approaches are of
academic interest only without significant practical application indicates
above all the multi-layered nature of the corresponding (interpersonal)
reflection structures of production, selection and self-regulating
dissemination of the corresponding explanatory patterns.

With an actor-centred view, i* models consistently implement the approach of
"areas of responsibility" (lane, performer role and actor in BPDM) built into
other BP models.  It is implemented in a more strict way as it points in the
direction of a systemic closure, in which a feedback loop between expectations
and experiences can be incorporated (not yet included in the i* concept). The
areas of action of the individual actors highlighted in grey in the i*
diagrams have many parallels to the concept of action spaces in the lecture.
Compared to classical management approaches, this requires a concept of
interaction _between_ such management areas and thus opens the door to
self-similar system concepts. It was not further addressed in the presentation
o what extent this is also realised in the current i* concept, i.e. if
system-supersystem structures are conceptualised. However, it must be taken
into account that the approach does not claim to be a complete BP modelling,
but focuses on requirements engineering and thus on a first phase of detailed
modelling.

i* modelling consists of two essentially different dimensions - the design of
_dependency relations_ between actor areas and the modelling of internals of
the "grey areas". From a systemic point of view, the former is comparable to
the black box specification of dependencies. On the one hand import and export
interfaces can be distinguished by specifying such couplings and directions,
and on the other hand not only the functional "what?" but also the causal "for
whom?"  is preserved. In modern component concepts in computer science, such
as the CORBA Component Model CCM [CCM], these import and export interfaces
play a central role as receptacles and facets, and the couplings are dropped
under the aspect of (broader) reuse in favour of a formal specification of the
interface.

Inside the "grey areas", process structures are modelled as directed graphs
from predefined building blocks. This models a white box approach, whereby it
remains unclear to what extent structural, functional and process-related
aspects are differentiated. In the examples given, the structuring of _goals_
- the central notion in an i* model - is used in all three ways. It is also
clear that the notions _task_ and _resource_ conceal further requirements (a
task must be implemented, a resource must be provided), which are not further
developed in the diagram. The distinction between these two types of (masked)
requirement was not discussed further in the presentation and discussion.

It remains to note that the approach goes beyond those considered so far in
one direction. It considers the interaction of independent third parties (the
actors) in a service area and thus _contractually bound management structures_
without a "central manager" with correspondingly authorised possibilities of
intervention. It remains open to what extent such modelling approaches are
typical for a service-oriented industry and whether or since when we are
really in a "service society" in which such economic relationships dominate.

* [CCM] Chapter 6 in <https://www.omg.org/spec/CCM/4.0/PDF>

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

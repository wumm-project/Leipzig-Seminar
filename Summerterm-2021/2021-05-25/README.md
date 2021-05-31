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

Presentation and discussion focused on a closer look at concepts, tools and
models for describing Business Processes (BP). This field has been massively
developing over the last 20 years. Characteristic for this development was its
embedding in an evolving cycle between development of appropriate concepts and
testing their practical suitability in applications in a co-operative process
of practice.  This clearly goes beyond the sometimes speculative
conceptualisations of Russell Ackoff or Peter Drucker.

The result is a development and consolidation process of the terminology
itself, which was illustrated in the presentation by means of the historical
development of various BP language systems (in addition to BPMN, ?? and EPK
were considered).  The need of cross-concept coordination processes for
_practical_ interoperability led to cooperate structures between the various
groups around the different emerging standards in a _Business Process
Management Initiative_ (BPMI, until 2005) and a _Business Modeling and
Integration Domain Task Force_ (BMI DTF, until 2008). Since 2008 the
standardisation was coordinated by the _Object Management Group_ (OMG).  In
this course, BPMN consolidated and is nowadays widely accepted as leading
standard, while the other alternatives lost importance.

BPDM emerged as the product (in TRIZ terms) of the process of formally fixing
the meaning of terms that had previously been used in the different standards
with a wider range of variation.

In this process, the cross-company infrastructural significance of such
descriptive systems becomes evident. Only on the basis of clearly agreed
models with a sufficient number of degrees of freedom (parameters)
cross-company workflows can be effectively coordinated. Only in such a
cross-company infrastructure digitally executable "smart contracts" will be
available for recurring and clearly defined business transactions. A similar
development is well known from computer science with the formalisation of
repeating functional sequences in function definitions.

The development path of the potential of the modelling language covers several
levels of maturity - from simple communication in concrete cooperations
(model) to the development of structured communication on the basis of
emerging common concepts (meta-model) to the (currently still informal)
development of the expressive capacity of that language itself at the level of
a meta-meta-model. This evolution illustrates once more the dynamic character
of the memo item "Meaning __is__ the use of terms" given in the lecture. See
also the parallels to the language development processes explained for the
concert example in the first lecture.

Ralf Laue justified the meanwhile dominant position of BPMN 2.0 with the fact
that it is the only standard that also defines a _process semantics_. This
aspect remains to be explored further, especially the significance and
position of such a process- and workflow-oriented _process semantics_ compared
to the taxonomically oriented concept formation processes of a _structural
semantics_ within the language development process compared. Process semantics
presuppose structural semantics, but the modelling focus is shifted from
static to dynamic models. It remains to be clarified to what extent the
required conceptual system can be understood as a simple extension of the
structural model or whether more fundamental qualitative changes in the
modelling itself need to be taken into account here (Shchedrovitsky: "You can
only manage systems that are in motion").

BPDM is part of that taxonomically oriented component of BPMN. This raises the
question of whether it is really out of date as claimed in the presentation or
it is an integral part of the established taxonomic-structural component of
that language universe that is now characterised by terms such as [BPMN, CMMN
and DMN](https://www.omg.org/intro/TripleCrown.pdf). In any case, Ralf Laue
pointed to such a shift of the front line of current concept formation
processes in the direction of variabilities of dynamic process description
schemes.

Let's consider as second aspect the relation of the presented BP concepts in
our systemic context.

The definition "A business process consists of a sequence of coordinated
activities. These are either tasks or subprocesses" clearly shows that we are
in the continuity of the concepts presented in the last seminar on MBO (action
and activity) and that the self-similarity of the approach still assumed there
(action as activity in a more comprehensive action) is now clearly
presupposed.

This allows to grasp the concepts of BP modelling in the described systemic
context. The main problem from the last seminar - the clear distinction
between design time and runtime of the respective systemic description - was
addressed rudimentarily in the presentation with the distinction between BP
and BP instance, but not developed consistently. The (simple) distinction
between class and instance (or object) from OO programming takes place on
another level, between _template_ and _specific expression_, both of which are
still forms of description.

This is already clear from the position of compiler and interpreter as tools -
as it is well known, that both are translators from a high-level language into
a machine language, input and output thus are in language form. Only the
_execution_ of that detailed programme _on a robot infrastructure_, for
example, has real-world consequences. The relationship of BP and BP instances
as a high-level and detailed description form of (potential) business
transactions to the _real_ business transactions themselves is similar. The
essential link between the two is the _solution of the resource question_,
without which the potentiality of the descriptive form cannot be transformed
into the reality of the form of execution. This fundamental question remained
unilluminated once more.

##  From the Chat

- Kleemann : also for later: connection atom model?

Graebe, Hans-Gert :

- How does the business process (BP) concept fit with our systems approach?
  - See the notes.

- Many conceptual questions concerning the relation and distinction between
  BP, BP instances and real-world business transaction remained vague.
  - BP and BP instance - system template and real-world system?  
  - Why can BP be managed?
    - This relates to Shchedrovitsky's claim "Only moving systems can be
      managed" and the need for a better distinction between decision
      preparation as process of planning and decision making as part of
      process execution.

- Does BP exist other than in model form?
  - At least BP Modelling is concerned only with models, since even the
    experienced results as first class source for convergence between model
    and practice cannot be processed without their transformation in language
    form.
  - Model, system, representative of a complicated original - how does this
    relate to our concept of system?

- Model depends on purpose. Where does purpose come from?

- Metamodel - how is modelling related to language? What is language? Where
  does language come from?

- Slide 4: How are the BP model and BP related? The two in the company talking
  ("first phase"), are they talking about BP or BP model?

- Slide 6: Is it about BP or BP model? BPMN metamodel consists of the
  different "boxes".  How does it relate to other BP?

- Essential elements of BPMN (model?): Activities, Gateways, Events (slide 7),
  Flows (slide 8), Pools, Lanes (slide 9 - areas of responsibility), Artefacts
  (slide 10 - resources?), Annotations (comments).
  - What about "process" and BP instance, paths, critical paths? 
  - How "artefacts" are included in a BP? Where do they come from? Don't they
    have to be produced or at least provided? How it is to be understood that
    they can be attached to both nodes (BP) and arrows (flow between BP)?
  - How are BP models and domain knowledge related? (Explanation to slide 10)

- Slide 11: BPDM as meta-meta-model as language to compare meta-models?  Then
  also meta-model = language for comparing models?

- What are the essential elements of the BPDM model? What is the relationship
  to the meta-models? Why "mapping"? Isn't BPDM simply a common glossary for
  _all_ BP metamodels? So more like "embedding" the terminologies?  How does
  this relate to the notion of "language binding" that is common in computer
  science?

- Historically (slide 17), one can see the intensive effort to agree on a
  common language as well. BPMN and BPDM are stages on this path. How are the
  levels of abstraction related to each other?

Daniel Werner :
- How exactly does BPDM work in modelling these metamodels?  Similar to BPMN
  using graphical elements or via languages like XML?
- Maybe BPDM is more about administration and less about managing processes?
  Especially since "managing" is sometimes translated as "administering"?
- BPMN is ultimately just an extension of classical activity diagrams, I would
  argue.
  - Ralf Laue : The only difference is that UML AD never had its execution
    semantics defined in a sensible way (there are nice papers by Harald
    Störrle on this).
  - BPDM is a _formal standard_ 
    - <https://www.omg.org/spec/BPDM/1.0/About-BPDM/#docs-normative-machine>

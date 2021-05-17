# On the concept of system in the theory of dynamic systems 

- Literature: (Prigogine/Stengers 1984)
- Additional reading: (Jantsch 1992)

## Issues in the theory of dynamical systems

- <https://en.wikipedia.org/wiki/Dynamical_system>
- <https://de.wikipedia.org/wiki/Dynamisches_System_(systems theory)>

## First examples

Examples in the homogeneous gravitational field

- __A single system__ - Pendulum: Known equation for trajectory, single
  equilibrium point (attractor). The pendulum moves in a plane according to
  the initial deflection (amplitude), its eigenfrequency omega depends only on
  the length of the suspension thread: omega=sqrt(g/l). The ideal pendulum
  swings forever, the real pendulum swings with damped amplitude in that plane
  around the equilibrium point.  
  - <https://en.wikipedia.org/wiki/Pendulum>
  - <https://de.wikipedia.org/wiki/Pendel>
  - The pendulum equation has a nice solution (of a linear o.d.e. of second
    order) only for small amplitudes x, if sin(x) can be replaced by x.
  - Note the effect of "Foucault's pendulum" - the moving plane is constant in
    space even if the earth rotates away underneath.
    - <https://en.wikipedia.org/wiki/Foucault_pendulum>

- __A single system__ - Magnetic Pendulum 1: Add a single repelling magnet,
  i.e. a single well defined force. The system has no more a single
  equilibrium point, but a whole circle of resting positions.  The real
  pendulum "chooses" one of that point for rest and already moves on a
  (seemingly) chaotic trajectory.
  - Note that the pendulum does no more swing in a plane, but the same is true
    for the ordinary pendulum, if there is an inertial force not in the
    pendulum plane. A little push from the side and also the ordinary pendulum
    "wobbles" around its rest position - but in a predictable way on a spiral
    trajectory.

- __A single system__ - Magnetic Pendulum 2: Add 3 attracting magnets forming
  an isoscele triangle around the center of the pendulum.  Three forces of the
  magnets "compete" for the pendulum, but as lng as the pendulum has "enough
  own energy" it can leave the "influence area" of one of the magnets in
  favour of another one.  The pendulum circles around one magnet for some time
  and then "jumps" to another to circle around that one too, until it gets
  "tired" and decides to remain at one magnet as an attractor.
  - <https://www.supermagnete.de/eng/Magnet-applications/Magnetic-pendulum>
  - <https://de.wikipedia.org/wiki/Magnetisches_Pendel>

- __Two interacting systems__ - Coupled Pendulum: Two equal pendulums (same
  eigenfrequencies, coupled with a rigid link on their suspensions). Each with
  "known behavior", a deterministic link organises "energy transfer" between,
  several forms of behavior are possible: swing in phase, in opposite phase,
  periodic energy transfer ...  
  - <https://en.wikipedia.org/wiki/Oscillation#Coupled_oscillations>
  - <https://de.wikipedia.org/wiki/Gekoppelte_Pendel>

- __Two interacting systems__ - Double pendulum: A pendulum (upper pendulum)
  is attached to the end of another pendulum (lower pendulum). During the
  permanent transformation of potential into kinetic energy and vice versa of
  the upper pendulum (with frequency depending only on the length of its
  suspension) some energy is "exchanged" with the lower pendulum since their
  frequencies differ.
  - <https://en.wikipedia.org/wiki/Double_pendulum>
  - <https://de.wikipedia.org/wiki/Doppelpendel>
  - The coupling changes from "being in phase" (transfer of energy from the
    upper to the lower pendulum, the upper pendulum "slows down", the lower
    pendulum "accelerates") to "being out of phase" (transfer of energy from
    the lower to the upper pendulum, the upper pendulum "accelerates", the
    lower perndulum "slows down").
  - Note nevertheless, that this "story" uses the language of the description
    of the (well understood) __single__ pendulum. The language may be
    completely inappropriate for emergent behavior of the coupled system.

  - Results in a _chaotic trajectory_ of the lower pendulum for large
    amplitudes and almost the same lengths of the suspensions (i.e. equal
    eigenfrequencies).

  - Note: For small amplitudes and large difference in the eigenfrequencies
    the systems tends to a behavior as a single pendulum with pendulum body in
    the mass centre of the system.  Both systems make an "agreement" about
    their energy transfer mode.

Examples with gravitational interaction
- Two-body problem
  - <https://en.wikipedia.org/wiki/Two-body_problem>
  - <https://de.wikipedia.org/wiki/Zweikörperproblem>
- Three-body problem
  - <https://en.wikipedia.org/wiki/Three-body_problem>
  - <https://de.wikipedia.org/wiki/Dreikörperproblem>
- KAM theory (Kolmogorow-Arnold-Moser-Theorem)

  - ... Quasiperiodic solutions can be close to each other, but unstable
    orbits can lie between them, so that in practice it cannot be decided
    whether one is on a stable or unstable orbit because of, for example,
    finite measurement accuracy. For the planetary system, it can be shown
    that the unstable orbits are much rarer than the stable ones.

These are already - necessarily reductionistic - description forms of reality:
for example, pendulums with and without damping.  But: Meaningful reductions
of forms of description __improve__ our understanding of the
interrelationships of the world.  If Galileo Galilei had not applied this
method of thinking he would never have noticed that iron and feather fall at
the same rate.

- Not everything that looks like chaos has to be chaotic:
  <https://i.redd.it/zr7tet9mdfl01.gif>

## Limit cycles and attractors

In most situations there is no single equilibrium position but several as in
the case of the pendulum with a single repelling magnet.
- Limit cycles
  - <https://en.wikipedia.org/wiki/Limit_cycle>
  - <https://de.wikipedia.org/wiki/Grenzzyklus>

In many cases the real movement f(t) in time is _attracted_ by that limit
cycle, i.e. f(t) can be decomposed into f(t)=l(t)+r(t) with l(t) the
projection on the limit cycle and r(t) a (small) orthogonal deviation.

When the body is on the limit cycle, it stays there, i.e. the limit cycle is a
_stable solution_ of the equations of motion of the system, called
__steady-state equilibrium__ or __attractor__.
- Attractor = stable solution of the corresponding system of diff. eq.
  - <https://en.wikipedia.org/wiki/Attractor>

The body moves along this path forever, mostly in a periodic motion. However,
the whole story is about the _description model_ (i.e. after a "reduction to
the essentials") and not necessarily about reality.  Management can, however,
mean keeping a system on such a path through small influences (small effort,
great effect).

On the importance of "stable" cyclical processes in nature. 

We are able to perceive such __approximately__ repeating patterns in natural
processes (i.e. attractors), i.e. also independently of mathematics achieve
such a reduction performance.

For given (deterministic) equations of motion one can compute the geometry of
such an attractor as __global deterministc__ invariant of the equations of
motion.

Question: How complicated can such attractors be?

- The Lorenz attractor
  - <https://en.wikipedia.org/wiki/Lorenz_system>
  - <https://de.wikipedia.org/wiki/Lorenz-Attraktor>
  - Attention, with the numerical methods used there for visualisation it is
    difficult to distinguish whether they are calculating a chaotic trajectory
    or really the attractor, which is a __global__ artefact.
  - "Almost all initial points will tend to an invariant set – the Lorenz
    attractor – a strange attractor, a fractal, and a self-excited attractor"
    (Wikipedia)

- Strange (or chaotic) Attractors
  - <https://en.wikipedia.org/wiki/Attractor#Strange_attractor>
  - <https://de.wikipedia.org/wiki/Seltsamer_Attraktor>
  - "final state of a dynamic process whose fractal dimension is non-integer
    and whose Kolmogorov entropy is genuinely positive. It is a fractal that
    cannot be described geometrically in closed form". (German Wikipedia)
  - A dynamic system with a chaotic attractor is locally unstable yet globally
    stable: once some sequences have entered the attractor, nearby points
    diverge from one another but never depart from the attractor.

__This means that the trajectory concept of classical physics is no longer
applicable to such phenomena__.  ("butterfly effect").

## Behavior of coupled systems on multiple time scales

- Predator-prey cycles
  - <https://de.wikipedia.org/wiki/Räuber-Beute-Beziehung>
  - <https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations>
  - <https://de.wikipedia.org/wiki/Lotka-Volterra-Regeln>

An important approach arises for systems whose dynamics run on different time
scales. As a further step of abstraction, one can then methodically first
investigate the dynamics on the individual time scales (investigating each of
the two systems separately) and later add the interactions between the time
scales in an extended model.  Massively new phenomena arise already when
__two__ time scales are considered, which is referred to as __micro- and
macroevolution__.

- Example: double pendulum with two very different length (and small
  deflection).
  - Hence eigenfrequencies are different, but the "upper" pendulum "injects"
    energy at different rates to the "lower" pendulum to force it in a
    "common" movement.
  - Although a double pendulum, the system is thus (finally) _not_ chaotic,
    but behaves like a simple pendulum with mass at its centre of gravity.
  
- Known in the literature as the "enslavement effect" and used especially in
  methodologically poorly founded sociological considerations as a verbal
  argument.

- But see https://de.wikipedia.org/wiki/Netzwerkforschung

What problems arise in piecing together (understood) microevolutions of
subsystems to an understanding of macro-level dynamics?

- Immersive and Submersive System Concepts (see lecture)
- The concepts of immersion and submersion in the category of vector bundles
  - <https://de.wikipedia.org/wiki/Submersion>
  - <https://de.wikipedia.org/wiki/Immersion_(Mathematics)>

  - <https://en.wikipedia.org/wiki/Submersion_(mathematics)>
  - <https://en.wikipedia.org/wiki/Immersion_(mathematics)>

## Emergent phenomena

"The whole is greater than the sum of its parts".  This __only__ applies to the
submersive system concept. 

- Nonlinear systems and Phase transitions
  - <https://en.wikipedia.org/wiki/Phase_transition>
  - <https://de.wikipedia.org/wiki/Phasenübergang>
- Self-organisation in dissipative structures
  - <https://en.wikipedia.org/wiki/Rayleigh%E2%80%93B%C3%A9nard_convection>
  - <https://en.wikipedia.org/wiki/Belousov%E2%80%93Zhabotinsky_reaction>

  - <https://de.wikipedia.org/wiki/Rayleigh-Bénard-Konvektion>
  - <https://de.wikipedia.org/wiki/Belousov-Zhabotinsky-Reaktion>
- Dissipative structures
- Temperature as an emergent phenomenon.
- Entropy and Enthalpy.
- Life on Earth as a dissipative system.


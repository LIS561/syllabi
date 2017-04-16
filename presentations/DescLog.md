---
title: Description Logics
author: Dave Dubin
date: April 17, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usepackage{mathabx}
---

# Description Logics
- Description logics (plural) are a family of artificial languages
  used in information modeling and knowledge representation.
- They are the logical foundations of ontology languages (such as OWL)
  that are used in deductive information management applications.
- An ontology can be understood as a set of declarations and
  constraints in a specific description logic such as $\mathcal{ALC}$
  or $\mathcal{SROIQ}$.
- Any description logic can be understood as a *decidable subset* of
  first order logic.

# Logic, computation, and decidability

- Decidability is a complex topic, but it's basically about our
  ability to use general-purpose algorithms to answer questions.
- In information processing applications, we're interested in
  questions about information we've collected in a database. In
  deductive applications, we care about more than just retrieving
  answers we've explicitly stored. Typically we store logical rules or
  definitions that act on individual facts and records. A typical
  query would be asking for a list of individuals that are instances
  of a specific class.
- The more things you can express in an artificial language, the more
  computational resources (time and memory) it takes to answer
  questions. Many interesting questions have no general way to answer
  them.
- Small expressive differences between languages make a huge
  difference in what kinds of questions are either too expensive or
  impossible to answer.
  
# Decidability, continued
- In logic, a typical question is whether some statement follows
  logically from a set of other statements, or whether its truth is at
  least consistent with those statements (i.e., that it could be
  true).
- Propositional logic is decidable, but general-purpose procedures for
  deduction are too expensive.
- Predicate logic is only semi-decidable. If a statement follows
  logically from a set of premises, we have algorithms that will
  verify that. But that can take a very long time, and if the
  statement does *not* follow, then our procedures may run forever
  without ever telling us that the answer is no.
- You can think of description logics as crippled versions of
  predicate logic. The expressive power has been restricted in order
  to guarantee that our questions are decidable, and that algorithms
  for answering our questions are usually efficient.

# Key differences: predicate logic vs. description logs

1. Description logics only have unary and binary predicates.
    - Just like Bach's fragment. Nothing like ${\forall}x{\forall}y{\exists}z\ Pxyz$ is allowed.
    - This is one reason why description logics are decidable.
    - We'll also see a convenient adaptation to the RDF model.
    - Unary predicates are called *concepts* (like RDF classes).
    - Binary predicates are called *roles* (like RDF properties).
2. Variables aren't explicit in syntax. Concepts have one and roles have two.
3. Reasoning about anonymous individuals is imited with description logics.
4. Description logic statements are understood to be divided into
   three categories:
    - Statements assigning individuals to concepts and roles are in the *ABox*.
    - Relationships among concepts are in the *TBox*.
    - Relationships among roles are in the *RBox*.

# Syntax used in description logics

Description Logic                                                                                       Predicate Logic
--------------------                                -------------------------------------------------------------------
$Mother(julia)$                                                                                                    $Mj$
$parentOf(julia, john)$                                                                                           $Pij$
$Mother \sqsubseteq Parent$                                                            ${\forall}x (Mx \rightarrow Px)$
$Person \equiv Human$                                                              ${\forall}x (Px \leftrightarrow Hx)$
$parentOf \sqsubseteq ancestorOf$                                          ${\forall}x{\forall}y (Pxy \rightarrow Axy)$
$brotherOf \circ parentOf \sqsubseteq uncleOf$      ${\forall}x{\forall}y{\forall}z ((Bxy \wedge Pyz) \rightarrow Uxz)$
$Female \sqcap Parent$                                                                                 $(Fx \wedge Px)$

Table: Correspondences between description logics and first order logic.

# More syntax examples

Description Logic                                                         Predicate Logic English
--------------------------------------  ------------------------------------------------- -----------------------------------------------------
$Father \sqcup Mother$                                                     $(Fx \vee Mx)$ \tiny Fathers or mothers \normalsize
$Female \sqcap {\neg}Married$                                      $(Fx \wedge {\neg}Mx)$ \tiny Unmarried females \normalsize
$\top \sqsubseteq Male \sqcup Female$                           ${\forall}x (Mx \vee Fx)$ \tiny Everything is either male or female \normalsize
$Male \sqcap Female \sqsubseteq \bot$                   ${\forall}x {\neg}(Mx \wedge Fx)$ \tiny Nothing is both male and female \normalsize
$Parent \equiv {\exists}parentOf.\top$  ${\forall}x (Px \leftrightarrow {\exists}yRxy)$   \tiny Parents are parents of something \normalsize
${\forall}parentOf.Female$                              ${\forall}y (Rxy \rightarrow Fy)$ \tiny Parents of only female children \normalsize
${\exists}sonOf.\top \sqsubseteq Male$       ${\forall}x ({\exists}y Sxy \rightarrow Mx)$ \tiny Sons of anything are male \normalsize
$\top \sqsubseteq {\forall}sonOf.Parent$      ${\forall}x{\forall}y (Sxy \rightarrow Px)$ \tiny You can only be son of a parent \normalsize

Table: Not all description logics let you use all these features.



# Existential quantification

- The existential quantifier in DLs has the same meaning as in
  predicate logic, but our ability to reason about anonymous individuals is limited.
- Suppose we define a native as someone who lives in the same country they were born in.
- In predicate logic we could express this definition as: ${\forall}x(Nx \leftrightarrow {\exists}y(Cy \wedge (Bxy \wedge Lxy)))$
- There's no way to capture this definition in a description logic. We can come close with classes connected via named individuals.
- For example:
   - $GermanResident \equiv {\exists}livesIn.\{germany\}$
   - $GermanBorn \equiv {\exists}bornIn.\{germany\}$
   - $GermanNative \equiv GermanResident \sqcap GermanBorn$

# Grammar for DLs


The grammar for a DL will provide most (but not all) of its expressive
constraints. $\mathcal{SROIQ}$, for example, has this grammar for
role and concept expressions and axioms, where $U$ is the universal role that
links all pairs of individuals, $n$ is the set of integers, and $N_{I}, N_{C}, N_{R}$
are sets of individual, concept, and role names, respectively:

- $R \Coloneqq U|N_{R}|N_{R}^{-}$
- $C \Coloneqq N_{C}|C \sqcup C|C \sqcap C|{\neg}C|\top|\bot|{\exists}R.C$
- $C \Coloneqq {\forall}R.C|{\geqslant}n\ R.C|{\leqslant}n\ R.C|{\exists}R.self|\{N_{I}\}$
- $ABox \Coloneqq C(N_{I})|R(N_{I},N_{I})|N_{I} \approx N_{I}|N_{I} \napprox N_{I}$
- $TBox \Coloneqq C \sqsubseteq C|C \equiv C$
- $RBox \Coloneqq R \sqsubseteq R|R \equiv R|R \circ R \sqsubseteq R|Disjoint(R,R)$
- $\varphi \Coloneqq ABox|TBox|RBox$

# DL Semantics

A DL interpretation $\mathcal{I} = {\langle}\Delta^{\mathcal{I}}, \cdot^{\mathcal{I}}{\rangle}$ where:

- $\Delta^{\mathcal{I}}$ is the domain set (Bach's $E$ and van
  Benthem's $D$).
- $\cdot^{\mathcal{I}}$ is the denotation function (Bach's $D$ and van
  Benthem's $I$). This function maps:
     - a concept $A \rightarrow A^{\mathcal{I}} \subseteq \Delta^{\mathcal{I}}$
     - a role $R \rightarrow R^{\mathcal{I}} \subseteq \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}}$
     - a name $a \rightarrow a^{\mathcal{I}} \in \Delta^{\mathcal{I}}$
- An interpretation *satisfies* a statement if it is true in
  that interpretation: $\mathcal{I}\ {\models}\ \varphi$.  
- An interpretation $\mathcal{I}$ satisfying every statement in a
  set $\mathcal{O}$, is a *model* of $\mathcal{O}$.
- If **at least one** model exists for a set of DL statements
  then those statements are *consistent.*

# Models and open world reasoning

- We're used to concluding that a proposition is false if we cannot
  demonstrate that it is true.
- That's because our systems are understood to contain complete
  information, and so any question for which we cannot demonstrate a
  yes answer must be answered no.
- But our decentralized, networked, and cooperative information
  systems increasingly rely on an *open world assumption.*
- The open world assumption is that not all relevant information is
  necessarily available. We ask whether any model of our statements
  exists (i.e., whether they're consistent).

# Open world reasoning example

- Suppose we assert that the individual Dave (class Person) stands in
  the $appointedPosition$ relationship to the individual
  research_associate_professor:
  $Person(dave) \sqcap appointedPosition(dave,research\_associate\_professor)$

- Suppose that we also assert that the domain of $appointedPosition$
  is the concept $Appointment$: ${\exists}appointedPosition.\top \sqsubseteq Appointment$

- In a conventional database application we'd expect an error unless
  Dave matches the domain constraint.

- But unless persons and appointments are specifically modeled as disjoint, there
  exist interpretations in which Dave belongs to both classes.

- In knowledge-based applications, domain rules offer sanity checks on our data.






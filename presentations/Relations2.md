---
title: Formalization of relationships
author: Dave Dubin
date: February, 2019
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# Tonight
- Earlier we considered Jubien's definition of property: "a way that something can be."
- Anything in the domain we're modeling that exhibits the property is an *instance* of the property.
- We'll discuss how we can use sets to model properties and relationships, even
  though a property will be different than the set that is its
  *extension*.

# From our syllabus

The course is thus simultaneously a foundations course
and a survey course. There are several important cross-cutting
themes:

- Data independence through abstraction.
- The interdefinability of fundamental modeling constructs.
- Deep vs. superficial differences in modeling languages.
- The expressiveness vs. tractability tradeoff.
- The fundamental role of a very small set of inter-related concepts.

# Formal set-theoretic accounts

- It's important to our authors that we can reduce complex concepts to simpler ones.
- They're willing to sacrifice conceptual richness and subtlety for precision and rigor.
- They aim to capture common sense understanding and domain knowledge without appeal to either of those.
- Sometimes a demonstration that we *can* account for something in terms of simple sets is seen as
  valuable, even if it's not convenient or practical to ever use the reduction again.


# From Barabara Partee's discussion of sets

> The notion of set is taken as “undefined”, “primitive”, or “basic”,
> so we don’t try to define what a set is, but we can give an informal
> description, describe important properties of sets, and give
> examples. All other notions of mathematics can be built up based on
> the notion of set.

> Description: a *set* is a collection of objects which are called the
> *members* or *elements* of that set. If we have a set we say that some
> objects *belong* (or *do not belong*) to this set, *are* (or *are
> not*) *in* the set. We say also that sets *consist* of their elements.

# Implications

- Sets are abstract objects, even if their members are concrete or
  social objects.
- No two distinct sets can have the same members: same members implies
  same set.
- No set can change with respect to its members: different members
  implies different sets.
- Be careful of set descriptions that pick out different things at
  different times.
- When specifying a set in predicate notation, different descriptions may
  pick out exactly the same set.
- But properties are not defined by their instances. Therefore, properties and
  sets are different.


# Elements vs. subsets

- We use the $\in$ operator to relate an element to the set it belongs to.
- For example, $b \in \{a,b,c\}$
- $\{a,b\} \in \{\{a,b\}, \{b,c,d\}, \{a,f,g\}\}$
- But $\{a,b\} \subseteq \{a,b,c\}$
- $\{b\} \subseteq \{a,b,c\}$
- $\{a,c\} \subseteq \{a,b,c\}$
- $\{\{a,b\}, \{a,f,g\}\} \subseteq \{\{a,b\}, \{b,c,d\}, \{a,f,g\}\}$
- $\emptyset \subseteq \{a,b,c\}$ but $\emptyset \notin \{a,b,c\}$

# Sets and properties are different things

- The property of being an odd integer less than 8 and greater than 2
  is different from the property of being a prime integer less than 8
  and greater than 2, because "being prime" and "being odd" are different
  properties.
- But the set of odd integers between 2 and 8 is the same as the set
  of primes between 2 and 8. This is not just any equivalence
  relationship: we're talking about only one set.
- You might specify a category "students enrolled at the iSchool," but its
   *extension* would be different sets at different times.


# Set operations

- Union: $A \cup B =_{def} \{x | x \in A$ or $x \in B\}$
- Intersection: $A \cap B =_{def} \{x | x \in A$ and $x \in B\}$
- Complement:  $A' =_{def} \{x | x \notin A\}$
- Relative Complement:  $A - B =_{def} \{x | x \in A$ and $x \notin B\}$


# Tuples are ordered sets

- $\langle a,b \rangle =_{def} \{\{a\},\{a,b\}\}$
- $\langle a,b,c \rangle =_{def} \langle\langle a,b \rangle,c\rangle$
- Cartesian products are sets of tuples.
- $A \times B =_{def} \{\langle x,y \rangle\ |\ x \in A\ and\ y \in B\}$
- Relations are subsets of cartesian products.
- If $A$ and $B$ are sets and $R \subseteq A \times B$ we say that $R$ is a binary relation from $A$ to $B$.
- $A \times B \times C =_{def} ((A \times B) \times C)$


# Domain, range, functions, and composition.

- The set \textbf{dom} $R = \{a\ |\ \langle a,b \rangle \in R$ for some $b\}$ is called the \emph{domain}
  of the relation $R$ and \ldots
- \ldots the set \textbf{range} $R = \{b\ |\ \langle a,b \rangle \in R$ for some $a\}$ is called the
   \emph{range} of relation $R$.
- If  $A$ and $B$ are sets and $R \subseteq A \times B$ we say that $R^{-1} \subseteq B \times A$ is the
  \emph{inverse} of $R$, where $R^{-1} =_{def} \{\langle b,a \rangle\ |\ \langle a,b \rangle \in R\}$.
- Given relations $R \subseteq A \times B$ and $S \subseteq B \times C$ the composite of $R$ and $S$,
  written $S \circ R =_{def} \{\langle x,z \rangle |$ for some $y, \langle x,y \rangle \in R$ and $\langle y,z \rangle \in S \}$
- A relation $F \subseteq A \times B$ is a \emph{function} (or mapping) $F:A \rightarrow B$ if and only if
  the domain of $F$ is $A$ and $F$ pairs every element in that domain with exactly one element in the range,
  i.e. $\langle a,b \rangle \in F$ and $\langle a,c \rangle \in F$ implies $b = c$.


# From sets to properties and relations
- Suppose, for example, our domain ($\Delta$) includes things that have the
  properties of being courses, course sections, students, and
  instructors.
- Define $C, E, I, O, P, S \subseteq \Delta$ as the sets of courses,
  events, instructors, course sections (offerings), persons, and students, respectively.
- $I \subseteq P$, $S \subseteq P$, $O \subseteq E$

# From relations to relationships

- Recall that Jubien understands relationships as ways something can
  be with respect to something else.
- We can model relationships as relations between two or more sets.
- For example, define the "has section" relationship $H \subseteq (C \times O)$
- Let $a, b, c, d$ represent IS561, IS501, Sp2019-IS561-OA, and
  Fa2019-IS501-A, respectively.
- $\langle a, c \rangle \in (C \times O), \langle a, d \rangle \in (C \times O), \langle b, c \rangle \in (C \times O), \langle b, d \rangle \in (C \times O)$
- $\langle a, c \rangle \in H$ but $\langle a, d \rangle \notin H$
- $\langle b, d \rangle \in H$ but $\langle b, c \rangle \notin H$


# Classes vs. properties

- In our professional discourse we'll frequently encounter the term
  "class" as roughly synonymous with "category."
- Classes, like properties, will have instances, but we'll typically
  encounter them in the context of software or database development,
  where the classes and instances are data structures, rather than
  domain objects.
- The two types of diagram we often see in our professions were originally
  invented for software engineering.
- Therefore, some of their notational conventions will make sense only
  for purposes of writing code or defining database schemas.
- Unfortunately, that doesn't stop people from using those conventions
  imprecisely for illustrating domain models.
- We will focus on those conventions important for modeling our
  domains of interest.

# UML Class Diagram
![UML](UML1.eps)\ 

# Entity-Relationship Diagram
![ER](ER1.eps)\ 


# Common to the ER diagram and the UML class diagram

1. Rectangles representing domain categories ("entity sets" and "classes")
2. Arrows between the rectangles representing hierarchical structure on the categories ("generalization")
3. Connections between the rectangles representing domain relationships ("relationships" and "associations")
4. The arity or "degree" of the relationship (typically binary)
5. The cardinality or multiplicity of the relationship
6. Scalar attributes or features of the classes

# Not common to both diagrams

1. Directionality of the relationship
2. "Weak entity" distinction
3. Identifying vs. descriptive attributes
4. Meronymic vs. non-meronymic associations
5. \ldots and many things covered in the readings, but not used in these examples



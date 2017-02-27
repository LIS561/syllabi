---
title: Relational Modeling, Part 1.
author: Dave Dubin
date: February 27, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# This week

- Last week we considered sets, relations, and formalization.
- This week you read about two types of diagram: the *entity-relationship diagram* and the *UML class diagram*.
- Tonight I'll show you the connections between last week's discussion and this week's readings.

# Review from last week

- Tuples are ordered sets
- Cartesian products are sets of tuples.
- $A \times B =_{def} \{\langle x,y \rangle\ |\ x \in A\ and\ y \in B\}$
- Relations are subsets of cartesian products.
- If $A$ and $B$ are sets and $R \subseteq A \times B$ we say that $R$ is a binary relation from $A$ to $B$.
- $A \times B \times C =_{def} ((A \times B) \times C)$
- The set \textbf{dom} $R = \{a\ |\ \langle a,b \rangle \in R$ for some $b\}$ is called the \emph{domain}
  of the relation $R$ and \ldots
- \ldots the set \textbf{range} $R = \{b\ |\ \langle a,b \rangle \in R$ for some $a\}$ is called the
   \emph{range} of relation $R$.
- If  $A$ and $B$ are sets and $R \subseteq A \times B$ we say that $R^{-1} \subseteq B \times A$ is the
  \emph{inverse} of $R$, where $R^{-1} =_{def} \{\langle b,a \rangle\ |\ \langle a,b \rangle \in R\}$.

# From sets to properties
- In our first presentation we considered Jubien's definition of property: "a way that something can be."
- Anything in the domain we're modeling that exhibits the property is an *instance* of the property.
- Last week we saw that we can use sets to model properties, even
  though a property will be different than the set that is its
  *extension*.
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
- Let $a, b, c, d$ represent LIS561, LIS501, Sp2017-LIS561-LE, and
  Fa2016-LIS501-A, respectively.
- $\langle a, c \rangle \in (C \times O), \langle a, d \rangle \in (C \times O), \langle b, c \rangle \in (C \times O), \langle b, d \rangle \in (C \times O)$
- $\langle a, c \rangle \in H$ but $\langle a, d \rangle \notin H$
- $\langle b, d \rangle \in H$ but $\langle b, c \rangle \notin H$
- In predicate logic we'd say $Hbd \wedge {\neg}Hbc$

# Classes vs. properties

- In our professional discourse we'll frequently encounter the term
  "class" as roughly synonymous with "category."
- Classes, like properties, will have instances, but we'll typically
  encounter them in the context of software or database development,
  where the classes and instances are data structures, rather than
  domain objects.
- The two types of diagram you read about for today were originally
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

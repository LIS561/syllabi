---
title: Relational Modeling, Part 1.
author: Dave Dubin
date: February 27, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# Review from last week
- Last week we considered sets, relations, and formalization.


# UML Class Diagram
![UML](UML1.eps)\ 

# Entity-Relationship Diagram
![ER](ER1.eps)\ 


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

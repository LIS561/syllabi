---
title: Sets, relations, and functions
author: Dave Dubin
date: February 20, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# Sets we've already encountered

- Propositional logic: A set of $n$ proposition letters generates a set of $2^n$ states of affairs: ways the world might be.
- $\{p,q,r\}$ generates $\{pqr,pq\overline{r},p\overline{q}r,p\overline{qr},\overline{p}qr,\overline{p}q\overline{r},\overline{pq}r,\overline{pqr}\}$
- Grammar: let $P$ be a set of proposition letters and let $p \in P$. 
- Production set: $\varphi \Coloneqq p|\neg\varphi|(\varphi \wedge \varphi)|(\varphi \vee \varphi)|(\varphi \rightarrow \varphi)|(\varphi \leftrightarrow \varphi)$
- Think $\{\varphi \Coloneqq p, \varphi \Coloneqq \neg\varphi, \varphi \Coloneqq (\varphi \wedge \varphi), \varphi \Coloneqq (\varphi \vee \varphi),\ldots\}$
- Logical consistency: A set of propositional logic statements is consistent if
  at least one state of affairs satisfies every statement in 
  the set.
- Inference: a conclusion is \emph{valid} with respect to a set of premises if the conclusion
  is true in every sitation where the premises are true (van Benthem, et al, section 2-4).



# From our syllabus

The course is thus simultaneously a foundations course
and a survey course. There are several important cross-cutting
themes:

- Data independence through abstraction.
- The interdefinability of fundamental modeling constructs.
- Deep vs. superficial differences in modeling languages.
- The expressiveness vs. tractability tradeoff.
- The fundamental role of a very small set of inter-related concepts.

# From the Partee reading

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
   
# Key definitions from the Partee reading

- $\langle a,b \rangle =_{def} \{\{a\},\{a,b\}\}$
- $A \times B =_{def} \{\langle x,y \rangle\ |\ x \in A\ and\ y \in B\}$
- $\langle a,b,c \rangle =_{def} \langle\langle a,b \rangle,c\rangle$
- $A \times B \times C =_{def} ((A \times B) \times C)$
- If $A$ and $B$ are sets and $R \subseteq A \times B$ we say that $R$ is a binary relation from $A$ to $B$.
- The set \textbf{dom} $R = \{a\ |\ \langle a,b \rangle \in R$ for some $b\}$ is called the \emph{domain}
  of the relation $R$ and \ldots
- \ldots the set \textbf{range} $R = \{b\ |\ \langle a,b \rangle \in R$ for some $a\}$ is called the
   \emph{range} of relation $R$.
- If  $A$ and $B$ are sets and $R \subseteq A \times B$ we say that $R^{-1} \subseteq B \times A$ is the
  \emph{inverse} of $R$, where $R^{-1} =_{def} \{\langle b,a \rangle\ |\ \langle a,b \rangle \in R\}$.
- A relation $F \subseteq A \times B$ is a \emph{function} (or mapping) $F:A \rightarrow B$ if and only if
  the domain of $F$ is $A$ and $F$ pairs every element in that domain with exactly one element in the range,
  i.e. $\langle a,b \rangle \in F$ and $\langle a,c \rangle \in F$ implies $b = c$.

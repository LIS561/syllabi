---
title: Artificial Languages, Part 2 (Semantics)
author: Dave Dubin
date: April 3, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usepackage{mathabx}  
---

# Language and the mind
![Cognitive view](semantics1.eps)\ 

# Language and the world
![Platonistic view](semantics2.eps)\ 



# Bach on Semantics

1. The structure of language can each be described using formal systems.
2. Language has meaning.
2. Meanings are things that aren't language.

# Language and the world
![page 10 figure from Bach (1989)](denotes.eps)

# Language and the world
![page 12 figure from Bach (1989)](lovers.eps)

# Syntax of Bach's logic subset

${\langle}var{\rangle} \Coloneqq w|x|y|z$

${\langle}con{\rangle} \Coloneqq a|b|c|d$

${\langle}ter{\rangle} \Coloneqq {\langle}var{\rangle}|{\langle}con{\rangle}$

${\langle}1pp{\rangle} \Coloneqq Run|Walk|Happy|Calm$

${\langle}2pp{\rangle} \Coloneqq Love|Kiss|Like|See$

${\langle}wff{\rangle} \Coloneqq {\langle}1pp{\rangle}({\langle}ter{\rangle})$

${\langle}wff{\rangle} \Coloneqq {\langle}2pp{\rangle}({\langle}ter{\rangle},{\langle}ter{\rangle})$

${\langle}wff{\rangle} \Coloneqq -{\langle}wff{\rangle}$

${\langle}wff{\rangle} \Coloneqq ({\langle}wff{\rangle} \vee {\langle}wff{\rangle})$

${\langle}wff{\rangle} \Coloneqq ({\langle}wff{\rangle}\ \&\ {\langle}wff{\rangle})$

${\langle}wff{\rangle} \Coloneqq {\forall}{\langle}var{\rangle}\ {\langle}wff{\rangle}$

${\langle}wff{\rangle} \Coloneqq {\exists}{\langle}var{\rangle}\ {\langle}wff{\rangle}$

# Notational differences between the readings

- The $\&$ and $\wedge$ symbols both mean conjunction ("and").
- The $\neg$, $\sim$, and $-$ all mean negation ("not").
- Sometimes predicates are written with parentheses ($P(x,y)$), sometimes not ($Pxy$).
- In other words, $(Pab \wedge {\neg}Qbc)$ is the same as $(P(a,b)\ \&\ {-Q}(b,c))$.
- van Benthem, et al. use $D$ for the domain set and $I$ for the interpretation function.
- But Bach calls the domain set $E$ (entities) and the interpretation function $D$ (denotes).
- I will bring in some details from the van Benthem readings, but use Bach's notation in this
  presentation.
- Bach calls his structure an interpretation, so I'll use $I$ for that.

# The semantics of propositional logic vs. predicate logic

van Benthem, et al. write:

> In propositional logic, the link was the valuation mapping proposition letters to truth
> values. But this will no longer do. For checking whether a statement saying that a certain
> object has a certain property, or that certain objects are in a certain relation is true we need
> something more refined. Instead of just saying that "John is boy" is assigned the value
> true, we now need an interpretation for “John” and an interpretation for "being a boy".

Recall that the only non-language view of the world or domain that we needed consisted of
truth values and propositions that concerned domain entities. Now we're going to include
domain elements themselves in our model, not just propositions concerning them.


# Language and the world
![Cognitive view](semantics3a.eps)\ 

# Language and the world
![Cognitive view](semantics3b.eps)\ 

# Language and the world
![Cognitive view](semantics3c.eps)\ 

# Language and the world
![Cognitive view](semantics3d.eps)\ 

# Language and the world
![Cognitive view](semantics3e.eps)\ 



# Models and interpretations

Bach writes:

> An *interpretation* is a way of assigning denotations 
> in a certain model structure
> to expressions in a language.

- While van Benthem's formalization is simply $M = {\langle}D, I{\rangle}$, Bach's approach gives us:
  $I = {\langle}M1, D, G{\rangle}$ where:
     - $M1$ is the first model structure he proposes;
     - $G$ is a set of assignments of values to variables (same as van Benthem, et al.)
     - $D$ is the denoting evaluation function (van Benthem's $I$).
- Bach's $M1$ is itself a two-place tuple consisting of:
     - Set $E$ of individuals (van Benthem's $D$);
     - The set of truth values $\{ 1, 0 \}$.
- Toward the end of the reading he suggests adding a set of times and a set of
  possible worlds for more expressive languages.

# Simple denotations

Individual constants (like $a$ and $b$) will denote individuals in the domain, so they'll
be elements of (Bach's) set $E$. The one-place predicates (classes) will denote their
extensions (i.e., subsets of the domain). The two-place predicates (binary relations) will
denote sets of ordered pairs.

$D({\langle}con{\rangle}) \in E$ 

$D({\langle}1pp{\rangle}) \subseteq E$

$D({\langle}2pp{\rangle}) \subseteq E \times E$

Following the convention in your logic readings, we adopt the
notation ${\varphi}_D$ for $D({\varphi})$. So, for example,
$a_D$ would be some individual in the Domain set $E$, and 
$Love_D$ would be a set of ordered pairs ${\langle}x,y{\rangle}$, 
in each of which $x$ loves $y$.

# Variable assignments

- Let $V$ be the set of variables in the language. Bach's $G$ is a set of variable
  assignments, and each $g \in G$ is a function from variables ($v \in V$) to individuals in $E$, i.e.:
  $g \subseteq V \times E$.
- For example, suppose $g_1 = \{{\langle}w,a_D{\rangle}, {\langle}x,b_D{\rangle}, {\langle}y,c_D{\rangle}, {\langle}z,d_D{\rangle}\}$,
  but $g_2 = \{{\langle}w,b_D{\rangle}, {\langle}x,c_D{\rangle}, {\langle}y,d_D{\rangle}, {\langle}z,a_D{\rangle}\}$.
- Because our functions are cartesian product subsets, two or more different variables can be mapped to the
  same individual. For example, maybe 
  $g_3 = \{{\langle}w,a_D{\rangle}, {\langle}x,a_D{\rangle}, {\langle}y,b_D{\rangle}, {\langle}z,a_D{\rangle}\}$ and
  $g_4 = \{{\langle}w,c_D{\rangle}, {\langle}x,c_D{\rangle}, {\langle}y,c_D{\rangle}, {\langle}z,c_D{\rangle}\}$.
  But they're functions, so every variable in the domain will be included.
- Following van Benthem, et al., the expression $g[v{\coloneqq}e]$ is
  understood to mean "the variable assignment that is completely like
  $g$ except that $v$ now gets the value $e$ (where $g$ might have
  assigned a different value)."
- For example, $g_1[x{\coloneqq}d_D] = \{{\langle}w,a_D{\rangle}, {\langle}x,d_D{\rangle}, {\langle}y,c_D{\rangle}, {\langle}z,d_D{\rangle}\}$

# Denotation, support, and truth

An expression in our language will be true or false in an interpretation, relative to a
particular assignment of individuals to variables. So, carrying forward our notion of
support from the propositional logic semantics, we write $I\ {\models_g}\ \varphi$ to mean
that assignment $g$ *satisfies* expression $\varphi$ in interpretation $I$ (or, in other
words, $\varphi$ is true in interpretation $I$ under assignment $g$).  

- ${\ldbrack}v{\rdbrack}^g_D = g(v)$
- ${\ldbrack}c{\rdbrack}^g_D = c_D$
- $I\ {\models_g}\ P(t)$ iff ${\ldbrack}t{\rdbrack}^g_D \in P_D$
- $I\ {\models_g}\ R(s,t)$ iff ${\langle}{\ldbrack}s{\rdbrack}^g_D,{\ldbrack}t{\rdbrack}^g_D{\rangle} \in R_D$
- $I\ {\models_g}\ {-\varphi}$ iff it is not the case that $I\ {\models_g}\ \varphi$
- $I\ {\models_g}\ (\varphi_1\ \&\ \varphi_2)$ iff $I\ {\models_g}\ \varphi_1$ and $I\ {\models_g}\ \varphi_2$
- $I\ {\models_g}\ (\varphi_1 \vee \varphi_2)$ iff $I\ {\models_g}\ \varphi_1$ or $I\ {\models_g}\ \varphi_2$
- $I\ {\models_g}\ {\forall}v \varphi$ iff for all $e \in E$ it holds that $I\ {\models_{g[v{\coloneqq}e]}}\ \varphi$
- $I\ {\models_g}\ {\exists}v \varphi$ iff for at least one $e \in E$ it holds that $I\ {\models_{g[v{\coloneqq}e]}}\ \varphi$

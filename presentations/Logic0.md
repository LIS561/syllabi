---
title: Propositional Logic
author: Dave Dubin
date: October 10, 2016
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# Concepts from earlier in the semester

- Propositions are the bearers of truth values: the kinds of things that can be
  true or false.

- States of affairs are the parts of reality responsible for making
  propositions true or false.


# Propositional logic

 - We represent propositions with lower case letters (typically $p, q,$ and $r$).
 - A set of proposition letters generates a set of states of affairs: ways the world might be.
 - $n$ proposition letters generate $2^n$ states of affairs.
 - $\{pqr,pq\overline{r},p\overline{q}r,p\overline{qr},\overline{p}qr,\overline{p}q\overline{r},\overline{pq}r,\overline{pqr}\}$

# Logical Operators

Symbol               In natural language   Technical name
------------------- --------------------- ---------------
$\neg$                       not                 negation
$\wedge$                     and              conjunction
$\vee$                       or               disjunction
$\rightarrow$              if ... then        implication
$\leftrightarrow$       if and only if        equivalence

Table: 2.15 from van Benthem, et al.

# Logical Expressions

 - A sentence constructed from proposition letters and operators is true
   or false in each state of affairs.
 - Consider, for example: $({\neg}p \vee q) \rightarrow r$
 - The sentence is mapped to a truth value via the following tables

 
# Semantics of the operators

  $\phi$   $\neg\phi$
 -------- ------------
    0           1
    1           0	

  $\phi$   $\psi$   $\phi \wedge \psi$   $\phi \vee \psi$   $\phi \rightarrow \psi$   $\phi \leftrightarrow \psi$
 -------- -------- -------------------- ------------------ ------------------------- ----------------------------- 
    0         0            0                    0                        1                         1                          
    0         1            0                    1                        1                         0                          
    1         0            0                    1                        0                         0                          
    1         1            1                    1                        1                         1                           

Table: 2.18 from van Benthem, et al.


# Exercise 2.3

You are given the information that $p$-or-$q$ and (not-$p$)-or-$r$. What can you conclude
about $q$ and $r$? What is the strongest valid conclusion you can draw? (A statement is stronger than
another statement if it rules out more possibilities.)


# Drawing truth tables for expressions


\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\sim$ & p & $\lor$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & 0 & \textcolor{red}{1} & 1 & \textcolor{red}{1} &  & 1 & \textcolor{red}{1} & \\
1 & 1 & 0 &  &  & 0 & \textcolor{red}{1} & 1 & \textcolor{red}{1} &  & 0 & \textcolor{red}{0} & \\
1 & 0 & 1 &  &  & 0 & \textcolor{red}{1} & 0 & \textcolor{red}{0} &  & 1 & \textcolor{red}{1} & \\
1 & 0 & 0 &  &  & 0 & \textcolor{red}{1} & 0 & \textcolor{red}{0} &  & 1 & \textcolor{red}{0} & \\
0 & 1 & 1 &  &  & 1 & \textcolor{red}{0} & 1 & \textcolor{red}{1} &  & 1 & \textcolor{red}{1} & \\
0 & 1 & 0 &  &  & 1 & \textcolor{red}{0} & 1 & \textcolor{red}{1} &  & 0 & \textcolor{red}{0} & \\
0 & 0 & 1 &  &  & 1 & \textcolor{red}{0} & 1 & \textcolor{red}{0} &  & 1 & \textcolor{red}{1} & \\
0 & 0 & 0 &  &  & 1 & \textcolor{red}{0} & 1 & \textcolor{red}{0} &  & 0 & \textcolor{red}{0} & \\
\end{tabular}



# Drawing truth tables for expressions


\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\sim$ & p & $\lor$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & \textcolor{red}{0} & \textcolor{green}{1} & 1 & 1 &  & 1 & 1 & \\
1 & 1 & 0 &  &  & \textcolor{red}{0} & \textcolor{green}{1} & 1 & 1 &  & 0 & 0 & \\
1 & 0 & 1 &  &  & \textcolor{red}{0} & \textcolor{green}{1} & 0 & 0 &  & 1 & 1 & \\
1 & 0 & 0 &  &  & \textcolor{red}{0} & \textcolor{green}{1} & 0 & 0 &  & 1 & 0 & \\
0 & 1 & 1 &  &  & \textcolor{red}{1} & \textcolor{green}{0} & 1 & 1 &  & 1 & 1 & \\
0 & 1 & 0 &  &  & \textcolor{red}{1} & \textcolor{green}{0} & 1 & 1 &  & 0 & 0 & \\
0 & 0 & 1 &  &  & \textcolor{red}{1} & \textcolor{green}{0} & 1 & 0 &  & 1 & 1 & \\
0 & 0 & 0 &  &  & \textcolor{red}{1} & \textcolor{green}{0} & 1 & 0 &  & 0 & 0 & \\
\end{tabular}


# Drawing truth tables for expressions


\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\sim$ & p & $\lor$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & \textcolor{red}{0} & \textcolor{red}{1} & 1 & \textcolor{red}{1} &  & 1 & 1 & \\
1 & 1 & 0 &  &  & \textcolor{red}{0} & \textcolor{red}{1} & 1 & \textcolor{red}{1} &  & 0 & 0 & \\
1 & 0 & 1 &  &  & \textcolor{red}{0} & \textcolor{red}{1} & 0 & \textcolor{red}{0} &  & 1 & 1 & \\
1 & 0 & 0 &  &  & \textcolor{red}{0} & \textcolor{red}{1} & 0 & \textcolor{red}{0} &  & 1 & 0 & \\
0 & 1 & 1 &  &  & \textcolor{red}{1} & \textcolor{red}{0} & 1 & \textcolor{red}{1} &  & 1 & 1 & \\
0 & 1 & 0 &  &  & \textcolor{red}{1} & \textcolor{red}{0} & 1 & \textcolor{red}{1} &  & 0 & 0 & \\
0 & 0 & 1 &  &  & \textcolor{red}{1} & \textcolor{red}{0} & 1 & \textcolor{red}{0} &  & 1 & 1 & \\
0 & 0 & 0 &  &  & \textcolor{red}{1} & \textcolor{red}{0} & 1 & \textcolor{red}{0} &  & 0 & 0 & \\
\end{tabular}


# Drawing truth tables for expressions


\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\sim$ & p & $\lor$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & \textcolor{red}{0} & \textcolor{red}{1} & 1 & \textcolor{red}{1} &  & 1 & 1 & \\
1 & 1 & 0 &  &  & \textcolor{red}{0} & \textcolor{red}{1} & 1 & \textcolor{red}{1} &  & 0 & 0 & \\
1 & 0 & 1 &  &  & \textcolor{red}{0} & \textcolor{red}{1} & 0 & \textcolor{red}{0} &  & 1 & 1 & \\
1 & 0 & 0 &  &  & \textcolor{red}{0} & \textcolor{red}{1} & 0 & \textcolor{red}{0} &  & 1 & 0 & \\
0 & 1 & 1 &  &  & \textcolor{red}{1} & \textcolor{red}{0} & 1 & \textcolor{red}{1} &  & 1 & 1 & \\
0 & 1 & 0 &  &  & \textcolor{red}{1} & \textcolor{red}{0} & 1 & \textcolor{red}{1} &  & 0 & 0 & \\
0 & 0 & 1 &  &  & \textcolor{red}{1} & \textcolor{red}{0} & 1 & \textcolor{red}{0} &  & 1 & 1 & \\
0 & 0 & 0 &  &  & \textcolor{red}{1} & \textcolor{red}{0} & 1 & \textcolor{red}{0} &  & 0 & 0 & \\
\end{tabular}



# Drawing truth tables for expressions


\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\sim$ & p & $\lor$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & 0 & 1 & 1 & 1 &  & 1 & 1 & \\
1 & 1 & 0 &  &  & 0 & 1 & 1 & 1 &  & 0 & 0 & \\
1 & 0 & 1 &  &  & 0 & 1 & 0 & 0 &  & 1 & 1 & \\
1 & 0 & 0 &  &  & 0 & 1 & 0 & 0 &  & 1 & 0 & \\
0 & 1 & 1 &  &  & 1 & 0 & 1 & 1 &  & 1 & 1 & \\
0 & 1 & 0 &  &  & 1 & 0 & 1 & 1 &  & 0 & 0 & \\
0 & 0 & 1 &  &  & 1 & 0 & 1 & 0 &  & 1 & 1 & \\
0 & 0 & 0 &  &  & 1 & 0 & 1 & 0 &  & 0 & 0 & \\
\end{tabular}


# Drawing truth tables for expressions

~~~~~~~~~~
   (~p v q) -> r
-------------------
     0   0     0
     0   0     1
     0   1     0
     0   1     1
     1   0     0
     1   0     1
     1   1     0
     1   1     1
~~~~~~~~~~

# Drawing truth tables for expressions

~~~~~~~~~~
   (~p v q) -> r
-------------------
    10   0     0
    10   0     1
    10   1     0
    10   1     1
    01   0     0
    01   0     1
    01   1     0
    01   1     1
~~~~~~~~~~

# Drawing truth tables for expressions

~~~~~~~~~~
   (~p v q) -> r
-------------------
    10 1 0     0
    10 1 0     1
    10 1 1     0
    10 1 1     1
    01 0 0     0
    01 0 0     1
    01 1 1     0
    01 1 1     1
~~~~~~~~~~

# Drawing truth tables for expressions

~~~~~~~~~~
   (~p v q) -> r
-------------------
    10 1 0  0  0
    10 1 0  1  1
    10 1 1  0  0
    10 1 1  1  1
    01 0 0  1  0
    01 0 0  1  1
    01 1 1  0  0
    01 1 1  1  1
~~~~~~~~~~

# Grammar of propositional logic

Let $P$ be a set of proposition letters and let $p \in P$. 

The following expression defines the recursive grammar for a logical
expression $\phi$ in [Backus–Naur Form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form):

$\phi \Coloneqq p|\neg\phi|(\phi \wedge \phi)|(\phi \vee \phi)|(\phi \rightarrow \phi)|(\phi \leftrightarrow \phi)$

# Syntactically conforming expressions

Let $P = \{o,q,r,s\}$



Examples of grammatically conforming expressions include:

- $r$
- ${\neg}q$
- $(s \leftrightarrow o)$
- $({\neg}(s \leftrightarrow \neg\neg{\neg}o) \rightarrow (q \wedge q))$

Grammatically *incorrect* expressions would include:

- $\neg\vee p$ 
- $\vee ) p \neg$
- ${\neg}p \vee q \rightarrow r$ 

How many correct expressions are consistent with the last one?

# Syntactic ambiguity

These conforming expressions are all consistent with ${\neg}p \vee q \rightarrow r$

- $(({\neg}p \vee q) \rightarrow r)$
- $({\neg}(p \vee q) \rightarrow r)$
- ${\neg}((p \vee q) \rightarrow r)$
- $({\neg}p \vee (q \rightarrow r))$
- ${\neg}(p \vee (q \rightarrow r))$

# More on semantics

- Semantics is the relationship of a language to the part
  of the world that we're modeling.

- Valuations are functions from expressions to truth values.

- "$V(\phi) = 1$" means the formula (or sentence) $\phi$ is true in the state
  of affairs represented by the function $V$. "$V(\phi) = 0$" means that $\phi$ is false in
  the state of affairs represented by the function $V$.

- For "$V(\phi) = 1$" we also write "$V \models \phi$" read as "V is a model of $\phi$"
  or "V satisfies $\phi$."

- If V doesn't satisfy $\phi$ we write "$V \not\models \phi$". In other words $V(\phi) = 0$.

# Logical truth and logical falsity.

- A statement $\phi$ is logically true if it is true in every state of
  affairs generated by its propositional variables.

- A statement $\phi$ is logically false if it is false in every state of
  affairs generated by its propositional variables.

- If a statement $\phi$ is neither logically true or logically false then
  it is contingent.

- Examples:
    1. $(q \vee {\neg}q)$ is logically true.
    2. $(q \wedge {\neg}q)$ is logically false.

# Consistency

- A set of propositional logic statements is consistent if
  at least one state of affairs satisfies every statement in 
  the set.

- A set of propositional logic statements is inconsistent if
  no state of affairs satisfies every statement in 
  the set.

# Inference and validity

- A conclusion is \emph{valid} with respect to a set of premises if the conclusion
  is true in every sitation where the premises are true (van Benthem, et al, page 2-4).
- One can validly infer a conclusion $\phi$ from a set of premises
  $P$ if the negation of $\phi$ is inconsistent with the set of statements
  $P$.


# Computation and expressive power

(From van Bentham, et al., chapter 2)

1. Computing a truth value for a formula takes linear time.
2. Computing a truth table for validity takes exponential time.
3. The problem of testing for validity in propositional logic is
   decidable: there exists a mechanical method that computes the
   answer, at least in principle.
---
title: Propositional Logic
author: Dave Dubin
date: Fall Semester, 2018
---

# Reasoning vs. representation

- In this class we'll give some attention to logical reasoning and inference.
- The same rules that govern valid argumentation also enable information systems to answer interesting questions.
- Logic is also a means to describe a *domain* (some part of the world
  we're interested in).

# Propositions, statements, and sentences
![Platonistic view](propositions1.eps)\ 


# Propositions, statements, and sentences

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
 - Consider, for example: $(({\neg}p \vee q) \rightarrow r)$
 - The sentence is mapped to a truth value via the following tables

 
# Semantics of the operators

  $\varphi$   $\neg\varphi$
 ----------- ---------------
      0            1
      1            0	

  $\varphi$   $\psi$   $\varphi \wedge \psi$   $\varphi \vee \psi$   $\varphi \rightarrow \psi$   $\varphi \leftrightarrow \psi$
 ----------- -------- ----------------------- --------------------- ---------------------------- -------------------------------- 
      0         0               0                       0                        1                         1                          
      0         1               0                       1                        1                         0                          
      1         0               0                       1                        0                         0                          
      1         1               1                       1                        1                         1                           

Table: 2.18 from van Benthem, et al.

# Exercise 2.6

- "I will only go to school if I get a cookie now."
- Compare with "I will go to school if I get a cookie"
- The latter is cookie implies school, but the former is school implies cookie.
- You want $(s \rightarrow c)$
- Gloss: s =  "I will go to school" and c =  "I get a cookie."
- John and Mary are running
- $(j \wedge m)$
- A foreign national is entitled to social security if he has legal
  employment or if he has had such less than three years ago, unless
  he is currently also employed abroad.
- $(((e \vee l) \wedge {\neg}a) \rightarrow s)$
- $e =$ "A foreign national has legal employment."
- $l =$  "He has had legal employment less than three years ago."
- $a =$  "He is currently employed abroad."
- $s =$ "He is entitled to social security."

# Drawing truth tables for expressions

\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\neg$ & p & $\vee$ & q & ) & $\rightarrow$ & r & )\\
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
p & q & r & ( & ( & $\neg$ & p & $\vee$ & q & ) & $\rightarrow$ & r & )\\
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
p & q & r & ( & ( & $\neg$ & p & $\vee$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & \textcolor{green}{0} & 1 & \textcolor{red}{1} & \textcolor{green}{1} &  & 1 & 1 & \\
1 & 1 & 0 &  &  & \textcolor{green}{0} & 1 & \textcolor{red}{1} & \textcolor{green}{1} &  & 0 & 0 & \\
1 & 0 & 1 &  &  & \textcolor{green}{0} & 1 & \textcolor{red}{0} & \textcolor{green}{0} &  & 1 & 1 & \\
1 & 0 & 0 &  &  & \textcolor{green}{0} & 1 & \textcolor{red}{0} & \textcolor{green}{0} &  & 1 & 0 & \\
0 & 1 & 1 &  &  & \textcolor{green}{1} & 0 & \textcolor{red}{1} & \textcolor{green}{1} &  & 1 & 1 & \\
0 & 1 & 0 &  &  & \textcolor{green}{1} & 0 & \textcolor{red}{1} & \textcolor{green}{1} &  & 0 & 0 & \\
0 & 0 & 1 &  &  & \textcolor{green}{1} & 0 & \textcolor{red}{1} & \textcolor{green}{0} &  & 1 & 1 & \\
0 & 0 & 0 &  &  & \textcolor{green}{1} & 0 & \textcolor{red}{1} & \textcolor{green}{0} &  & 0 & 0 & \\
\end{tabular}


# Drawing truth tables for expressions


\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\neg$ & p & $\vee$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & 0 & 1 & \textcolor{green}{1} & 1 &  & \textcolor{red}{1} & \textcolor{green}{1} & \\
1 & 1 & 0 &  &  & 0 & 1 & \textcolor{green}{1} & 1 &  & \textcolor{red}{0} & \textcolor{green}{0} & \\
1 & 0 & 1 &  &  & 0 & 1 & \textcolor{green}{0} & 0 &  & \textcolor{red}{1} & \textcolor{green}{1} & \\
1 & 0 & 0 &  &  & 0 & 1 & \textcolor{green}{0} & 0 &  & \textcolor{red}{1} & \textcolor{green}{0} & \\
0 & 1 & 1 &  &  & 1 & 0 & \textcolor{green}{1} & 1 &  & \textcolor{red}{1} & \textcolor{green}{1} & \\
0 & 1 & 0 &  &  & 1 & 0 & \textcolor{green}{1} & 1 &  & \textcolor{red}{0} & \textcolor{green}{0} & \\
0 & 0 & 1 &  &  & 1 & 0 & \textcolor{green}{1} & 0 &  & \textcolor{red}{1} & \textcolor{green}{1} & \\
0 & 0 & 0 &  &  & 1 & 0 & \textcolor{green}{1} & 0 &  & \textcolor{red}{0} & \textcolor{green}{0} & \\
\end{tabular}


# Exercise 2.11

\begin{tabular}{@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{}c@{ }}
p & q & ( & ( & p & $\rightarrow$ & q & ) & $\vee$ & ( & q & $\rightarrow$ & p & ) & )\\
\hline 
1 & 1 &  &  & 1 & 1 & 1 &  & \textcolor{red}{1} &  & 1 & 1 & 1 &  & \\
1 & 0 &  &  & 1 & 0 & 0 &  & \textcolor{red}{1} &  & 0 & 1 & 1 &  & \\
0 & 1 &  &  & 0 & 1 & 1 &  & \textcolor{red}{1} &  & 1 & 0 & 0 &  & \\
0 & 0 &  &  & 0 & 1 & 0 &  & \textcolor{red}{1} &  & 0 & 1 & 0 &  & \\
\end{tabular}

# Exercise 2.11

\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{}c@{}@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{}@{}c@{ }}
p & q & r & ( & ( & ( & p & $\vee$ & $\neg$ & q & ) & $\wedge$ & r & ) & $\leftrightarrow$ & ( & $\neg$ & ( & p & $\wedge$ & r & ) & $\vee$ & q & ) & )\\
\hline 
1 & 1 & 1 &  &  &  & 1 & 1 & 0 & 1 &  & 1 & 1 &  & \textcolor{red}{1} &  & 0 &  & 1 & 1 & 1 &  & 1 & 1 &  & \\
1 & 1 & 0 &  &  &  & 1 & 1 & 0 & 1 &  & 0 & 0 &  & \textcolor{red}{0} &  & 1 &  & 1 & 0 & 0 &  & 1 & 1 &  & \\
1 & 0 & 1 &  &  &  & 1 & 1 & 1 & 0 &  & 1 & 1 &  & \textcolor{red}{0} &  & 0 &  & 1 & 1 & 1 &  & 0 & 0 &  & \\
1 & 0 & 0 &  &  &  & 1 & 1 & 1 & 0 &  & 0 & 0 &  & \textcolor{red}{0} &  & 1 &  & 1 & 0 & 0 &  & 1 & 0 &  & \\
0 & 1 & 1 &  &  &  & 0 & 0 & 0 & 1 &  & 0 & 1 &  & \textcolor{red}{0} &  & 1 &  & 0 & 0 & 1 &  & 1 & 1 &  & \\
0 & 1 & 0 &  &  &  & 0 & 0 & 0 & 1 &  & 0 & 0 &  & \textcolor{red}{0} &  & 1 &  & 0 & 0 & 0 &  & 1 & 1 &  & \\
0 & 0 & 1 &  &  &  & 0 & 1 & 1 & 0 &  & 1 & 1 &  & \textcolor{red}{1} &  & 1 &  & 0 & 0 & 1 &  & 1 & 0 &  & \\
0 & 0 & 0 &  &  &  & 0 & 1 & 1 & 0 &  & 0 & 0 &  & \textcolor{red}{0} &  & 1 &  & 0 & 0 & 0 &  & 1 & 0 &  & \\
\end{tabular}

# Grammar of propositional logic

Let $P$ be a set of proposition letters and let $p \in P$. 

The following expression defines the recursive grammar for a logical
expression $\varphi$ in [Backus–Naur Form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form):

$\varphi \Coloneqq p|\neg\varphi|(\varphi \wedge \varphi)|(\varphi \vee \varphi)|(\varphi \rightarrow \varphi)|(\varphi \leftrightarrow \varphi)$

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


# Exercise 2.7

Which of the following are formulas in propositional logic?

- $p \rightarrow {\neg}q$
- ${\neg}{\neg} \wedge q \vee p$
- $p{\neg}q$


# More on semantics

- Semantics is the relationship of a language to the part
  of the world that we're modeling.

- Valuations are functions from expressions to truth values.

- "$V(\varphi) = 1$" means the formula (or sentence) $\varphi$ is true in the state
  of affairs represented by the function $V$. "$V(\varphi) = 0$" means that $\varphi$ is false in
  the state of affairs represented by the function $V$.

- For "$V(\varphi) = 1$" we also write "$V \models \varphi$" read as "V is a model of $\varphi$"
  or "V satisfies $\varphi$."

- If V doesn't satisfy $\varphi$ we write "$V \not\models \varphi$". In other words $V(\varphi) = 0$.

# Logical truth and logical falsity.

- A statement $\varphi$ is logically true if it is true in every state of
  affairs generated by its propositional variables.

- A statement $\varphi$ is logically false if it is false in every state of
  affairs generated by its propositional variables.

- If a statement $\varphi$ is neither logically true or logically false then
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
- One can validly infer a conclusion $\varphi$ from a set of premises
  $P$ if the negation of $\varphi$ is inconsistent with the set of statements
  $P$.


# Computation and expressive power

(From van Benthem, et al., chapter 2)

1. Computing a truth value for a formula takes linear time.
2. Computing a truth table for validity takes exponential time.
3. The problem of testing for validity in propositional logic is
   decidable: there exists a mechanical method that computes the
   answer, at least in principle.
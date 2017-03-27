---
title: Artificial Languages, Part 1 (Syntax)
author: Dave Dubin
date: March 27, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# Grammars for artificial languages

- We've seen grammars in earlier presentations.
- Propositional logic:
    - Let $P$ be a set of proposition letters and let $p \in P$.
    - $\varphi \Coloneqq p|\neg\varphi|(\varphi \wedge \varphi)|(\varphi \vee \varphi)|(\varphi \rightarrow \varphi)|(\varphi \leftrightarrow \varphi)$
- Predicate logic:
    - $\textbf{v} \Coloneqq x|y|z|\ldots$
    - $\textbf{c} \Coloneqq a|b|c|\ldots$
    - $\textbf{t} \Coloneqq \textbf{v}|\textbf{c}$
    - $\textbf{P} \Coloneqq P|Q|R|\ldots$
    - $\textbf{Atom} \Coloneqq \textbf{Pt}_{1}\ldots\textbf{t}_{n}$ where $n$ is the arity of \textbf{P}
    - $\varphi \Coloneqq \textbf{Atom}|\neg\varphi|(\varphi \wedge \varphi)|(\varphi \vee \varphi)|(\varphi \rightarrow \varphi)|(\varphi \leftrightarrow \varphi)|{\forall}\textbf{v} \varphi|{\exists}\textbf{v} \varphi$

# Bottom-up parse

\small

-   ${\forall}wx ((Fxw \wedge Aw) \rightarrow {\exists}yz ((Pxy \wedge Ay) \wedge (Fxz \wedge Dz)))$
- ${\forall}\textbf{vv} ((F\textbf{vv} \wedge A\textbf{v}) \rightarrow {\exists}\textbf{vv} ((P\textbf{vv} \wedge A\textbf{v}) \wedge (F\textbf{vv} \wedge D\textbf{v})))$
- ${\forall}\textbf{vv} ((\textbf{Pvv} \wedge \textbf{Pv}) \rightarrow {\exists}\textbf{vv} ((\textbf{Pvv} \wedge \textbf{Pv}) \wedge (\textbf{Pvv} \wedge \textbf{Pv})))$
- ${\forall}\textbf{vv} ((\textbf{Ptt} \wedge \textbf{Pt}) \rightarrow {\exists}\textbf{vv} ((\textbf{Ptt} \wedge \textbf{Pt}) \wedge (\textbf{Ptt} \wedge \textbf{Pt})))$
- ${\forall}\textbf{vv}((\textbf{Atom} \wedge \textbf{Atom})\rightarrow{\exists}\textbf{vv}((\textbf{Atom} \wedge \textbf{Atom}) \wedge (\textbf{Atom} \wedge \textbf{Atom})))$
- ${\forall}\textbf{vv} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{vv} ((\varphi \wedge \varphi) \wedge (\varphi \wedge \varphi)))$
- ${\forall}\textbf{vv} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{vv} ((\varphi \wedge \varphi) \wedge \varphi))$
- ${\forall}\textbf{vv} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{vv} (\varphi \wedge \varphi))$
- ${\forall}\textbf{vv} (\varphi \rightarrow {\exists}\textbf{vv} (\varphi \wedge \varphi))$
- ${\forall}\textbf{vv} (\varphi \rightarrow {\exists}\textbf{vv}\varphi)$
- ${\forall}\textbf{vv} (\varphi \rightarrow \varphi)$
- ${\forall}\textbf{vv}\varphi$
- $\varphi$

\normalsize

# Parsing is a search through a space of possible solutions

We can go wrong!

-   ${\forall}wx ((Fxw \wedge Aw) \rightarrow {\exists}yz ((Pxy \wedge  Ay) \wedge (Fxz \wedge Dz)))$
- ${\forall}\textbf{vv} ((F\textbf{vv} \wedge A\textbf{v}) \rightarrow {\exists}\textbf{vv} ((P\textbf{vv} \wedge A\textbf{v}) \wedge (F\textbf{vv} \wedge D\textbf{v})))$
- ${\forall}\textbf{vv} ((\textbf{Pvv} \wedge \textbf{Pv}) \rightarrow {\exists}\textbf{vv} ((\textbf{Pvv} \wedge \textbf{Pv}) \wedge (\textbf{Pvv} \wedge \textbf{Pv})))$
- ${\forall}\textbf{tt} ((\textbf{Ptt} \wedge \textbf{Pt}) \rightarrow {\exists}\textbf{tt} ((\textbf{Ptt} \wedge \textbf{Pt}) \wedge (\textbf{Ptt} \wedge \textbf{Pt})))$
- ${\forall}\textbf{tt}((\textbf{Atom} \wedge \textbf{Atom})\rightarrow{\exists}\textbf{tt}((\textbf{Atom} \wedge \textbf{Atom}) \wedge (\textbf{Atom} \wedge \textbf{Atom})))$
- ${\forall}\textbf{tt} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{tt} ((\varphi \wedge \varphi) \wedge (\varphi \wedge \varphi)))$
- ${\forall}\textbf{tt} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{tt} ((\varphi \wedge \varphi) \wedge \varphi))$
- ${\forall}\textbf{tt} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{tt} (\varphi \wedge \varphi))$
- ${\forall}\textbf{tt} (\varphi \rightarrow {\exists}\textbf{tt} (\varphi \wedge \varphi))$
- ${\forall}\textbf{tt} (\varphi \rightarrow {\exists}\textbf{tt}\varphi)$
- Stuck! No rule applies, so we must backtrack.
- A conforming expression should have *some* path to our start symbol, but how do we program software to make the right choices?

# Parsing as search

- Grammars like the ones we've seen typically have the parsing problem of which rules to apply in which order.
- Nondeterministic parsing software explores one path of choices, and if no rule applies will back up and try a different path.
- If all possible paths are exhausted for an expression, then the parse fails because the expression doesn't conform to the grammar.
- The time required to explore all those possibilities is expensive, even for very fast computers.
- Rules of thumb (heuristics) for ordering the productions can save time, but only on average.
- Ideally we'd like an efficient and deterministic path through the search space that allows us to quit early if the expression doesn't conform.
- It turns out that some languages are easy to parse: consider, for example, the set of strings consisting of the letter 'b'.

# An easy URL subset grammar

Consider this simple syntax for a subset of URL web addresses:

- Conforming expressions will all begin with `http://`
- followed by strings of one or more lower case letters that are separated by periods,
- the last such string will be one of `com`, `org`, or `edu`,
- then there's a slash,
- then zero or more strings of lower case letters that are separated by slashes
- with one of those slashes being the rightmost character.
- We can easily parse this from left to right, and quit right away if one of the rules is broken.

# Parsing a URL

\small

- `http://www.whatever.something.com/abc/cba/wxy/qrs/`
- **http://**`www.whatever.something.com/abc/cba/wxy/qrs/`
- **http://www.**`whatever.something.com/abc/cba/wxy/qrs/`
- **http://www.whatever.**`something.com/abc/cba/wxy/qrs/`
- **http://www.whatever.something.**`com/abc/cba/wxy/qrs/`
- **http://www.whatever.something.com/**`abc/cba/wxy/qrs/`
- **http://www.whatever.something.com/abc/**`cba/wxy/qrs/`
- **http://www.whatever.something.com/abc/cba/**`wxy/qrs/`
- **http://www.whatever.something.com/abc/cba/wxy/**`qrs/`
- **http://www.whatever.something.com/abc/cba/wxy/qrs/**
- **Success!**

\normalsize


# Regular expressions

- We can summarize the URL subset grammar using *regular expression* notation.
- Not all grammars can be encoded this way, but those that can will admit the kind of efficient,
  left-to-right parsing shown on the previous slide.
- Most popular programming languages, and many text editors include support for regular expressions.
- The full grammar is expressed as `(http://)(([a-z]+)\.)+(com|org|edu)/(([a-z]+)/)*`
- `[a-z]` means any single lower case letter.
- `[a-z]+` means a string of one or more lower case letters.
- `\.` means a literal period.
- `(([a-z]+)\.)+` means one or more sequences of lower case letter strings separated by periods.

# Regular expressions

~~~~~~~~~~
(http://)(([a-z]+)\.)+(com|org|edu)/(([a-z]+)/)*
~~~~~~~~~~

- `(com|org|edu)` means one of either `com`, `org`, or `edu`.
- `(([a-z]+)/)*` means zero or more lower case letter strings separated by slashes.
- So \small `(http://)(([a-z]+)\.)+(com|org|edu)/(([a-z]+)/)*` \normalsize means:
    - `http://` followed by
    - one or more strings of lower case letters, separated by periods, followed by
    - one of either `com`, `org`, or `edu`,
    - followed by a slash, followed by
    - zero or more lower case letter strings separated by slashes.


# Abstract state machines

- We can diagram the rules for the URL subset grammar as a state transition diagram.
- States (circles) are situations or configurations of the parser.
- As we parse the string from left to right, we try to move from the start state (circle number 1) to the goal state (circle 7).
- If our input matches the label on an arc, we can follow that arrow.
- Otherwise we look for a default arc labeled with an asterisk.
- Our first diagram is almost deterministic, but may still require some backtracking.
- The second diagram adds some additional states and arcs, but is completely deterministic.

# Nondeterministic Finite State Automaton

![NFA Parser for URL grammar](nfa5.eps)


# Deterministic Finite State Automaton

![DFA Parser for URL grammar](dfa5b.eps)


# Top-down derivation

Derivation (a term you read in Rosen) is parsing in reverse.

- $\varphi$
- ${\forall}\textbf{v}\varphi$
- ${\forall}\textbf{v} (\varphi \leftrightarrow \varphi)$
- ${\forall}\textbf{v} (\varphi \leftrightarrow {\exists}\textbf{v}\varphi)$
- ${\forall}\textbf{v} (\textbf{Atom} \leftrightarrow {\exists}\textbf{v}\varphi)$
- ${\forall}\textbf{v} (\textbf{Atom} \leftrightarrow {\exists}\textbf{v} \textbf{Atom})$
- ${\forall}\textbf{v} (\textbf{Pt} \leftrightarrow {\exists}\textbf{v} \textbf{Atom})$
- ${\forall}\textbf{v} (\textbf{Pt} \leftrightarrow {\exists}\textbf{v} \textbf{Ptt})$
- ${\forall}\textbf{v} (\textbf{Pv} \leftrightarrow {\exists}\textbf{v} \textbf{Pvv})$
- ${\forall}\textbf{v} (\textbf{Pv} \leftrightarrow {\exists}\textbf{v} L\textbf{vv})$
- ${\forall}\textbf{v} (V\textbf{v} \leftrightarrow {\exists}\textbf{v} L\textbf{vv})$
- ${\forall}\textbf{v} (V\textbf{v} \leftrightarrow {\exists}z L\textbf{v}z)$
- ${\forall}x (Vx \leftrightarrow {\exists}z Lxz)$



# Rosen on vocabularies

> A *vocabulary* (or *alphabet*) $V$ is a finite nonempty set of
> elements, called *symbols*.  A *word* (or *sentence*) over $V$ is a
> string of finite length of elements of $V$. The *empty string* or
> *null string*, denoted by $\lambda$, is the string containing no
> symbols.  The set of all words over $V$ is denoted by $V^{*}$. A
> language over $V$ is a subset of $V^{*}$.

# Rosen on grammars

> A *phrase-structure grammar* $G = \langle V,T,S,P \rangle$ consists
> of a vocabulary $V$, a subset $T$ of $V$ consisting of terminal
> elements, a start symbol $S$ from $V$, and a set of productions
> $P$. The set $V - T$ is denoted by $N$. Elements of $N$ are
> called *nonterminal symbols.* Every production in $P$ must contain
> at least one nonterminal on its left side.

# Rosen on languages and derivability

> Let $G = \langle V,T,S,P \rangle$ be a phrase-structure grammar. Let
> $w_{0} = lz_{0}r$ (that is, the concatenation of $l$, $z_{0}$, and
> $r$) and $w_{1} = lz_{1}r$ be strings over $V$.  If $z_{0}
> \rightarrow z_{1}$ is a production of $G$, we say that $w_{1}$ is
> *directly derivable* from $w_{0}$ and we write $w_{0} \Rightarrow
> w_{1}$. If $w_{0}, w_{1},\ldots\, w_{n}, n \geq 0$, are strings over
> $V$ such that $w_{0} \Rightarrow w_{1}, w_{1} \Rightarrow w_{2},
> \ldots\, w_{n-1} \Rightarrow w_{n}$, then we say that $w_{n}$ is
> *derivable from* $w_{0}$, and we write $w_{0} \xRightarrow{*}
> w_{n}$.  The sequence of steps used to obtain $w_{n}$ from $w_{0}$
> is called a *derivation*.

. . .

> Let $G = \langle V,T,S,P \rangle$ be a phrase-structure grammar. The
> *language generated by* $G$ (or the *language of* $G$), denoted by
> $L(G)$, is the set of all strings of terminals that are derivable
> from the starting state S. In other words, $L(G) = \{w \in T^{*}|S
> \xRightarrow{*} w\}$.

# Production type determines grammar classification

Per Rosen, section 10.1:

- A *type 0* grammar has no restriction on its productions.
- A *type 1* grammar can have productions only of the form $w_{1}
  \rightarrow w_{2}$, where the length of $w_{2}$ is greater than or
  equal to the length of $w_{1}$, or of the form $w_{1} \rightarrow
  \lambda$.
- A *type 2* (context free) grammar can have productions only of the form $w_{1}
  \rightarrow w_{2}$, where $w_{1}$ is a single symbol that is not a
  terminal symbol.
- A *type 3* (regular) grammar can have productions only of the form $w_{1}
  \rightarrow w_{2}$ with $w_{1} = A$, and either $w_{2} = aB$ or
  $w_{2} = a$, where $A$ and $B$ are nonterminal symbols and $a$ is a
  terminal symbol, or with $w_{1} = S$ and $w_{2} = \lambda$.

# Regular Expressions

~~~~~~~~~~
(http://)(([a-z]+)\.)+(com|org|edu)/(([a-z]+)/)*

<protocol> ::= http://
<letter>   ::= a|b|c|d|e|f|g|h|i|j|k|l|m
<letter>   ::= n|o|p|q|r|s|t|u|v|w|x|y|z
<slash>    ::= /
<dot>      ::= .
<string>   ::= <letter><string>|<letter>
<host>     ::= <string><dot><host>|<string><dot>
<domain>   ::= com|org|edu
<site>     ::= <host><domain><slash>
<dir>      ::= <string><slash>
<body>     ::= <dir><body>|<dir>
<url>      ::= <protocol><site><body>|<protocol><site>
~~~~~~~~~~

# Context free, non-regular grammars

~~~~~~~~~~
<protocol> ::= http://
<letter>   ::= a|b|c|d|e|f|g|h|i|j|k|l|m
<letter>   ::= n|o|p|q|r|s|t|u|v|w|x|y|z
<slash>    ::= /
<dot>      ::= .
<string>   ::= <letter><string>|<letter>
<host>     ::= <string><dot><host>|<string><dot>
<domain>   ::= com|org|edu
<site>     ::= <host><domain><slash>
<dir>      ::= <string><slash>
<body>     ::= <dir><body>|<dir>
<url>      ::= <protocol><site><body>|<protocol><site>
~~~~~~~~~~




# Pushdown Automaton

![PDA Parser for the predicate logic grammar](pda6.eps)

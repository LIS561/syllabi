---
title: Artificial Languages, Part 1 (Syntax)
author: Dave Dubin
date: March 27, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# Key concepts for language topics

1. Syntax governs the *form* expressions of a language may take.
2. Semantics governs the *relationship* between language expressions and the *domain* we're modeling.
3. We have the usual formalist agenda of reducing our accounts of language to simple mathematical objects.
4. That agenda is partly in the service of understanding, but also our aim to process language expressions using software.
5. The cost of processing language is measured in processing time and memory.
6. The more expressive our language, the more expensive it will be to run our software over it.
7. Classifications of languages (like the Chomsky hierarchy) help us recognize what kind of software we need to
   accomplish our processing goals.

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

- ${\forall}w{\forall}x ((Fxw \wedge Aw) \rightarrow {\exists}y{\exists}z ((Pxy \wedge Ay) \wedge (Fxz \wedge Dz)))$
- ${\forall}\textbf{v}{\forall}\textbf{v} ((F\textbf{vv} \wedge A\textbf{v}) \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} ((P\textbf{vv} \wedge A\textbf{v}) \wedge (F\textbf{vv} \wedge D\textbf{v})))$
- ${\forall}\textbf{v}{\forall}\textbf{v} ((\textbf{Pvv} \wedge \textbf{Pv}) \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} ((\textbf{Pvv} \wedge \textbf{Pv}) \wedge (\textbf{Pvv} \wedge \textbf{Pv})))$
- ${\forall}\textbf{v}{\forall}\textbf{v} ((\textbf{Ptt} \wedge \textbf{Pt}) \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} ((\textbf{Ptt} \wedge \textbf{Pt}) \wedge (\textbf{Ptt} \wedge \textbf{Pt})))$
- ${\forall}\textbf{v}{\forall}\textbf{v}((\textbf{Atom} \wedge \textbf{Atom})\rightarrow{\exists}\textbf{v}{\exists}\textbf{v}((\textbf{Atom} \wedge \textbf{Atom}) \wedge (\textbf{Atom} \wedge \textbf{Atom})))$
- ${\forall}\textbf{v}{\forall}\textbf{v} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} ((\varphi \wedge \varphi) \wedge (\varphi \wedge \varphi)))$
- ${\forall}\textbf{v}{\forall}\textbf{v} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} ((\varphi \wedge \varphi) \wedge \varphi))$
- ${\forall}\textbf{v}{\forall}\textbf{v} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} (\varphi \wedge \varphi))$
- ${\forall}\textbf{v}{\forall}\textbf{v} (\varphi \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} (\varphi \wedge \varphi))$
- ${\forall}\textbf{v}{\forall}\textbf{v} (\varphi \rightarrow {\exists}\textbf{v}{\exists}\textbf{v}\varphi)$
- ${\forall}\textbf{v}{\forall}\textbf{v} (\varphi \rightarrow {\exists}\textbf{v}\varphi)$
- ${\forall}\textbf{v}{\forall}\textbf{v} (\varphi \rightarrow \varphi)$
- ${\forall}\textbf{v}{\forall}\textbf{v}\varphi$
- ${\forall}\textbf{v}\varphi$
- $\varphi$

\normalsize

# Parsing is a search through a space of possible solutions

We can go wrong!

-   ${\forall}w{\forall}x ((Fxw \wedge Aw) \rightarrow {\exists}y{\exists}z ((Pxy \wedge  Ay) \wedge (Fxz \wedge Dz)))$
- ${\forall}\textbf{v}{\forall}\textbf{v} ((F\textbf{vv} \wedge A\textbf{v}) \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} ((P\textbf{vv} \wedge A\textbf{v}) \wedge (F\textbf{vv} \wedge D\textbf{v})))$
- ${\forall}\textbf{v}{\forall}\textbf{v} ((\textbf{Pvv} \wedge \textbf{Pv}) \rightarrow {\exists}\textbf{v}{\exists}\textbf{v} ((\textbf{Pvv} \wedge \textbf{Pv}) \wedge (\textbf{Pvv} \wedge \textbf{Pv})))$
- ${\forall}\textbf{t}{\forall}\textbf{t} ((\textbf{Ptt} \wedge \textbf{Pt}) \rightarrow {\exists}\textbf{t}{\exists}\textbf{t} ((\textbf{Ptt} \wedge \textbf{Pt}) \wedge (\textbf{Ptt} \wedge \textbf{Pt})))$
- ${\forall}\textbf{t}{\forall}\textbf{t}((\textbf{Atom} \wedge \textbf{Atom})\rightarrow{\exists}\textbf{t}{\exists}\textbf{t}((\textbf{Atom} \wedge \textbf{Atom}) \wedge (\textbf{Atom} \wedge \textbf{Atom})))$
- ${\forall}\textbf{t}{\forall}\textbf{t} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{t}{\exists}\textbf{t} ((\varphi \wedge \varphi) \wedge (\varphi \wedge \varphi)))$
- ${\forall}\textbf{t}{\forall}\textbf{t} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{t}{\exists}\textbf{t} ((\varphi \wedge \varphi) \wedge \varphi))$
- ${\forall}\textbf{t}{\forall}\textbf{t} ((\varphi \wedge \varphi) \rightarrow {\exists}\textbf{t}{\exists}\textbf{t} (\varphi \wedge \varphi))$
- ${\forall}\textbf{t}{\forall}\textbf{t} (\varphi \rightarrow {\exists}\textbf{t}{\exists}\textbf{t} (\varphi \wedge \varphi))$
- ${\forall}\textbf{t}{\forall}\textbf{t} (\varphi \rightarrow {\exists}\textbf{t}{\exists}\textbf{t}\varphi)$
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



# Formalization: Rosen on vocabularies

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

# Phrase-structure grammar

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

# Chomsky hierarchy implications

- Regular languages (like our URL subset) can be summarized using DFAs, NFAs, and
  regular expressions.
- Therefore, their expressions can be parsed in very little time,
  using little memory.
- Our grammars for propositional and predicate logic are *not*
  regular, but they are context free.
- No regular expression is powerful enough to recognize any arbitrary
  logic expression, because logics admit arbitrarily deep levels of
  nesting: we can always open up a new set of parentheses, just as
  with Boolean search languages.
- Parsing non-regular, context free languages like our logic grammar
  always requires a stack memory, and often requires backtracking.
- We can usually tell that a language is not regular by seeing whether its productions meet Rosen's constraints.

# Context free, non-regular grammars

- $\textbf{v} \Coloneqq x|y|z|\ldots$
- $\textbf{c} \Coloneqq a|b|c|\ldots$
- $\textbf{t} \Coloneqq \textbf{v}|\textbf{c}$
- $\textbf{P} \Coloneqq P|Q|R|\ldots$
- $\textbf{Atom} \Coloneqq \textbf{Pt}_{1}\ldots\textbf{t}_{n}$ where $n$ is the arity of \textbf{P}
- $\varphi \Coloneqq \textbf{Atom}|\neg\varphi|(\varphi \wedge \varphi)|(\varphi \vee \varphi)|(\varphi \rightarrow \varphi)|(\varphi \leftrightarrow \varphi)|{\forall}\textbf{v} \varphi|{\exists}\textbf{v} \varphi$

# Caveats for the Rosen definitions

- Being regular and being context-free are really properties of languages, not grammars.
- Some grammars that don't satisfy Rosen's type 3 definition still summarize regular languages.
- It can be challenging to verify whether a language is regular just by looking at the productions.

# The URL subset is a regular language

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

# Context free, non-regular grammars

- ${\langle}const{\rangle} \Coloneqq a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p$
- ${\langle}var{\rangle}   \Coloneqq q|r|s|t|u|v|w|x|y|z$
- ${\langle}pred{\rangle}  \Coloneqq A|B|C|D|E|F|G|H|I|J|K|L|M$
- ${\langle}pred{\rangle}  \Coloneqq N|O|P|Q|R|S|T|U|V|W|X|Y|Z$
- ${\langle}lp{\rangle}    \Coloneqq ($
- ${\langle}rp{\rangle}    \Coloneqq )$
- ${\langle}quant{\rangle} \Coloneqq {\forall}|{\exists}$
- ${\langle}not{\rangle}   \Coloneqq \neg$
- ${\langle}binop{\rangle} \Coloneqq {\wedge}|{\vee}|{\rightarrow}|{\leftrightarrow}$
- ${\langle}term{\rangle}  \Coloneqq {\langle}const{\rangle}|{\langle}var{\rangle}$
- ${\langle}atom{\rangle}  \Coloneqq {\langle}pred{\rangle}{\langle}term{\rangle}|{\langle}atom{\rangle}{\langle}term{\rangle}$
- ${\langle}phi{\rangle}   \Coloneqq {\langle}atom{\rangle}|{\langle}not{\rangle}{\langle}phi{\rangle}|{\langle}quant{\rangle}{\langle}var{\rangle}{\langle}phi{\rangle}$
- ${\langle}phi{\rangle}   \Coloneqq {\langle}lp{\rangle}{\langle}phi{\rangle}{\langle}binop{\rangle}{\langle}phi{\rangle}{\langle}rp{\rangle}$


# Parsing context free languages

- Adding a stack memory to our NFA gives us a *push down automaton* (PDA).
- We only access a stack at one end: pushing a symbol on top, or
  popping one off and discarding it.
- We can't search for a symbol in the middle of a stack, but that
  means that stack access is always independent of how much material
  is stored there.
- Transitions on the next diagram include requirements for the next
  input symbol (just like the NFA), operations on the stack, or both.
- `-/-` means leave the stack unchanged;
- `/$` means push `$` on the top of the stack;
- `$/` means pop `$` off the top of the stack;


# Pushdown Automaton

![PDA Parser for the predicate logic grammar](pda6.eps)

---
title: From graphs to predicates
author: Dave Dubin
date: February 2019
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usecolortheme{lily}  
---


# Predicates

- A *predicate* is a kind of expression that represents a proposition.
- A predicate consists of a *predicate symbol* and one or more *arguments*.
- The layout of a predicate expression depends on which syntax we adopt.
- Examples: $Pb$, $Rabc$, $Qx$, $Tdxn$
- Examples: $Postman(b)$, $Reminds(a, b,c)$, $Quiet(x)$, $Thinking(d,x,n)$

# Propositions

- A *proposition* is the abstract content of a simple declarative sentence.
- "Eight is an integer" expresses the same proposition as "Ok estas entjero."
- "Jupiter is larger than Venus" expresses the same proposition as "Jupiter ist größer als die Venus".
- Propositions are the bearers of truth values: they are the kinds of
  things that can be true or false.
- Propositions are the objects of *propositional attitudes*. They are the kinds of things that
  can be believed, desired, doubted, expected, or feared.
  

# Predicate logic expressions

- Our predicate logic notation uses letters in three different ways.
- Lower case letters from the beginning of the Latin alphabet represent specific
  individual things in the domain we're modeling. Think of them like proper names.
- Lower case letters from the end of the alphabet (like $x$ and $y$) are variables
  that can denote different individuals under different assignments---just like 
  variables in algebraic expressions.  
- Capital letters represent properties that an individual might have, classes they
  might belong to, or relations they might stand in. Think of them like relations in
  a relational database.



# UML Class Diagram
![UML](CourseSection.eps)\ 




# Predicates for courses and sections

- $Px$ means "x is a person."
- $Sx$ means "x is a student."
- $Rx$ means "x is a professor."
- $Cx$ means "x is a course."
- $Nx$ means "x is a section."
- $Oxy$ means "x is a section of y."
- $Exy$ means "x is enrolled in y."
- $Ixy$ means "x is instructor for y."
- $Txy$ means "x is taking y."
- $Gxy$ means "x is teaching y."
- $a$ means "Adamo."
- $s$ means "Sofia."
- $m$ means "IS561"
- $o$ means "IS561-OA Spring 2019."

# Instance diagram
![RDF](courses2.eps)\ 

# Simple assertions

- Adamo is enrolled in IS561-OA: $Eao$
- Sofia is the instructor for IS561-OA: $Iso$
- IS561-OA is a section of IS561: $Oom$

# Logical Operators

![sl](logicTable.eps){width=350}\ 


  
# Examples of predicate logic expressions

- Predicates take a particular number of arguments, and the order matters. Let $Lxy$
  stand for the binary predicate "x loves y," $Vx$ stand for the unary predicate
  "x is a lover," and the propositional constants $r, j, o, d, i$ stand for Romeo,
  Juliet, Othello, Desdemona, and Iago, respectively.
- $Lrj$ means "Romeo loves Juliet."
- $(Lrj \wedge {\neg}Loi)$ means "Romeo loves Juliet, but Othello doesn't love Iago."
- ${\forall}x Lxd$ means "everyone loves Desdemona"
- ${\neg\exists}xLix$ means "Iago loves no one."
- ${\forall}x {\forall}y (Vx \rightarrow Lyx)$ means "everyone loves a lover."
- ${\forall}x (Vx \leftrightarrow {\exists}z Lxz)$ means "a lover is someone who loves."

# Quantifiers have scope

- The scope of a quantifier consists of the logical expression immediately following it. This means that one quantifier can be
  within the scope of another.
- Define $Cx$, $Px$, and $Rxy$ as meaning $x$ is a child, $x$ is a pony, and $x$ rode $y$, respectively.
- The ambiguous English sentence, "Every child was riding a pony" expresses two different propositions.
- We can express the first in logical form as ${\exists}x (Px \wedge {\forall}y (Cy \rightarrow Ryx))$. On this
  interpretation, there is some particular pony (or ponies) that every child rode.
- We can express the second as ${\forall}y (Cy \rightarrow  {\exists}x (Px \wedge Ryx))$. On this interpretation,
  every child was riding some pony, but no particular pony was necessarily ridden by every child.

# Translating to logical form

- Many English sentences admit more than one logical form. We say they
  are either syntactically or semantically \emph{ambiguous}.
- A syntactically ambiguous sentence has more than one parse. We'll
  have more to say about that in a few weeks, but one example is "I
  saw the man on the hill with the telescope."
- A semantically ambiguous parse has more than one interpretation, even
  with the same grammatical parse. Consider this argument from LeBlanc and Wisdom:
       - All fathers are parents;
       - All artists are dreamers;
       - Therefore, all fathers of artists are parents of artists and
         fathers of dreamers.
- Define the unary predicates $Ax$ and $Dx$ as "x is an artist" and "x
  is a dreamer," respectively.
- Define the binary predicates $Fxy$ and $Pxy$ as "x is the father of
  y" and "x is the parent of y," respectively.

# Translating to logical form

It seems natural to translate the argument this way:

- All fathers are parents: ${\forall}xy (Fxy \rightarrow Pxy)$
- All artists are dreamers: ${\forall}x (Ax \rightarrow Dx)$
- Therefore, all fathers of artists are parents of artists and
  fathers of dreamers:
  ${\forall}wx ((Fxw \wedge Aw) \rightarrow {\exists}yz ((Pxy \wedge Ay) \wedge (Fxz \wedge Dz)))$

. . .

That translation is not only natural, it also gives us a valid argument. But on reflection, a strict
reading of the first premise gives us this translation:

. . .

- All fathers are parents: ${\forall}xy (Fxy \rightarrow {\exists}z Pxz)$

. . .

In other words, "All fathers of anyone are parents of \emph{someone}. And the resulting
argument is \emph{not} valid.

# Inference and validity

- Just as with propositional logic, a conclusion follows validly from premises if it cannot be false
  when the premises are true.
- As with translation, our common sense and domain knowledge can set
  us up for surprises. Consider (courtesy of Prof. Smullyan) :
      - Everyone loves a lover;
      - Romeo loves Juliet;
      - Therefore, Othello loves Iago.

# Surprised?

- Everyone loves a lover
      - ${\forall}x {\forall}y (Vx \rightarrow Lyx)$
      - ${\forall}x (Vx \leftrightarrow {\exists}z Lxz)$
- Romeo loves Juliet
      - $Lrj$
- Therefore, Othello loves Iago.
      - $Loi$

# Formal grammar for first order logic

From your reading for this week:

- $\textbf{v} \Coloneqq x|y|z|\ldots$
- $\textbf{c} \Coloneqq a|b|c|\ldots$
- $\textbf{t} \Coloneqq \textbf{v}|\textbf{c}$
- $\textbf{P} \Coloneqq P|Q|R|\ldots$
- $\textbf{Atom} \Coloneqq \textbf{Pt}_{1}\ldots\textbf{t}_{n}$ where $n$ is the arity of \textbf{P}
- $\varphi \Coloneqq \textbf{Atom}|\neg\varphi|(\varphi \wedge \varphi)|(\varphi \vee \varphi)|(\varphi \rightarrow \varphi)|(\varphi \leftrightarrow \varphi)|{\forall}\textbf{v} \varphi|{\exists}\textbf{v} \varphi$

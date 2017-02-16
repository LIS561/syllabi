---
title: Predicate Logic, Part 2
author: Dave Dubin
date: February 13, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usecolortheme{lily}  
---


# Psalm 41:1
- "Blessed is he who considers the poor."
- Professor Marcus is looking for the answer ${\forall}x (Cx \rightarrow Bx)$
    - where $Cx$ means "x considers the poor"
    - and $Bx$ means "x is blessed."
- Suppose we want $C$ to be a two-place predicate, where the first
  argument represents the considering agent, and the second whatever
  receives the consideration.
- The most straightforward modification would be ${\forall}x (Cxp \rightarrow Bx)$
    - where individual $p$ ("the poor") picks out one or more poor
      persons in our domain of discourse.
    - The expression ${\forall}x{\forall}y (Cxy \rightarrow Bx)$ won't
      work, since that would be "blessed is he who considers anyone."
    - Using a propositional constant like $p$ presents a problem, but
      not because it represents an individual. An individual can be
      any identifiable thing in our domain, including a group.

# Domain diagram
![Domain](psalm41b.eps)\ 

# Domain diagram
![Domain](psalm41c.eps)\ 

# Domain diagram
![Domain](psalm41d.eps)\ 

# Psalm 41:1
- The problem is not that $p$ might pick out a group, but that:
    - "The poor" is a definite description, rather than a name.
    - That is to say, the term denotes unspecified individuals in the
      domain who are poor.
    - "Consideration" might be understood as a relation that obtains
       between individual persons, not between a person and a group.
- The next formulation we might consider is
  ${\forall}x{\forall}y ((Py \wedge Cxy) \rightarrow Bx)$, where $Py$ means "y is poor."

- This could be paraphrased "Everyone is blessed who considers any of the poor."

# Domain diagram
![Domain](psalm41e.eps)\ 

# Psalm 41:1
- The problem with 
  ${\forall}x{\forall}y ((Py \wedge Cxy) \rightarrow Bx)$
  is not that $x$ can be blessed, even if he doesn't consider the poor.
- The psalmist doesn't say that I'm blessed only if I consider the poor.

# Domain diagram
![Domain](psalm41h.eps)\ 


# Psalm 41:1
> - The problem with 
>   ${\forall}x{\forall}y ((Py \wedge Cxy) \rightarrow Bx)$
>   is not that $x$ can be blessed, even if he doesn't consider the poor.
> - The psalmist doesn't say that I'm blessed only if I consider the poor.

. . .

- If I believe that's the message, then I could write an implication in the other direction,
- \ldots such as ${\forall}x (Bx \rightarrow {\exists}y(Py \wedge Cxy))$
- The problem with
  ${\forall}x{\forall}y ((Py \wedge Cxy) \rightarrow Bx)$ is that this kind of reference "the poor," seems to
  presuppose that there are poor who need our consideration. But the expression is made true by a state of affairs
  in which no poor exist.

# Domain diagram
![Domain](psalm41i.eps)\ 


# Psalm 41:1
> - The problem with 
>  ${\forall}x{\forall}y ((Py \wedge Cxy) \rightarrow Bx)$
>  is not that $x$ can be blessed, even if he doesn't consider the poor.
> - The psalmist doesn't say that I'm blessed only if I consider the poor.
> - If I believe that's the message, then I could write an implication in the other direction,
> - \ldots such as ${\forall}x (Bx \rightarrow {\exists}y(Py \wedge Cxy))$
> - The problem with
>   ${\forall}x{\forall}y ((Py \wedge Cxy) \rightarrow Bx)$ is that this kind of reference "the poor," seems to
>   presuppose that there are poor who need our consideration. But the expression is made true by a state of affairs
>   in which no poor exist.

. . .

- The third proposal, in which we're blessed only if we consider the poor, also could be true
  in a world without poverty, provided it's also a world without blessings.

# Domain diagram
![Domain](psalm41a.eps)\ 


# Domain diagram
![Domain](psalm41f.eps)\ 

# Domain diagram
![Domain](psalm41g.eps)\ 


# Domain diagram
![Domain](atTheGymB.eps)\ 


# Domain diagram
![Domain](atTheGym.eps)\ 



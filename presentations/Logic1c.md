---
title: Existential quantification and closed vs. open worlds
author: Dave Dubin
date: March 2019
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usecolortheme{lily}  
---

# Inference rule from last week

~~~~~~~~~~~~~~~~~~~~
needstool(Recipe,Tool,Property) :-
   stepin(Step,Recipe),
   utool(Step,Tool),
   realizes(Tool, Property).
~~~~~~~~~~~~~~~~~~~~

- If a step in a recipe uses a tool that realizes a property, then the recipe needs that tool for the property.
- ${\forall}w {\forall}x {\forall}y {\forall}z (((Swx \wedge Uwy) \wedge Ryz ) \rightarrow Nxyz)$
- However, our data usually doesn't specify both the tool and the property. One or the other is mentioned alone.

# Using existential quantification

- With predicate logic we could deduce the existence of a needed tool from a property that it should realize.
- ${\forall}x {\forall}y {\forall}z ((Rxy \wedge Syz) \rightarrow {\exists}w Nxwz)$
- This is a powerful inference, since it lets us reason about one or more individuals that aren't specified.
- But Datalog doesn't give us full existential quantification for reasoning.






# Instance Diagram
![instances](Ingredient2.eps)\ 

# Datalog assertions

~~~~~~~~~~~~~~~~~~~~
% Ingredient side
requires(sccs,chicken).
hasconstit(chicken,chickenthighs).
hasquant(chicken,lbs2).
satisfies(chicken,bonein).
satisfies(chicken,skinned).
satisfies(chicken,trimmed).
~~~~~~~~~~~~~~~~~~~~

# Instance Diagram
![instances](StepTool3.eps)\ 

# Datalog assertions

~~~~~~~~~~~~~~~~~~~~
% Step and tool side
includes(sccs,step2).
dfollows(step2p1,step2p2).
hsubstep(step2,step2p1).
utool(step2p1,slowcooker).
utool(step2p2,thing1).
realizes(thing1,diced).
~~~~~~~~~~~~~~~~~~~~

# Rules of inference

~~~~~~~~~~~~~~~~~~~~
% A recipe needs a tool if a step in the recipe uses
% the tool or if the recipe requires an ingredient
% satisfying a property

needstool(Recipe,something,Property) :-
   requires(Recipe,Ingredient),
   satisfies(Ingredient, Property).
~~~~~~~~~~~~~~~~~~~~

${\forall}x {\forall}y {\forall}z ((Rxy \wedge Syz) \rightarrow Nxaz)$

# Rules of inference

~~~~~~~~~~~~~~~~~~~~
% A recipe needs a tool if a step in the recipe uses the
% tool or if the recipe requires an ingredient satisfying
% a property

needstool(Recipe,Tool,Property) :-
   stepin(Step,Recipe),
   utool(Step,Tool),
   realizes(Tool, Property).
~~~~~~~~~~~~~~~~~~~~

${\forall}w {\forall}x {\forall}y {\forall}z (((Swx \wedge Uwy) \wedge Ryz ) \rightarrow Nxyz)$

# Rules of inference

~~~~~~~~~~~~~~~~~~~~
% A recipe needs a tool if a step in the recipe uses
% the tool or if the recipe requires an ingredient
% satisfying a property

needstool(Recipe,Tool,someproperty) :-
   stepin(Step,Recipe),
   utool(Step,Tool),
   not realizes(Tool, _).
~~~~~~~~~~~~~~~~~~~~

${\forall}w {\forall}x {\forall}y {\forall}z (((Swx \wedge Uwy) \wedge {\neg}Ryz ) \rightarrow Nxyb)$

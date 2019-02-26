---
title: Modeling with predicates in Datalog
author: Dave Dubin
date: February 2019
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usecolortheme{lily}  
---

# Instance Diagram
![instances](Instances2.eps)\ 

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

# Inverse relationship, domain, and codomain

~~~~~~~~~~~~~~~~~~~~
% Inverse, domain and codomain for 'realizes'
realizedby(Property,Tool) :- realizes(Tool,Property).
qproperty(Property) :- realizes(_,Property).
tool(Tool) :- realizes(Tool,_).
~~~~~~~~~~~~~~~~~~~~

- ${\forall}x {\forall}y (Rxy \rightarrow Byx)$
- ${\forall}x {\forall}y (Rxy \rightarrow Qy)$
- ${\forall}x {\forall}y (Rxy \rightarrow Tx)$

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

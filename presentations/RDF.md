---
title: The Resource Description Framework
author: Dave Dubin
date: March 2019
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usepackage{mathabx}  
---

# Key ideas for tonight

1. RDF is an abstract syntax for modeling a domain, and a family of published language specifications.
2. RDF uses IRI (aka URI) identifiers to name things. These act like constants in predicate logic.
3. RDF has several concrete syntaxes for serializing descriptions.
4. Many domain-specific and application-specific languages use RDF as a framework.
5. Other modeling languages use RDF as a basis.

# An RDF example from an earlier presentation
![instances](Instances2.eps)\

# Abstract vs. concrete syntax

- The turtle format discussed tonight is a *concrete syntax* definition.
- It is governed by a formal grammar that defines what strings count as valid expressions.
- An *abstract syntax* is a model for the data structure produced when a conforming expression is parsed.
- RDF's data model is a *graph*: a set of *vertices* and a set of *edges* that connect the vertices.

# RDF's graph model

- A statement in RDF consists of three parts: a *subject,* a *predicate,* and an *object*.
    - The subject: what's being talked about;
    - The predicate: a property it has or a binary relationship it stands in;
    - The object: the value of the property, or the other participant in the relationship.
- In RDF, all properties are *reduced* to binary relationships.
- So just as suggested by the diagram, subjects and objects can be understood as vertices in a directed graph, where relationships
  serve as the graph edges.

# IRIs are the new URIs

- URIs include URL web addresses and URNs: Uniform Resource Names.
- IRIs are *internationalized* identifiers (we have more lexical options).
- Identifiers for resources in RDF look like web addresses.
- Considering RDF in isolation, we can pretend that this resemblance is purely coincidental.
- Of course, it's not just a coincidence: the web architecture has everything to do with RDF applications.
- But we run the risk of blurring a role distinction in our minds: IRIs as identifiers vs. URLs as addresses.


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


# Turtle statements

~~~~~~~~~~~~~~~~~~~~
:sccs :requires :chicken .
:chicken :hasConstituent :chickenthighs .
:chicken :hasQuantity :lbs2 .
:chicken :satisfies :bonein .
:chicken :satisfies :skinned .
:chicken :satisfies :trimmed .
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


# Turtle statements

~~~~~~~~~~~~~~~~~~~~
:sccs :includes :step2 .
:step2p2 :directlyFollows :step2p1 .
:step2 :hasSubStep :step2p1 .
:step2p1 :usesTool :slowcooker .
:step2p2 :usesTool :thing1 .
:thing1 :realizesProperty :diced .
~~~~~~~~~~~~~~~~~~~~




# Class and property declarations in RDF

~~~~~~~~~~~~~~~~~~~~
@prefix : <http://is561.org/Recipes#> .

:Recipe a owl:Class .
:Ingredient a owl:Class .

:requires a owl:ObjectProperty ;
	rdfs:domain :Recipe ;
	rdfs:range :Ingredient .
~~~~~~~~~~~~~~~~~~~~



# RDF serialization formats

RDF can be serialized in a variety of different formats. Each is a concrete syntax for RDF.

- RDF/XML
- Turtle
- N-Triples
- JSON-LD
- \ldots and others.

# Using remote classes

\small

~~~~~~~ 
@prefix : <http://example.com/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

:David_Dubin rdf:type foaf:Person .
:iSchool rdf:type org:Organization .
~~~~~~~ 

\normalsize



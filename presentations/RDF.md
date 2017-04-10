---
title: The Resource Description Framework
author: Dave Dubin
date: April 10, 2017
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
![A state of affairs diagram](rdfex3.eps)

# Abstract vs. concrete syntax

- The syntax formalization we read in Rosen's chapter is for *concrete syntax* definition.
- That is to say, phrase structure grammars help us define what strings count as valid expressions in a language.
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

# Instances with classes
![Classes and instances](rdfex2.eps)

# Instance relationships in RDF

\small

~~~~~~~
@prefix : <http://example.com/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
:Dubin2007 rdf:type :Appointment ;           
    :start_date "09/01/2007"^^xsd:string ;
    :appointee :David_Dubin ;
    :appointing_organization :GSLIS ;
    :appointed_position :Research_Associate_Professor .
~~~~~~~ 

\normalsize

Compare with: $((((Aa \wedge Sab) \wedge Ead) \wedge Oag) \wedge Par)$

Compare with: $Abdgr$ 


# Class declarations in RDF

\small

~~~~~~~ 
@prefix : <http://example.com/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix event: <http://purl.org/NET/c4dm/event.owl#> .
:Appointment rdf:type rdfs:Class ;
   rdfs:subClassOf event:Event .
org:Post rdf:type rdfs:Class ;
   rdfs:subClassOf org:Role .
:Faculty_Position rdf:type rdfs:Class ;
   rdfs:subClassOf org:Post .
~~~~~~~ 

\normalsize


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
:GSLIS rdf:type org:Organization .
:Research_Associate_Professor rdf:type :Faculty_Position .

~~~~~~~ 

\normalsize



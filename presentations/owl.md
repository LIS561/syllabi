---
title: The OWL Ontology Language
author: Dave Dubin
date: April 2019
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# OWL is an RDF-based language

~~~~~~~~~~
:Dubin2007 a owl:NamedIndividual , :Appointment ;
	:appointed_position :Research_Associate_Professor ;
	:appointee :David_Dubin ;
	:appointing_organization :GSLIS ;
	:start_date "09/01/2007"^^xsd:string .
~~~~~~~~~~

\tiny

    <owl:NamedIndividual rdf:about="http://example.com/Dubin2007">
      <rdf:type rdf:resource="http://example.com/Appointment"/>
      <appointed_position rdf:resource="http://example.com/Research_Associate_Professor"/>
      <appointee rdf:resource="http://example.com/David_Dubin"/>
      <appointing_organization rdf:resource="http://example.com/GSLIS"/>
      <start_date rdf:datatype="http://www.w3.org/2001/XMLSchema#string">09/01/2007</start_date>
    </owl:NamedIndividual>

\normalsize


# Protege instance view

![Protege graph](protege.eps)

# Classes stand in hierarchical relationships

~~~~~~~~~~
:Appointment a owl:Class ;
	rdfs:subClassOf event:Event ;
	skos:definition """A period of time during which an 
        agent occupies a professional role or post.""" .
~~~~~~~~~~
. . .

- ${\forall}x (Ax \rightarrow Ex)$
- $A_D \subseteq E_D$
- $Appointment \sqsubseteq Event$

# Classes stand in hierarchical relationships

![Comparison to UML](UML7.eps)


# Classes stand in non-hierarchical relationships

~~~~~~~~~~
event:Event a owl:Class ;
	owl:disjointWith foaf:Person .
~~~~~~~~~~
. . .

- $\neg{\exists}x (Ex \wedge Px)$
- $E_D \cap P_D = \emptyset$
- $Event \sqcap Person \equiv \bot$

# Object properties obtain between resources

~~~~~~~~~~
:appointing_organization a owl:ObjectProperty ;
	rdfs:subPropertyOf event:agent ;
	owl:inverseOf :organization_appoints ;
	rdfs:domain :Appointment ;
	rdfs:range org:Organization ;
	rdfs:label "appointing organization"@en .
~~~~~~~~~~
. . .

- $appOrg \sqsubseteq agent$
- $appOrg^{-} \equiv orgAppoints$
- ${\exists}appOrg.\top \sqsubseteq Appointment$
- $\top \sqsubseteq {\forall}appOrg.Organization$

# Data Properties connect resources and data structures

~~~~~~~~~~
:start_date a owl:DatatypeProperty ;
	rdfs:domain event:Event ;
	rdfs:range xsd:string ;
	rdfs:label "start date" .

:Dubin2007 a owl:NamedIndividual , :Appointment ;
	:appointed_position :Research_Associate_Professor ;
	:appointee :David_Dubin ;
	:appointing_organization :GSLIS ;
	:start_date "09/01/2007"^^xsd:string .
~~~~~~~~~~
. . .

$startDate^{\mathcal{I}} \subseteq Event^{\mathcal{I}} \times \mathcal{D}$

# Complex classes

~~~~~~~~~~
:Material_Resource a owl:Class ;
    owl:equivalentClass [ a owl:Class ;
     owl:intersectionOf ( :Resource :PhysicalObject ) ] .
~~~~~~~~~~

. . .

$MaterialResource \equiv PhysicalObject \sqcap Resource$

. . .

~~~~~~~~~~
:Teaching_Resource a owl:Class ;
  owl:equivalentClass [ a owl:Restriction ;
    owl:hasValue :Teaching ;
    owl:onProperty :supports ] .
~~~~~~~~~~

. . .

$TeachingResource \equiv {\exists}supports.\{Teaching\}$

# Complex classes

~~~~~~~~~~
:Faculty_Member a owl:Class ;
  rdfs:subClassOf foaf:Person ;
  owl:equivalentClass [ a owl:Restriction ;
    owl:onProperty :has_appointment ;
    owl:someValuesFrom :Faculty_Appointment ] .

:Faculty_Appointment a owl:Class ;
  rdfs:subClassOf :Appointment ;
  owl:equivalentClass [ a owl:Restriction ;
    owl:onProperty :appointed_position ;
    owl:someValuesFrom :Faculty_Position ] .
~~~~~~~~~~

. . .

- $FacultyMember \sqsubseteq Person$
- $FacultyMember \equiv {\exists}hasAppointment.FacultyAppointment$
- $FacultyAppointment \sqsubseteq Appointment$
- $FacultyAppointment \equiv {\exists}appointedPosition.FacultyPosition$



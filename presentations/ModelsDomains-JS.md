---
title: Models and Domains
author: Jodi Schneider (based on slides from Dave Dubin)
date: January 26, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{mathtools}
  - \usepackage{amssymb}
csl: apa-annotated-bibliography.csl
references:
- id: jubien_platonism_1997
  type: chapter
  author:
  - family: Jubien
    given: Michael
  issued:
  - year: '1997'
  title: Platonism
  container-title: 'Contemporary Metaphysics: An Introduction'
  publisher: Blackwell
  publisher-place: Cambridge MA
  page: '36-62'

- id: reicher_2009
  type: chapter
  author:
  - family: Reicher
    given: Maria
  issued:
  - year: '2009'
  title: Introduction
  container-title: 'States of Affairs'
  publisher: Ontos Verlag
  publisher-place: Frankfurt
  page: '7-37'

- id: ferraris_social_2011
  type: chapter
  author:
  - family: Ferraris
    given: Maurizio
  editor:
  - family: Sartor
    given: Giovanni
  - family: Casanovas
    given: Pompeu
  - family: Biasiotti
    given: Mariangela
  - family: Fernández-Barrera
    given: Meritxell
  issued:
  - year: '2011'
  title: Social Ontology and Documentality
  container-title: 'Approaches to Legal Ontologies: Theories, Domains, Methodologies'
  publisher: Springer
  publisher-place: Dordrecht
  page: '83-97'
...
---

# Information Modeling
 - This class is called "Information Modeling."
 - That suggests the course is about modeling information.
 - But we're actually going to learn about modeling parts of the world.
 - It's more accurate to say we'll be modeling *with* information,
 - or modeling for purposes of keeping track of information.

# Today
 - Today I want to introduce some vocabulary in an informal way.
 - Over the next few weeks we will explore more formal understandings of these concepts.
 - Today I'll introduce you to a diagrammatic notation that we'll come back to in later presentations.

# Reality and Domains of Discourse
 - We will introduce formal definitions of a domain of discourse later.
 - For today, we'll define a domain of discourse as some part of reality
   that we wish to represent in a model.
 - Consider three categories of things we might believe are real:
   physical things, abstract things, and social things [@jubien_platonism_1997; @ferraris_social_2011].

# Physical things

Physical things exist in space and time: if they exist, then there is
some place and time where we can find them. Examples include:

 - The particular chair you're sitting in right now.
 - Particular sound waves reaching your ears at this moment.
 - The electric current circulating through wires in this room.
 - The seat back that is part of your chair.
 - Any specific atomic particle from which the chair is composed.

# Social things

Social things exist in time, but not in space. Examples include:

 - My marriage.
 - The mortgage on my house.
 - The promise I made to my partner to remember to pay the mortgage on time.
 - The University of Illinois School of Information Sciences.

# Abstract things

Abstract things are not found in the physical universe. They don't come into
existence, nor are they destroyed or modified. Examples include:

 - The number eleven.
 - Every physically possible configuration of Lego building blocks.
 - The property of being red.
 - The proposition that I am employed by the University if Illinois.
 - The relationship "employed by the University of Illinois."
 - The state of affairs "Jodi's being employed by the University of Illinois."
 - The state of affairs "Dave's being employed by the University of Illinois."

# Properties
Michael Jubien (1997) offers an accessible introduction to the Platonistic conception of
abstract things like properties. A property, he says, is "a way something can be."
His examples include:

 - green
 - hot
 - slimy
 - hungry
 - four-legged
 - dead
 - married
 - flat
 - soluble
 - "having been a female US President before 1997"

# Relationships
Jubien uses the term "relation" for a part of abstract reality that I'll call "relationship,"
so as to keep it distinct from a mathematical object that might or might not be the same thing.
Jubien's examples of relation(ships) include:

 - the "betweenness" relationship that can obtain among integers (like 4 is between 3 and 5);
 - the "betweenness" relationship that can obtain among physical objects in space;
 - the instantiation relationship that can link a property to a particular thing that exemplifies the property;

# Relational properties

 - Jubien distinguishes between the "love" relationship obtaining between Jack and Jill
   and the relational properties "being loved by Jack," and "being loved by Jill."
 - In several of the models we shall examine in this class, all properties are *reduced*
   to relationships.
 - In models such as RDF, these relational properties can only obtain between
   exactly two individuals (binary relationships only).

# Propositions

 - Propositions are abstract bearers of truth values.
 - That is to say, they're the kinds of things that can be true or false.
 - Propositions are language-independent entities. You can think of
   them as the information content of simple declarative sentences.
 - The Platonistic conception of propositions has them outside of
   time and space.
 - So a proposition is not in your mind: it's the kind of thing with respect to which you can
   stand in a relationship such as belief or desire.

# Propositions are language-independent
  - It's Thursday.
  - C'est jeudi.
  - t\'{a} s\'{e} D\'{e}ardaoin.

  
# States of Affairs (1)
 - States of affairs are the parts of reality responsible for making
  propositions true or false.
 - A state of affairs is "a way the actual world must be in order to make some given proposition about the actual world true; in other words, a state of affairs (situation) is a truth-maker, whereas a proposition is a truth-bearer." (Wikipedia, glossing the Stanford Encyclopedia of Philosophy) 
 - "a state of affairs (situation) is a truth-maker, whereas a proposition is a truth-bearer. Whereas states of affairs (situations) either obtain or fail-to-obtain, propositions are either true or false." (Wikipedia, glossing the Stanford Encyclopedia of Philosophy)
 - Also called "situations"

# State of affairs diagram
![Dave's being employed by the University of Illinois](rdfex1.eps)
 
# States of Affairs (2)  
 - Maria E. Reicher [-@reicher_2009] characterizes the "standard conception" of
  states of affairs as: "complex entities, consisting of particulars,
  (universal) properties and relations, such that an atomic state of
  affairs is a particular's exemplifying a property (or one or more
  particulars' exemplifying a relation)."

# Summary of concepts (1)
- **Domain of discourse**: Some part of reality that we wish to represent in a model.
- **Physical thing**: Something that's bounded in both time and space.
- **Abstract thing**: Something that's bounded in neither time nor space, but may have a physical expression or instantiation.
- **Social thing**: Something bounded in time, but not space, and is essentially connected to the context of its creation.

# Summary of concepts (2)
- **Property**: A way something could be.
- **Relationship**: A way two or more things could be with respect to each other.
- **Relational property**: A way something could be in virtue of its particpation in a relationship.
- **Proposition**: A language-independent bearer of truth values and object of propositional attitudes like belief.
- **State of affairs**: A particular's exemplifying a property, or one or more
  particulars' exemplifying a relation.

# Further Reading
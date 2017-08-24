---
title: What does logic have to do with information management?
author: Dave Dubin
date: Fall Semester, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{syllogism}  
  - \usepackage{mathtools}
---

# "Bene disserere est finis logices"

- Most logic books (including your assigned reading) introduce propositional
  logic as a tool or system for analyzing the validity and soundness of reasoning.

- van Benthem, et al. contrast arguments like this invalid one:

. . .

\syllog[(2.4)]{If you take my medication, you will get better}{But you are not taking my medication}{So, you will not get better.}

. . .

- \ldots with this valid argument:

\syllog[(2.6)]{If you take my medication, you will get better}{But you are not getting better}{So, you have not taken my medication.}


# Reasoning vs. representation

- In this class we'll give some attention to logical reasoning and inference.
- The same rules that govern valid argumentation also enable information systems to answer interesting questions.
- But it takes an entire semester course in logic before you start to get good at logical inference.
- This semester we'll focus mainly on logic as a means to express the contents of our information systems.

# Logic for machine reasoning

- Our information systems typically store facts, so that we can retrieve them later.
- But sometimes it will make more sense to store a combination of
  facts and rules, and *deduce* facts we haven't explicitly stored.
- If we can express a rule in logic, then that's precise enough to encode it in computer software.
- Consider this business rule:

. . .

\syllog{Any full-time employee is eligible for overtime pay}{Linda is a full-time employee}{So, Linda is eligible}

# Logic for precise description

- Another advantage of logic is that it forces us to spell out our assumptions in precise
  detail.

- This way, we don't rely on common sense and background knowledge that computers don't have.

- The following argument looks correct at first, but it's not logically valid:

. . .

\syllog{Dave always leaves the lights on overnight}{The lights were off overnight yesterday}{Yesterday someone left after Dave left}

# Why isn't that argument logically valid?

\syllog{Dave always leaves the lights on overnight}{The lights were off overnight yesterday}{Yesterday someone left after Dave left}

This argument relies on unstated background knowledge:

. . .

1. Dave was here yesterday.
2. Lights can't be both off and on at the same time.

. . .

That's the kind of information we often have to be reminded that computers can't figure out on their own.


---
title: Quantifier scope
author: Dave Dubin
date: September 23, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usepackage{mathabx}
---

# Stronger claims and weaker claims

- Consider the following assertion: "every student reads some Shakespeare plays."
- There are at least two ways to read this, a stronger claim and a weaker claim.
- The stronger claim is that there are *certain particular* plays by Shakespeare that
  every student reads (for example, they all read *Macbeth*, *Hamlet*, and *King Lear*).
- The weaker claim is that no student avoids reading Shakespeare entirely, but that
  the students might read any Shakespeare play. Some might read *Othello*, for example,
  and other students might read *The Tempest*.
- We say the second claim is weaker because there are a larger number of scenarios
  consistent with the claim.
- We say the first claim is stronger because it rules out a larger number of situations.

# No play is read by every student

![Every student reads some plays](Shakespeare.eps)\

\  

# Some play is read by every student

![Every student reads some particular plays](Shakespeare2.eps)\

\ 

# The claim vs. what might be true

- A sentence like "every student reads some Shakespeare plays" is usually understood
  (here in the US) to assert the weaker claim.
- That interpretation is natural if we're familiar with how American students are
  assigned literature to read by their teachers.
- But it might happen to be true that the every student in the US reads *Macbeth*
  and *Hamlet*. In that case, the stronger claim is true.
- Even if that stronger claim is supported by the facts, we probably still interpret
  the sentence to express the weaker claim.

# Quantifier combinations act like functions

- The weaker claim for "every student reads some Shakespeare plays" has this logical form: ${\forall}x{\exists}y(Sx \rightarrow (Py \wedge Rxy))$.
- Notice the existentially quantified variable $y$ is to the right (and therefore in the *scope*) of the universally quantified variable x.
- We can think of that $y$ as a *function* of each universally quantified variable that has it in its scope. For example, our diagra could
  be represented as:
   - $s1 \rightarrow {\langle}m,k{\rangle}$
   - $s1 \rightarrow {\langle}m,k{\rangle}$
   - $s1 \rightarrow {\langle}m,k{\rangle}$
   - $s1 \rightarrow {\langle}m,k{\rangle}$
   





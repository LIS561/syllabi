---
title: Predicate logic translation exercise
author: Dave Dubin
date: September 25, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usepackage{mathabx}  
---

# Alternate translations

Consider these proposed translations of the assertion, "all walkways are within rooms."

i. ${\forall}x(Kx \rightarrow {\exists}y(Ry \wedge Ixy))$ ($Kx$: x is a walkway; $Rx$: x is a room; $Ixy$: x is within y).
ii. ${\forall}x{\exists}y((Kx \wedge Ry) \rightarrow Ixy)$ ($Kx$: x is a walkway; $Rx$: x is a room; $Ixy$: x is within y).
iii. ${\forall}x{\forall}y((Kx \wedge Ixy) \rightarrow Ry)$ ($Kx$: x is a walkway; $Rx$: x is a room; $Ixy$: x is within y).
iv. ${\forall}x{\forall}y((Rx \wedge Iyx) \rightarrow Ky)$ ($Kx$: x is a walkway; $Rx$: x is a room; $Ixy$: x is within y).
v. ${\exists}y(Ry \wedge {\forall}x(Kx \rightarrow Ixy))$ ($Kx$: x is a walkway; $Rx$: x is a room; $Ixy$: x is within y).

### Question 1: translation i vs. translation iii

Explain the difference between translations i and iii in your own words. Give an example of a situation that would falsify
translation iii, but not translation i.

### Question 2: translation iii vs. translation iv

Explain the difference between translations iv and iii in your own words. Give an example of a situation that would falsify
translation iv, but not translation iii.

### Question 3: translation i vs. translation v

Explain the difference between translations i and v in your own words. Give an example of a situation that would falsify
translation v, but not translation i.

### Question 4: translation 1 vs. translation ii

Explain the difference between translations i and ii in your own words. Give an example of a situation that would falsify
translation i, but not translation ii.

### Question 5: Best translations

Which of these five translations are plausible on some understanding of the assertion, "all walkways are within rooms."
For each translation that is *not* plausible, explain in one sentence why it doesn't capture any meaning of the assertion.

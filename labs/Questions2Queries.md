---
title: Competency questions, logic, and queries
author: Dave Dubin
date: February 15, 2018
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usepackage{mathabx}  
---

### Group exercise: work collectively as a class

"Are there pathways in work spaces, for which the room capacity must not exceed 49 occupants, less than 28 inches in width?"

- $P(x)$ (x is a pathway)
- $S(x)$ (x is a work space)
- $O(x,y)$ (x has occupancy limit y)
- $I(x,y)$ (x is located within y)
- $W(x,y)$ (x has width in inches y)
- $L(x,y)$ (x is less than y)

${\exists}w{\exists}x{\exists}y{\exists}z(Px \wedge (Sy \wedge (O(y,z) \wedge (L(z,50) \wedge (W(x,w) \wedge L(w,28))))))$

- $P = \{{\langle}x,y,z{\rangle}|$pathway x in space y has width in inches z$\}$
- $S = \{{\langle}x,y{\rangle}|$space x has occupancy limit y$\}$

${\sigma}_{(P.y = S.x) \wedge (S.y < 50) \wedge (P.z < 28)} (P \times S)$
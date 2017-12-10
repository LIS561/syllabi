---
title: Limitations of Description Logics
author: Dave Dubin
date: December 4, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usepackage{mathabx}
---

# Things to know about description logic limitations

1. Syntactic limitations on individual statements: the grammars of DLs like $\mathcal{SROIQ}$ prevent us
   from saying some things that are easy to express in predicate logic.

2. Structural limitations: some DL features can't be used together in
   the same ontology. So even though the assertions and definitions
   may validate on a statement-by-statement basis, statements in
   combination with each other may be disallowed. That's because the
   decidable and computationally efficient procedures our reasoners
   use won't work if we go beyond the limitations of our DL.

# Running example: defining "native"

- To illustrate these limitations, we'll use the concept "native,"
  defined as someone who lives in the country they were born in.

- Consider a class of persons, a class of countries, two binary
  relations "born in" and "lives in," and six individuals: Jane, Jim,
  Nancy, Norman, Germany, and USA.

- Jane was born in the USA and lives in Germany. Jim is the
  converse. Nancy and Norman are natives of Germany and the USA,
  respectively.

- The range and domain of both relations are **Person** and **Country**,
  respectively. So in predicate logic, we say that $Bxy$ is true if person
  $x$ was born in country $y$.

# Native born in predicate logic

Predicate Logic                                                         English
----------------------------------------------------------------------- --------------------------------------------------------------------------------------
${\forall}x{\forall}y(Lxy \rightarrow (Px \wedge Cy))$                  \tiny 'Lives in' has domain Person and range Country. \normalsize
${\forall}x{\forall}y(Bxy \rightarrow (Px \wedge Cy))$                  \tiny 'Born in' has domain Person and range Country. \normalsize
$((Pi \wedge Pj) \wedge (Pn \wedge Po))$                                \tiny Jim and Jane and Nancy and Norman are people. \normalsize
$(Cg \wedge Cu)$                                                        \tiny Germany and the USA are countries. \normalsize
$((Bju \wedge Ljg) \wedge (Big \wedge Liu))$                            \tiny Jane and Jim are not natives. \normalsize
$((Bng \wedge Lng) \wedge (Bou \wedge Lou))$                            \tiny Nancy and Norman are natives of Germany and the USA. \normalsize
${\forall}x(Nx \leftrightarrow {\exists}y(Cy \wedge (Bxy \wedge Lxy)))$ \tiny A native lives in the country they were born in. \normalsize
${\forall}x{\forall}y((Bxy \wedge Lxy) \rightarrow Nx)$                 \tiny Same idea without ${\exists}$ quantifier. \normalsize
${\forall}x{\forall}y(Lxy \leftrightarrow Ryx)$                         \tiny Define $R$ as the inverse of $L$.
${\forall}x{\forall}y((Bxy \wedge Ryx) \rightarrow Nx)$                 \tiny Using $R$ ("country has resident") \normalsize

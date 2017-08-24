---
title: What is a Propositional Logic Expression?
author: Dave Dubin
date: Fall Semester, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{syllogism}  
  - \usepackage{mathtools}
---

# What is a propositional logic expression?

A propositional logic expression is:

1. A written or printed string of symbols.
2. But not just any symbols: only certain symbols are allowed.
3. The order of the symbols *must* conform to some specific rules.

# What symbols are allowed in a propositional logic expression?

1. Lower case letters from the English alphabet are allowed.
2. We'll sometimes specify certain specific lower case letters, and use only those.
    - For example, maybe just b, g, k, o, p, r. 
3. Parentheses are allowed.
4. Spaces are allowed.
5. These special symbols are allowed:
    - $\neg$ (pronounced "not")
    - $\wedge$ (pronounced "and")
    - $\vee$ (pronounced "or")
    - $\rightarrow$ (pronounced "implies")
    - $\leftrightarrow$ (pronounced "if and only if")

# First rule: a letter by itself

- Any of the lower case letters we've decided to use is a conforming expression.
- So each of the following is a propositional logic expression:
    - $p$
    - $q$
    - $r$
    - $b$
    - $g$
    - $k$

# Second rule: $\neg$ to the left of any conforming expression

- We can put a $\neg$ symbol immediately to the left of any conforming expression to make a different
  conforming expression.
- So each of the following is a propositional logic expression:
    - ${\neg}p$
    - ${\neg}q$
    - ${\neg}{\neg}p$
    - ${\neg}{\neg}{\neg}p$
    - ${\neg}{\neg}{\neg}{\neg}{\neg}{\neg}{\neg}{\neg}{\neg}r$

# Third rule: $\wedge$ and parentheses

- If we put the $\wedge$ symbol between any two conforming
  expressions, and put parentheses around the whole thing, then the
  result is a conforming expression.
- So each of the following is a propositional logic expression:
    - $(p \wedge r)$
    - $(p \wedge p)$
    - $(p \wedge {\neg}r)$
    - $(p \wedge (p \wedge q))$    
    - $(p \wedge {\neg}(p \wedge q))$
    - $(p \wedge (p \wedge {\neg}q))$
    - $((p \wedge p) \wedge {\neg}q)$    
    - $(r \wedge (p \wedge {\neg}(p \wedge q)))$

# Fourth through sixth rules: $\rightarrow \vee \leftrightarrow$

- Rules 4, 5, and 6 are the same as rule 3, but for $\rightarrow \vee \leftrightarrow$
- So each of the following is a propositional logic expression:
    - $(p \rightarrow q)$
    - $(p \vee {\neg}(p \leftrightarrow q))$
    - $((r \wedge {\neg}q) \leftrightarrow (p \vee {\neg}(p \rightarrow q))$


# Seventh rule: nothing else

- The most important rule: nothing that fails to conform to rules 1--7 is a propositional
  logic expression.

- Some strings of symbols obviously don't conform:

   - $))))))))))(((((((((($
   - $\wedge \wedge p q r \neg$
   - $(\leftrightarrow p \rightarrow)$
   - $(p \neg r)$

- But sometimes it's harder to spot the problem. What's wrong with these?

    - $p \wedge r$
    - $(p \wedge p \wedge q)$


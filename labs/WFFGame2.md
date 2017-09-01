---
title: Advanced Logic Game
author: IS561
---


Introduction
------------

The advanced version of the logic game is played using the same rules
as the introductory version. However, in this game players use all the
game materials, and there is an additional restriction on the formulas
you may write on the worksheet.

Materials
---------

1. The dice with the logical symbols and the propositional letters are used exactly the same as in the introductory game.
2. The six colored plastic cubes correspond to propositional letters on the dice:
    - The blue cube corresponds to the letter 'b'.
    - The green cube corresponds to the letter 'g'.
    - The black cube corresponds to the letter 'k'.
    - The orange cube corresponds to the letter 'o'.
    - The pink cube corresponds to the letter 'p'.
3. The tetrahedral (triangular) die is used to generate a random number from 1 to 4. The number rolled is the
   upright number at the base of the triangle.


Preparing the game
------------------

Draw two ovals at the top of the playing sheet, labeled "TRUE" and
"FALSE." Each oval should be large enough for all six colored cubes to
fit inside.


Playing the game
----------------

1. Roll the triangular tetrahedral die to determine how many of the six colored cubes should be placed in the "TRUE" oval.
2. Draw that number of colored cubes randomly from the drawstring bag, and place them in the "TRUE" oval. The propositions represented
   by these cubes are understood to be true.
3. Place the remaining colored cubes in the "FALSE" oval. The propositions represented by these cubes are understood to be false.
4. Shake and throw the six dice, just as you did in the introductory game.
5. Each group member writes a conforming expression using as many symbols as possible, just as in the introductory game. But
   **the entire formula must be true with respect to the truth values of the available propositional letters**. 


**Table 1: Logic Symbols**

  **Symbol**   **Logical Operation**
  ------------ ----------------------------
  →            implication (if…then)
  ↔            equality (if and only if)
  ¬            negation (not)
  ∧            conjunction (and)
  ∨            inclusive disjunction (or)



Tables
------

**Truth table for conjunction**

     $p$       $q$         $p \wedge q$ 
 ----------- -------- ----------------------
      0         0               0            
      0         1               0            
      1         0               0            
      1         1               1            


**Truth table for disjunction**


     $p$       $q$          $p \vee q$  
 ----------- -------- ----------------------
      0         0               0            
      0         1               1            
      1         0               1            
      1         1               1            


**Truth table for implication**

     $p$       $q$         $p \rightarrow q$ 
 ----------- -------  --------------------------
      0         0                  1              
      0         1                  1              
      1         0                  0              
      1         1                  1              


**Truth table for "if and only if"**

     $p$       $q$         $p \leftrightarrow q$ 
 ----------- --------   --------------------------
      0         0                  1                  
      0         1                  0                  
      1         0                  0                  
      1         1                  1                  







**Table 2: Truth Table for Logical Implication (→)**

  ***p***   ***q***   ***p → q***
  --------- --------- -------------
      T         T           T
      T         F           F
      F         T           T
      F         F           T

**Table 3: Truth Table for Logical Equality (↔)**

  ***p***   ***q***   ***p ↔ q***
  --------- --------- -------------
     T         T           T
     T         F           F
     F         T           F
     F         F           T

**Table 4: Truth Table for Logical Negation (¬)**

  ***p***   ***¬p***
  --------- ----------
     T         F
     F         T
 
**Table 5: Truth Table for Logical Conjunction (∧)**

  ***p***   ***q***   ***p $\wedge$ q***
  --------- --------- ------------------
     T         T               T
     T         F               F
     F         T               F
     F         F               F

**Table 6: Truth Table for Logical Inclusive Disjunction (∨)**

  ***p***   ***q***   ***p ∨ q***
  --------- --------- -------------
     T         T           T
     T         F           T
     F         T           T
     F         F           F

Example of Game Play
--------------------

Brett, Ian, Kavya, Linh, Melina, and Zhang are playing again.
Brett rolls a 2 on the tetrahedral die, and Zhang draws two colored cubes at random from the drawstring bag.
These turn out to be the orange cube and the blue cube, and so Zhang put them in the "TRUE" oval, and the other
four colored cubes in the "FALSE" oval.


Kavya rolls the six white dice and
generates the following results: p, r, k, →, →, ∧. Kavya places the p, r and k results near the "FALSE" oval
as a reminder that propositions p, r and k (the pink, red and black cubes) are false.

Melina will write the first expression. This exercise is challenging


From this they
assemble the following formula: (¬ g→r) ∧r

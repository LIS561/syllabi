---
title: Greek letters and other typographic cues
author: Dave Dubin
date: September, 2017
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usepackage{mathabx}
---

# What's with the Greek letters?

- The authors of *Logic in Action* use Greek letters in many of the
  tables and definitions in chapter 2.

- For example, Definition 2.5 on page 2-11 looks like this:

. . .

Let $P$ be a set of proposition letters and let $p \in P$. 

The following expression defines the recursive grammar for a logical
expression $\varphi$ in [Backus–Naur Form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form):

$\varphi \Coloneqq p|\neg\varphi|(\varphi \wedge \varphi)|(\varphi \vee \varphi)|(\varphi \rightarrow \varphi)|(\varphi \leftrightarrow \varphi)$

. . .

- Why use a Greek letter here?

- Short answer: the parentheses, $\wedge$, $\rightarrow$, $\leftrightarrow$, and $\vee$ are symbols that literally appear in a logical expression.
- The $\varphi$ itself doesn't appear in the expression, but represents some entire expression that already conforms to the rules.

# The truth tables from chapter 2

Example 2.18 from van Benthem, et al.


  $\varphi$   $\neg\varphi$
 ----------- ---------------
      0            1
      1            0	

  $\varphi$   $\psi$   ($\varphi \wedge \psi$)   ($\varphi \vee \psi$)   ($\varphi \rightarrow \psi$)   ($\varphi \leftrightarrow \psi$)
 ----------- -------- ------------------------- ----------------------- ------------------------------ ---------------------------------- 
      0         0                0                         0                       1                              1                          
      0         1                0                         1                       1                              0                          
      1         0                0                         1                       0                              0                          
      1         1                1                         1                       1                              1                           


# Examples

- $\mathit{a,b,c}$
- $\mathcal{P,Q,R}$
- $\theta, \lambda, \rho, \sigma, \pi$


# Greek alphabet

         Letter                    Spel           MP        mp
-----------------------------  -----------    ---------- ----------
  $A \alpha$                     Alpha         Alfah      Alfah
  $B \beta$                      Beta          Beyta      Veetah
  $\Gamma \gamma$                Gamma         Gammah     Wammah
  $\Delta \delta $               Delta         Dehltah    Dheltah
  $E \epsilon \varepsilon$       Epsilon       Epsilon    Epsilon
  $Z \zeta$                      Zeta          Zeytah     Zeetah
  $H \eta  $                     Eta           Eytah      Eetah
  $\Theta \theta$                Theta         Theytah    Theetah
  $I \iota   $                   Iota          Iota       Yotah
  $K \kappa   $                  Kappa         Kaepah     Kahpah
  $\Lambda \lambda$              Lambda        Laemdah    Lahmdhah
  $M \mu   $                     Mu            Moo        Mee
  $N \nu   $                     Nu            Noo        Nee
  $\Xi \xi $                     Xi            Zaye       Ksee
  $O o     $                     Omicron       Ohmikron   Ohmikrron
  $\Pi \pi $                     Pi            Paye       Pee
  $P \rho  $                     Rho           Roh        Rroh
  $\Sigma \sigma $               Sigma         Sigmah     Seewmah
  $T \tau   $                    Tau           Tauw       Tahf
  $\Upsilon \upsilon $           Upsilon       Upsilon    Eepsilon
  $\Phi \phi \varphi $           Phi           Faye/Fee   Fee
  $X \chi          $             Chi           Kaye       Hee
  $\Psi \psi       $             Psi           Saye       Psee
  $\Omega \omega   $             Omega         Ohmeygah   Ohmeywah


# Final slide






# Properties, categories, and relationships in predicate logic

The categories, properties, and relationships on this worksheet have
been proposed by your classmates in the highlighting exercise. The
last challenge for each example is to translate the entire rule into
predicate logic. Skip these exercises (5, 9, and 13) during your first
session with this worksheet, and return to them after trying the
translation exercises in chapter 4.

It may be helpful to review Bach chapter 1 on the relationship between
language and the world. Note especially the diagram on page 10.

*Logic in Action* chapter 4 uses individual capital letters for
 predicate symbols instead of (Bach's) English words. Arguments to those
 predicates do not require parentheses, but the logical operators
 still do (see the grammar in section 4.5).


Worked example:

"A stairwell is separated from a building area if and only if the
separating door is closed."

Entity categories:

- *stairwell* (predicate = $Sx$)
- *door* (predicate = $Dx$)
- *building area* (predicate = $Ax$)

Properties:

- *closed* (domain = *door*; predicate = $Cx$)

Relationships:

- *separated from* (domain = *stairwell*, *area*; predicate = $Fxy$)
- *separates* (domain = *door*, *stairwell*, *area*; predicate = $Txyz$)

The rule in logic: ${\forall}x{\forall}y ((Sx \wedge Ay) \rightarrow (Fxy \leftrightarrow {\exists}z(Dz \wedge Tzxy)))$

------------------------------------

Consider this rule based on the Idaho Exit Access Requirements:

"An exit door leads to a public way if and only if a pathway connects
the exit door to the public way."

1. Identify the two most important *relationships* in this rule.

2. For each relationship, identify the two or three categories of
   entity that participate in the relationship.

3. Propose either a two-place or three-place predicate to
   denote/represent each of the relationships.

4. Propose a one-place predicate to denote/represent each
   of the entity categories you specified in question 2.

5. Express the entire rule as a predicate logic expression.


Consider this rule:

"If a pathway from a door to a public way is at least as wide as the
door, then the pathway is unobstructed."

6. What is the key relationship in this rule? Propose a predicate to
   represent that relationship.

7. What categories of entity participate in the relationship
   identified in question 6? Represent them with unary (one-place)
   predicates.

8. What other property is important in this rule? What kind of thing
   can have the property? Represent each of them using unary (one-place)
   predicates.

9. Express the entire rule as a predicate logic expression.

Consider this rule:

"All walkways within a room are clear if and only if every such walkway
allows access to every exit within the room."

10. Identify the two most important *relationships* in this
   rule. Propose binary (two place) predicates to denote/represent
   these relationships.

11. For each relationship, identify the two categories of entity that
    participate in the relationship. Represent the categories with unary
    (one-place) predicates.

12. What other property is important in this rule? Represent it with a
    unary predicate.

13. Express the entire rule as a predicate logic expression.


